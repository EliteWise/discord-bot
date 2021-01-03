from core.util.channel_id import get_channel_id_by_command_name
from discord.ext import commands
from core.util import player_request


class PlayerStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats")
    async def player_stats(self, ctx, player_name):
        """
        :param ctx: Context of the command
        :param player_name: Name of a player who has already connected at least once to the server
        :return: Display stats by player_name
        """
        try:
            # Get the channel chosen by the owner to display statistics
            channel = ctx.guild.get_channel(await get_channel_id_by_command_name(ctx, ctx.command.name))

            if channel is None:
                return

            player = player_request.getStats(player_name)
            await channel.send(f">>> **[{player.name}]**" +
                           f"\nPoints: {player.points}" +
                           f"\nTop1: {player.top1}" +
                           f"\nKills: {player.kills}" +
                           f"\nDeaths: {player.deaths}")

        except IndexError:
            await channel.send("Ce joueur ne s'est jamais connecté sur Odyssia ou n'existe pas.")


def setup(bot):
    """
    Setup cog to be able to listen events & commands inside this class
    Without this class, the module player_stats.py cannot be load
    """
    bot.add_cog(PlayerStats(bot))