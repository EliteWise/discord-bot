from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="clear")
    async def clear_channel(self, ctx, limit):
        await ctx.channel.purge(limit=int(limit))


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Clear(bot))