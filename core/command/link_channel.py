import asyncio
import json
from core.util.permission import is_admin
from discord.ext import commands


class LinkChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = {}

    @commands.command(name="link")
    @commands.check(is_admin)
    async def link(self, ctx, feature_name):
        """
        :param ctx:
        :param feature_name:
        :return:
        """
        for command in self.bot.commands:
            if str(command) == str(feature_name):
                # Data to be written
                self.channel_id[feature_name] = ctx.channel.id

                # Opening JSON file
                with open('core/data/channel_id.json', 'r') as openfile:
                    # Serializing json + Reading from json file
                    registered_channel = json.load(openfile)

                for key in self.channel_id:
                    if key in registered_channel:
                        registered_channel.pop(key)

                self.channel_id.update(registered_channel)

                with open('core/data/channel_id.json', 'w') as outfile:
                    json.dump(self.channel_id, outfile)
                self.channel_id.clear()
                notice_link = await ctx.send("Link effectué !")
                await asyncio.sleep(5)
                await notice_link.delete()


def setup(bot):
    """
    Setup cog to be able to listen events & commands inside this class
    Without this class, the module link_channel.py cannot be load
    """
    bot.add_cog(LinkChannel(bot))