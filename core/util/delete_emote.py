import discord
from discord.ext import commands
from discord.utils import get as discordget
from core.util.db import addDelatableMessage, getDelatableMessages, removeDelatableMessage, getVote
import asyncio

class delete_emote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def on_reaction_add(self, reaction, channel):
        for messageid in getDelatableMessages():
            if messageid == str(reaction.message.id):
                channel = self.bot.get_channel(int(getDelatableMessages().get(str(messageid))))
                message = await channel.fetch_message(messageid)
                if messageid is None: print("eroned id !"); removeDelatableMessage(messageid); continue
                if reaction.emoji == "🗑" and message.author.guild_permissions.manage_messages or message.author.guild_permissions.administrator:
                    await message.delete()
                    removeDelatableMessage(messageid)

async def add_delete_emote(bot, messageid:str, channelid:str):
    channel = bot.get_channel(int(channelid))
    message = await channel.fetch_message(messageid)
    await message.add_reaction("🗑")
    await asyncio.sleep(5)
    addDelatableMessage(str(messageid), str(channelid))


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(delete_emote(bot))