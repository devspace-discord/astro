import discord
from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, bot):
        """Initialized the Database cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(Database(bot))
