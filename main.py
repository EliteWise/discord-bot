import discord


class Main(discord.Client):

    async def on_ready(self):
        print("Bot Ready!")


client = Main()
token = ""
client.run(token)