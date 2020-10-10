#vote command
import discord
from discord.ext import commands
from core.util.delete_emote import add_delete_emote
import asyncio
from core.util.db import createVote

class Votes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def timeout(self, author, admin_channel):
        try:
            await self.bot.get_user(author).send(f":alarm_clock: you don't reply on the vote configuration, the vote administration channel has been deleted, we can try later...")
            await admin_channel.delete()
            pass
        except discord.ext.commands.errors.CommandInvokeError or discord.errors.NotFound:
            pass

    @commands.command(name="vote")
    async def vote(self,ctx):
        guild = ctx.guild
        author = ctx.message.author.id
        cdata = {}
        perms= {
            guild.default_role: discord.PermissionOverwrite(read_messages=False)
        }
        admin_channel = await guild.create_text_channel(f"{ctx.channel}_admin", overwrites=perms, category= ctx.message.channel.category)
        await admin_channel.send(f"<@{author}> we will configure the votes !")

        ###############################################################
        #Vote Settings
        ###############################################################
        message = await admin_channel.send(f"Set a vote title:")
        def checkm(message):
            return message.channel == admin_channel and message.author.id == author
        try:
            title = await self.bot.wait_for('message',timeout= 120.0, check=checkm)
        except asyncio.TimeoutError:
            await self.timeout(author, admin_channel)
            pass
        
        message = await admin_channel.send(f"Send the end date:")
        try:
            end = await self.bot.wait_for('message',timeout= 120.0, check=checkm)
        except asyncio.TimeoutError:
            await self.timeout(author, admin_channel)
            pass

        it = 1
        while True:
            ###############################################################
            #Reactions
            ###############################################################
            #reaction name
            message = await admin_channel.send(f"name your {it} choice:")
            try:
                msg = await self.bot.wait_for("message",timeout= 120.0, check=checkm)
            except asyncio.TimeoutError:
                await self.timeout(author, admin_channel)
                break


            while True:
                #reaction logo
                await admin_channel.send(f"please react to this message:")
                def checkr(reaction, user):
                    return user.id == author
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=120.0, check= checkr)
                except asyncio.TimeoutError:
                    await self.timeout(author, admin_channel)
                    break
                if str(type(reaction.emoji)) == "<class 'str'>":
                    break
                elif type(reaction.emoji) == discord.Emoji:
                    if reaction.emoji.is_usable():
                        break
                await admin_channel.send("❌ sorry, this emoji is curently not supported please use a another !")
                
            

            #continue
            message = await admin_channel.send("ok ! do you want to add another choice ?")
            await message.add_reaction("✅")
            await message.add_reaction("❌")
            def checke(reaction, user):
                return (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌") and user.id == author
            try:
                ereaction, user = await self.bot.wait_for("reaction_add", timeout=120.0, check= checke)
            except asyncio.TimeoutError:
                await self.timeout(author, admin_channel)
                break

            #category name | emoji
            cdata[msg.content] = reaction.emoji
            it = it + 1

            if str(ereaction) == "❌":
                break

        embed = discord.Embed(
            title= title.content,
            description= f"end date: {end.content}"
        )

        content = ""
        votesdict = {}
        for d in cdata:
            votesdict[cdata[d]] = []
            content = f"{content} \n {cdata[d]} - {d}"

        embed.add_field(name= "Reactions:", value=content)
        embed_message = await ctx.send(embed= embed)
        voteid = embed_message.id

        for d in cdata:
            await embed_message.add_reaction(cdata.get(d))

        clearadminchannel = await admin_channel.clone()
        await admin_channel.delete()

        embed = discord.Embed(
            title= title.content + " controll channel",
            description= f"vote end: {end.content}"
        )
        for d in cdata:
            embed.add_field(name="reaction", value="\nDelete vote: 🗑\n Pie graph: 📀\nBar graph: 📊")

        controllmessage = await clearadminchannel.send(embed= embed)
        await controllmessage.add_reaction("🗑")
        await controllmessage.add_reaction("📀")
        await controllmessage.add_reaction("📊")
        await asyncio.sleep(5)
        createVote(str(ctx.guild.id), voteid, str(ctx.channel.id), str(controllmessage.id), str(clearadminchannel.id), votesdict)


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Votes(bot))
