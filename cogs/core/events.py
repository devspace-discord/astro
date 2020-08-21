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

        self.bot.guild = self.bot.get_guild(self.bot.config["guild_id"])
        self.bot.suggestions_channel = self.bot.guild.get_channel(self.bot.config["suggestions_channel_id"])
        self.bot.pinboard_channel = self.bot.guild.get_channel(self.bot.config["pinboard_channel_id"])
        self.bot.error_channel = self.bot.guild.get_channel(self.bot.config["error_channel_id"])

        await self.database.update_staff()
        print(f"\n\n            ONLINE\n\n")


def setup(bot):
    bot.add_cog(Events(bot))
