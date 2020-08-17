import asyncpg
import discord
from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, bot):
        """Initialized the Database cog"""

        self.bot = bot
        self.db = self.bot.db

    async def add_staff(self, user_id):
        """Adds a member to the staff list"""

        if user_id in self.bot.staff_list:
            return

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO staff VALUES ($1)",
                user_id
            )

    async def update_staff(self):
        """Updates the cached staff list"""

        staff = self.db.fetchrow("SELECT * FROM staff")

        self.bot.staff_list = list(staff)

    async def remove_staff(self, user_id):
        """Removes a member from the staff list"""

        if user_id not in self.bot.staff_list:
            return

        async with self.db.acquire() as conn:
            await conn.execute(
                "DELETE FROM staff WHERE user_id = $1",
                user_id
            )

    async def add_tag(self, tag, author):
        """Adds a tag to the database"""

        existingTag = await self.get_tag(tag)
        if existingTag:
            return

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO tags (tag, author) VALUES ($1, $2)",
                tag, author
            )

    async def get_tag(self, tag):
        """Gets a tag from the database"""

        tag = await self.db.fetchrow(
            "SELECT * FROM tags WHERE tag = $1",
            tag
        )
        return tag

    async def remove_tag(self, tag):
        """Removes a tag from the database"""

        existingTag = await self.get_tag(tag)
        if not tag:
            return

        async with self.db.acquire() as conn:
            await conn.execute(
                "DELETE FROM tags WHERE tag = $1",
                tag
            )


def setup(bot):
    bot.add_cog(Database(bot))
