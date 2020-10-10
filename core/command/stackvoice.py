import discord
from discord.ext import commands
import core.util.db as db

class stackvoice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stackvoice")
    async def stackvoice(self, ctx, channelname:str, channeltype:str):
        if ctx.message.author.guild_permissions.manage_messages or ctx.message.author.guild_permissions.administrator:
            if channeltype.lower() not in ["yes", "y", "no", "n"]: await ctx.send("unkown privacy type, please read the help command"); return 
            if channeltype.lower() == "yes": channeltype = "y"
            if channeltype.lower() == "no": channeltype = "n"
            channeltype = channeltype.upper()

            guild = ctx.message.guild
            channel = await guild.create_voice_channel(channelname)
            channelid = channel.id
            serverid = ctx.message.guild.id

            db.addChannel(serverid, channelid, channeltype)
            await ctx.send(f":white_check_mark: a stacked chanel named `{channelname}` was sucessfully created !")
        else:
            await ctx.send("ouuuups, you can't do that :/")

def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(stackvoice(bot))