from discord.ext import commands
from core.util.permission import is_admin


class Invitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="invitation")
    @commands.check(is_admin)
    async def invitation_configuration(self, ctx):
        pass


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Invitation(bot))