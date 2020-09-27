import discord
import logging
from discord.ext import commands

bot = discord.Client()

invites = {}

# this specifies what extensions to load when the bot starts up
startup_extensions = ["core.command.stackvoice", "core.command.votes", "core.event.Voicechanel_stack_events", 
"core.event.votes_event"]

bot = commands.Bot(command_prefix='!')

# Initialize logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] {%(module)s} - %(funcName)s: %(message)s",
    handlers=[
        logging.FileHandler("log/debug.log"),
        logging.StreamHandler()
    ]
)

log = logging.getLogger("main")


@bot.event
async def on_ready():
    log.info("Bot Ready!")

    # Getting all the guilds our bot is in
    for guild in bot.guilds:
        # Adding each guild's invites to our dict
        invites[guild.id] = await guild.invites()


if __name__ == "__main__":
    # Load all extensions inside command and event packages
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            log.info('Extension: ' + extension + ' loaded!')
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            log.error('Failed to load extension {}\n{}'.format(extension, exc))

    token = "NzM1Nzk2ODQ3NTkwODk5NzQy.XxleNg.Y3YlEdVp7R2x_Guf81TbuFpEeBo"
    bot.run(token)
