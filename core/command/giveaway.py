import asyncio
import json
import random
import logging
from math import floor

from core.util.channel_id import get_channel_id_by_command_name
from core.util.permission import is_admin
from discord.ext import commands
from core.event import giveaway
from main import bot


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giveaway_message_id = None
        self.log = logging.getLogger("command/giveaway")

    @commands.command(name="giveaway")
    @commands.check(is_admin)
    async def create_giveaway(self, ctx, name, duration, prizes_size):
        """
        :param str name: The name of the giveaway
        :param int duration: How long the giveaway will last in hours
        :param int prizes_size: The number of winners (1 prize per winner)
        """
        channel = ctx.guild.get_channel(await get_channel_id_by_command_name(ctx, ctx.command.name))

        if channel is None:
            return

        days = int(duration)/24
        hours_left = int(duration) % 24
        duration_day_converter = str(round(days)) + " jours" if int(hours_left) == 0 else str(floor(days)) + " jour(s) et " + str(hours_left) + " heure(s)"
        message = await channel.send(f"Un giveaway {name} vient d'être lancé !"
                                     f"\nIl se terminera dans " + str(duration_day_converter) +
                                     f"\n{prizes_size} joueurs seront tirés au sort !")
        emoji = '\N{BALLOT BOX WITH CHECK}'
        self.giveaway_message_id = message.id
        await message.add_reaction(emoji)

        # Put the message id to know what is the right message in giveaway events
        self.bot.add_cog(giveaway.Giveaway(self.bot, self.giveaway_message_id))
        # Process can continue, the task run in background
        bot.loop.create_task(self.hided_timer_task(duration, channel, name, prizes_size))

    async def hided_timer_task(self, duration, channel, name, prizes_size):
        """Only suspends the current task, allowing other tasks to run"""
        await asyncio.sleep(int(duration))
        self.log.info("Timer done!")

        # Retrieve data stored in json file
        # It will be used for failure recovery in the future
        with open('core/data/giveaway.json') as json_file:
            data = json.load(json_file)
            random_pick = random.sample(data, int(prizes_size))
            display_winners = ' | '.join(str(player) for player in random_pick)
            self.log.info("Winners > " + display_winners)

        await channel.send(f"Le giveaway {name} vient de se terminer ! " + (f"\nLe gagnant est: {display_winners}" if len(random_pick) == 1 else f"\nLes gagnants sont: {display_winners}"))


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Giveaway(bot))
