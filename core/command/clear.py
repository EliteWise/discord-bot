from discord.ext import commands
from core.util.permission import is_admin


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.check(is_admin)
    async def clear_channel(self, ctx, limit):
        """
        :param ctx: Context of the command
        :param limit: The amount of messages to erase
        :return: Clear theses messages in the current channel
        """
        try:
            await ctx.channel.purge(limit=int(limit))
        except Exception:
            pass


def setup(bot):
    """
    Setup cog to be able to listen events & commands inside this class
    Without this class, the module clear.py cannot be load
    """
    bot.add_cog(Clear(bot))