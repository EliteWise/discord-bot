import discord
from discord.ext import commands
from core.util.db import dictTable, addActivechannel, getActiveChannels, removeActivechannel, removeChannel, getActiveChannelsPrivate

try:
    class stackvoiceEvent(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.Cog.listener()
        async def on_voice_state_update(self, user, before, after):
            if (before.channel is None and after.channel is not None) or (before.channel != after.channel and after.channel != None): #player join event/ player change channel event
                firstchannelpos = user.voice.channel.category
                channelid = user.voice.channel.id
                server = user.guild
                if str(channelid) in dictTable(server.id, "stackedchannels"): #check if joined channel was in stacked channel database
                    db = dictTable(server.id, "stackedchannels")
                    if db.get(str(channelid)) == "N": #is channel private
                        channel = await server.create_voice_channel(user.name, category= firstchannelpos)
                        await user.move_to(channel)
                        if channel.id in getActiveChannels():
                            return
                        addActivechannel(str(channel.id), "N")
                    if db.get(str(channelid)) == "Y": #is channel private
                        channel = await server.create_voice_channel("[P]"+user.name, category= firstchannelpos)
                        await user.move_to(channel)
                        if channel.id in getActiveChannels():
                            return
                        addActivechannel(str(channel.id), "Y")
                        for member in server.members:
                            if member.bot: await channel.set_permissions(member, view_channel=True); continue
                            await channel.set_permissions(member, view_channel=False)
                        await channel.set_permissions(user, view_channel=True)

                        
        
            for channelid in getActiveChannels(): #when a player leave, check alls created channels for delete they if they was empty
                channel = self.bot.get_channel(int(channelid))
                if channel is None: print("eroned id !"); removeActivechannel(channelid); continue
                if channel.members == []:
                    removeActivechannel(channelid)
                    server = channel.guild
                    await channel.delete()
                
        @commands.Cog.listener()
        async def on_guild_channel_delete(self, channel): #delete the channel drom the database when he was deleted
            server = channel.guild
            channelid = channel.id
            if str(channelid) in dictTable(server.id, "stackedchannels"):
                removeChannel(str(server.id), str(channelid))

    def setup(bot):
        """Setup cog to be able to listen events & commands inside this class"""
        bot.add_cog(stackvoiceEvent(bot))
        
except discord.errors.NotFound:
    pass