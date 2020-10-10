import discord
from discord.ext import commands
from core.util.db import createVote, removeVote, getVotefile, getTable, getVote
from matplotlib import pyplot as plt
from core.util.delete_emote import add_delete_emote
import os

class votesEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        votesf = getVotefile()
        for messageid in votesf:
            db = getTable(str(reaction.message.guild.id), "votes", arguments= f"WHERE messageid= {messageid}")
            # if messageid == str(reaction.message.id):
            #     if reaction.emoji.id == "🗑" and reaction.message.author.guild_permissions.manage_messages or reaction.message.author.guild_permissions.administrator:
            #         await reaction.message.channel.delete()
            #         print(f"{db[1][3]} - {db[1]}")
            #         channel = self.bot.get_channel(int(db[1][3]))
            #         message = await channel.fetch_message(db[1][2])
            #         await message.delete()
            #         removeVote(str(reaction.message.guild.id), messageid)
            #     elif reaction.emoji.id == "�":
                data = getVote(db[1][0])
                names = [d for d in data]
                values = [len(data.get(d)) for d in data]
                plt.bar(names, values)
                plt.savefig(fname='plot')
                channel = self.bot.get_channel(int(db[1][3]))
                message = await channel.send(file=discord.File('plot.png'))
                await add_delete_emote(self.bot, str(message.id), str(message.channel.id))
                os.remove('plot.png')
            elif messageid == str(db[0][2]):
                if messageid is None: print("eroned id !"); removeVote(str(reaction.message.guild.id), messageid); continue
                for emoji in votesf.get(messageid):
                    if reaction.emoji == emoji:
                        votes = getVotefile.get(messageid).get(emoji)
                        print(votes)
                        votes[emoji].append(user)
                        print(votes)
            

            
def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(votesEvent(bot))  