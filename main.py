import discord
from discord.ext import commands

bot = discord.Client()

invites = {}

# this specifies what extensions to load when the bot starts up
startup_extensions = ["core.event.invitation-manager"]

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print("Bot Ready!")

    # Getting all the guilds our bot is in
    for guild in bot.guilds:
        # Adding each guild's invites to our dict
        invites[guild.id] = await guild.invites()


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Extensions: ' + extension + ' loaded!')
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    token = "NzQwNTg3MjYyMzY1OTI1NDE3.XyrLog.H3J6BO934a64bzspWypTYV5cFaY"
    bot.run(token)
