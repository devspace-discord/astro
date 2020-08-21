import discord
from ..util import *
from discord.ext import commands


class ReactionRoles(commands.Cog):

    def __init__(self, bot):
        """Initialized the ReactionRoles cog"""

        self.bot = bot
        self.database = self.bot.get_cog("Database")

    @commands.command()
    @commands.check(staff_check)
    async def add_reaction_role(self, ctx, message_id: int, emoji: str, role: discord.Role):
        """Registers a message with reaction role functionality"""

        await self.database.add_reaction_role(message_id, emoji, role.id)

        await ctx.send(f"{self.bot.emoji['yes']} Successfully added reaction roles for the mentioned message!")

    @commands.command()
    @commands.check(staff_check)
    async def remove_reaction_role(self, ctx, message_id: int, emoji: str):
        """Removes a message's reaction role functionality"""

        await self.database.remove_reaction_role(message_id, emoji)

        await ctx.send(f"{self.bot.emoji['yes']} Successfully removed reaction roles for the mentioned message!")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """Listens for reactions to give reaction roles"""

        if payload.user_id == self.bot.user.id:
            return

        member = self.bot.guild.get_member(payload.user_id)
        if not member:
            return

        if payload.emoji.is_custom_emoji() and payload.emoji.animated:
            emoji = f"<a:{payload.emoji.name}:{payload.emoji.id}>"
        elif payload.emoji.is_custom_emoji() and not payload.emoji.animated:
            emoji = f"<:{payload.emoji.name}:{payload.emoji.id}>"
        elif payload.emoji.is_unicode_emoji():
            emoji = payload.emoji.name
        else:
            return

        reaction_role = await self.database.get_reaction_role(payload.message_id, emoji)
        if not reaction_role:
            return

        role = self.bot.guild.get_role(reaction_role['role_id'])
        await member.add_roles(role, reason="Reaction Role")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        """Listens for removed reactions to remove reaction roles"""

        if payload.user_id == self.bot.user.id:
            return

        member = self.bot.guild.get_member(payload.user_id)
        if not member:
            return

        if payload.emoji.is_custom_emoji() and payload.emoji.animated:
            emoji = f"<a:{payload.emoji.name}:{payload.emoji.id}>"
        elif payload.emoji.is_custom_emoji() and not payload.emoji.animated:
            emoji = f"<:{payload.emoji.name}:{payload.emoji.id}>"
        elif payload.emoji.is_unicode_emoji():
            emoji = payload.emoji.name
        else:
            return

        reaction_role = await self.database.get_reaction_role(payload.message_id, emoji)
        if not reaction_role:
            return

        role = self.bot.guild.get_role(reaction_role['role_id'])
        await member.remove_roles(role, reason="Reaction Role")

def setup(bot):
    bot.add_cog(ReactionRoles(bot))
