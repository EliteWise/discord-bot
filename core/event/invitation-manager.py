from discord.ext import commands
from main import invites

members_invites_counter = {}


class Invitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def find_invite_by_code(self, invite_list, code):
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
        channel = member.guild.get_channel(719257870822277174)
        member_name = member.display_name
        print("Welcome ", member_name, " !")
        invites_before_join = invites[member.guild.id]
        invites_after_join = await member.guild.invites()
        members_counter = member.guild.member_count
        for invite in invites_before_join:
            if invite.uses < self.find_invite_by_code(invites_after_join, invite.code).uses:
                inviter_name = invite.inviter.name
                members_invites_counter[inviter_name] = 1 if inviter_name not in members_invites_counter else members_invites_counter.get(inviter_name) + 1
                await channel.send("Hello " + member_name + f" (Members: {members_counter}) (Invited by: {invite.inviter.name}) (Invitations: {members_invites_counter.get(inviter_name)})")

                invites[member.guild.id] = invites_after_join
                return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """When a member leave or gets banned/kicked"""
        channel = member.guild.get_channel(719257870822277174)
        member_name = member.display_name
        print("Bye! See you next time ", member_name)
        invites[member.guild.id] = await member.guild.invites()
        await channel.send("Bye " + member_name + " (Members: " + str(member.guild.member_count) + ")")


def setup(bot):
    """Setup cog to be able to listen events & commands inside this class"""
    bot.add_cog(Invitation(bot))