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


def setup(bot):
    bot.add_cog(ReactionRoles(bot))
