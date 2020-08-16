import discord
from discord.ext import commands


class Tags(commands.Cog):

    def __init__(self, bot):
        """Initialized the Tags cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(Tags(bot))
