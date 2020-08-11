from [bot variable file] import bot
import discord
from [db file] import getActiveChannelsPrivate


@bot.command()
async def chadd(ctx, user: discord.Member):
    try:
        if ctx.author.voice.channel is not None:
            channel = ctx.author.voice.channel
            if getActiveChannelsPrivate(str(channel.id)) == "Y":
                await channel.set_permissions(user, view_channel=True)
                await ctx.send(f":white_check_mark: {user.name} have been aded to your channel")
            else:
                await ctx.send("your channel is not private !")
        else:
            await ctx.send("you need to be in a voice channel to perform this command !")
    except AttributeError:
        await ctx.send("you need to be in a voice channel to perform this command !")



        