import logging

from discord.ext import commands
from core.util.channel_id import get_channel_id_by_command_name


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Cette commande prend un ou plusieurs paramètres.")
        elif isinstance(error, commands.CommandNotFound):
            pass
        else:
            raise error


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(ErrorHandler(bot))