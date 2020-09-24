from discord.ext import commands


class LinkChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="link")
    async def link(self, ctx, feature_name):
        pass