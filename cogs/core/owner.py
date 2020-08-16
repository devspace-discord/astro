import discord
from discord.ext import commands


class Staff(commands.Cog):

    def __init__(self, bot):
        """Initialized the Staff cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(Staff(bot))
