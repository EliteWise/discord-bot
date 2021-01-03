from core.util.channel_id import get_channel_id_by_feature_name
from discord.ext import commands
import json


class Giveaway(commands.Cog):
    def __init__(self, bot, giveaway_message_id):
        self.bot = bot
        self.giveaway_message_id = giveaway_message_id
        self.giveaway_emoji = '\N{BALLOT BOX WITH CHECK}'
        self.players = []

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = user.guild.get_channel(await get_channel_id_by_feature_name("giveaway"))

        if channel is None:
            return

        if reaction.message.id == self.giveaway_message_id and channel and reaction.emoji == self.giveaway_emoji:
            # Prevent bot from playing
            if user.display_name != "Odyssia":
                self.players.append(user.mention)
            # Save list of players in json file
            with open('core/data/giveaway.json', 'w') as outfile:
                json.dump(self.players, outfile)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = user.guild.get_channel(await get_channel_id_by_feature_name("giveaway"))

        if channel is None:
            return

        if reaction.message.id == self.giveaway_message_id and channel and reaction.emoji == self.giveaway_emoji:
            # Trying to re-add reaction but doesn't work at the moment
            await reaction.message.add_reaction(self.giveaway_emoji)