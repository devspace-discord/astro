import discord
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, bot):
        """Initialized the Errors cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(Errors(bot))
