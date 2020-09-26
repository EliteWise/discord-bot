from discord.ext import commands


class Invitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="invitation")
    async def invitation_configuration(self, ctx):
        pass


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Invitation(bot))