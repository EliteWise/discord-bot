import asyncio
import logging
from discord.ext import commands
from core.util.constant import Constant
from core.util.permission import is_admin
from core.util.server_status import update_status
from core.util.channel_id import get_channel_id_by_command_name


class ServerStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server-status")
    @commands.check(is_admin)
    async def start_status_task(self, ctx):

        channel = ctx.guild.get_channel(await get_channel_id_by_command_name(ctx, ctx.command.name))

        if channel is None:
            return

        loop = asyncio.get_event_loop()
        loop.create_task(update_status(channel, Constant.HOSTNAME, 10))

    @commands.command(name="maintenance")
    @commands.check(is_admin)
    async def set_maintenance(self, ctx, status):
        """
        :param ctx: A command must always have at least one parameter, ctx, which is the Context
        :param status: Define the status of the maintenance, it can be on or off
        :return: Change the announcement message in the server-status channel
        """
        channel = ctx.guild.get_channel(await get_channel_id_by_command_name(ctx, "server-status"))

        if channel is None:
            return

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