import json

from discord.ext import commands
from main import invites
from core.util.channel_id import get_channel_id_by_feature_name


class Invitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.members_invites_counter = {}

    def find_invite_by_code(self, invite_list, code):
        """Invitations are identified by a code, it's the same code visible in a link discord.gg/<code>"""

        # Simply looping through each invite in an
        # invite list which we will get using guild.invites()

        for inv in invite_list:

            # Check if the invite code in this element
            # of the list is the one we're looking for

            if inv.code == code:
                # If it is, we return it.

                return inv

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """When a member join Discord"""

        channel = member.guild.get_channel(await get_channel_id_by_feature_name("invitation"))

        if channel is None:
            return

        member_name = member.display_name
        invites_before_join = invites[member.guild.id]
        invites_after_join = await member.guild.invites()
        members_counter = member.guild.member_count

        with open("core/data/inviter_counter.json", mode='r') as file:
            self.members_invites_counter = dict(json.load(file))

        for invite in invites_before_join:
            # When a new invitation is used (clicked), then the condition is true
            if invite.uses < self.find_invite_by_code(invites_after_join, invite.code).uses:
                inviter_name = invite.inviter.name
                self.members_invites_counter[inviter_name] = 1 if inviter_name not in self.members_invites_counter else self.members_invites_counter.get(inviter_name) + 1
                await channel.send("Hello " + member_name + f" (Members: {members_counter}) (Invited by: {invite.inviter.name}) (Invitations: {self.members_invites_counter.get(inviter_name)})")

                with open("core/data/inviter_counter.json", mode='w') as file:
                    json.dump(self.members_invites_counter, file)

                invites[member.guild.id] = invites_after_join
                return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """When a member leave or gets banned/kicked"""

        channel = member.guild.get_channel(await get_channel_id_by_feature_name("invitation"))

        if channel is None:
            return

        member_name = member.display_name
        invites[member.guild.id] = await member.guild.invites()
        await channel.send("Bye " + member_name + " (Members: " + str(member.guild.member_count) + ")")


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Invitation(bot))