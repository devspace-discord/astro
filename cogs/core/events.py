import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot):
        """Initializes the Events cog"""

        self.bot = bot


def setup(bot):
    bot.add_cog(Events(bot))
