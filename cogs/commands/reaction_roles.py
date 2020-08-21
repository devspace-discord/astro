import discord
from discord.ext import commands


class ReactionRoles(commands.Cog):

    def __init__(self, bot):
        """Initialized the ReactionRoles cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(ReactionRoles(bot))
