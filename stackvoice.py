import discord
from toolbox.botvar import bot
import toolbox.utils.db as db
from toolbox.utils.errors import error
from toolbox.utils.errors import error

@bot.command()
async def stackvoice(ctx, channelname:str, channeltype:str):
    if ctx.message.author.guild_permissions.manage_messages or ctx.message.author.guild_permissions.administrator:
        if channeltype.lower() not in ["yes", "y", "no", "n"]: await error(ctx, "unkown privacy type, please read the help command"); return 
        if channeltype.lower() == "yes": channeltype = "y"
        if channeltype.lower() == "no": channeltype = "n"
        channeltype = channeltype.upper()

        guild = ctx.message.guild
        channel = await guild.create_voice_channel(channelname)
        channelid = channel.id
        serverid = ctx.message.guild.id

        db.addChannel(serverid, channelid, channeltype)
        await ctx.send(f":white_check_mark: a stacked chanel named `{channelname}` was sucessfully created !")
    else:
        await error(ctx, "ouuuups, you can't do that :/")