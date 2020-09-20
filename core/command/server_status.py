import logging
from discord.ext import commands


class ServerStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="maintenance")
    async def set_maintenance(self, ctx, status):
        """
        :param ctx: A command must always have at least one parameter, ctx, which is the Context
        :param status: Define the status of the maintenance, it can be on or off
        :return: Change the announcement message in the server-status channel
        """
        channel = ctx.guild.get_channel(756791389097820210)
        messages = await channel.history(limit=1000).flatten()
        logging.info("Maintenance > " + status.upper())

        await messages[-1].edit(content="Les serveurs Odyssia sont " + ("**en maintenances** !" if status.lower() == "on" else "**accessibles à tous** !"))
        # Delete command message
        await ctx.message.delete()


def setup(bot):
    """
    Setup cog to be able to listen events & commands inside this class
    Without this class, the module giveaway.py cannot be load
    """
    bot.add_cog(ServerStatus(bot))