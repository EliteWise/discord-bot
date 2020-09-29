import logging

from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Cette commande prend un ou plusieurs paramètres.")
        elif isinstance(error, commands.CommandNotFound) or isinstance(error, commands.NotOwner):
            pass
        else:
            logging.warning(error)


def setup(bot):
    """
    Setup cog to be able to listen events & commands inside this class
    Without this class, the module command_error_handler.py cannot be load
    """
    bot.add_cog(ErrorHandler(bot))