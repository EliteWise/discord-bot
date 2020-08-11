import discord
from [bot variable file] import bot
import [db file]

@bot.command()
async def stackvoice(ctx, channelname:str, channeltype:str):
    if ctx.author.top_role < ctx.me.top_role: await ctx.send( "You are not a server administrator !"); return

    if channeltype.lower() not in ["yes", "y", "no", "n"]: await ctx.send("unkown privacy type, please read the help command"); return 
    if channeltype.lower() == "yes": channeltype = "y"
    if channeltype.lower() == "no": channeltype = "n"
    channeltype = channeltype.upper()

    guild = ctx.message.guild
    channel = await guild.create_voice_channel(channelname)
    channelid = channel.id
    serverid = ctx.message.guild.id

    db.addChannel(serverid, channelid, channeltype)
    await ctx.send(f":white_check_mark: a stacked chanel named `{channelname}` was sucessfully created !")