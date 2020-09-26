import discord
import logging
from discord.ext import commands

bot = discord.Client()

invites = {}

# this specifies what extensions to load when the bot starts up
startup_extensions = ["core.event.invitation_manager", "core.command.giveaway", "core.command.server_status",
                      "core.command.player_stats", "core.event.command_error_handler", "core.command.link_channel",
                      "core.command.invitation", "core.command.clear"]

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

    token = "NzQwNTg3MjYyMzY1OTI1NDE3.XyrLog.H3J6BO934a64bzspWypTYV5cFaY"
    bot.run(token)