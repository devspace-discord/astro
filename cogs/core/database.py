import asyncpg
import discord
from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, bot):
        """Initialized the Database cog"""

        self.bot = bot

    async def add_tag(self, tag, author):
        """Adds a tag to the database"""

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO tags (tag, author) VALUES ($1, $2)",
                tag, author
            )


def setup(bot):
    bot.add_cog(Database(bot))