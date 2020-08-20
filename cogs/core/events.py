import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, bot):
        """Initializes the Events cog"""

        self.bot = bot
        self.database = self.bot.get_cog("Database")

    @commands.Cog.listener()
    async def on_ready(self):
        """Triggered when the bot is ready and it's cache is loaded"""

        await self.database.update_staff()


def setup(bot):
    bot.add_cog(Events(bot))
