import discord
from discord.ext.commands import bot
from core.model.player import Player


@bot.command()
async def player_stats(ctx):
    player = Player()
    await ctx.send(player.getName() + "\n" +
                   "top1: " + player.getTop1() + "\n"
                   "kills: " + player.getKills() + "\n"
                   "deaths: " + player.getDeaths())
