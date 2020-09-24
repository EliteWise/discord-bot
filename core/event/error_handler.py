from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument) and ctx.command.name == "stats":
            await ctx.send("Saisis le pseudo d'un joueur pour voir ses stats.")
        else:
            raise error


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(ErrorHandler(bot))