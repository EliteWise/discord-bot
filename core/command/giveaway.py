import asyncio
import json
import os
import random
import logging
from math import floor

from discord.ext import commands
from core.event import giveaway
from main import bot


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giveaway_message_id = None
        self.log = logging.getLogger("command/giveaway")

    @commands.command(name="giveaway")
    async def create_giveaway(self, ctx, name, duration, prizes_size):
        channel = ctx.guild.get_channel(719257870822277174)
        days = int(duration)/24
        hours_left = int(duration) % 24
        duration_day_converter = str(round(days)) + " jours" if int(hours_left) == 0 else str(floor(days)) + " jour(s) et " + str(hours_left) + " heure(s)"
        message = await channel.send(f"Un giveaway {name} vient d'être lancé !"
                                     f"\nIl se terminera dans " + str(duration_day_converter) +
                                     f"\n{prizes_size} joueurs seront tirés au sort !")
        emoji = '\N{BALLOT BOX WITH CHECK}'
        self.giveaway_message_id = message.id
        await message.add_reaction(emoji)
        self.bot.add_cog(giveaway.Giveaway(self.bot, self.giveaway_message_id))

        bot.loop.create_task(self.hided_task(duration, channel, name, prizes_size))
        # Process can continue, the task is in background

    async def hided_task(self, duration, channel, name, prizes_size):
        await asyncio.sleep(int(duration))
        self.log.info("Timer done!")

        with open('core/data/giveaway.json') as json_file:
            data = json.load(json_file)
            random_pick = random.sample(data, int(prizes_size))
            display_winners = ' | '.join(str(player) for player in random_pick)
            self.log.info("Winners > " + display_winners)

        await channel.send(f"Le giveaway {name} vient de se terminer ! " + (f"\nLe gagnant est: {display_winners}" if len(random_pick) == 1 else f"\nLes gagnants sont: {display_winners}"))


def setup(bot):
    bot.add_cog(Giveaway(bot))
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
