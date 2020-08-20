import asyncpg
import discord
from ..exceptions import *
from discord.ext import commands


class Database(commands.Cog):

    def __init__(self, bot):
        """Initialized the Database cog"""

        self.bot = bot
        self.db = self.bot.db

    async def add_staff(self, user_id):
        """Adds a member to the staff list"""

        if user_id in self.bot.staff_list:
            raise MemberAlreadyStaff()

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO staff VALUES ($1)",
                user_id
            )

        await self.update_staff()

    async def update_staff(self):
        """Updates the cached staff list"""

        staff = await self.db.fetch(
            "SELECT user_id FROM staff"
        )

        self.bot.staff_list = list([int(member["user_id"]) for member in staff])

    async def remove_staff(self, user_id):
        """Removes a member from the staff list"""

        if user_id not in self.bot.staff_list:
            raise InvalidStaff()

        async with self.db.acquire() as conn:
            await conn.execute(
                "DELETE FROM staff WHERE user_id = $1",
                user_id
            )

        await self.update_staff()

    async def add_tag(self, tag, content, author):
        """Adds a tag to the database"""

        existingTag = await self.get_tag(tag)
        if existingTag:
            raise TagAlreadyExists()

        async with self.db.acquire() as conn:
            await conn.execute(
                "INSERT INTO tags (tag, content, author) VALUES ($1, $2, $3)",
                tag, content, author
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
            raise InvalidTag()

        async with self.db.acquire() as conn:
            await conn.execute(
                "DELETE FROM tags WHERE tag = $1",
                tag
            )

    async def edit_tag(self, tag, content):
        """Edits a custom tag in the database"""

        existingTag = await self.get_tag(tag)
        if not tag:
            raise InvalidTag()

        async with self.db.acquire() as conn:
            await conn.execute(
                "UPDATE tags SET content = $1 WHERE tag = $2",
                content, tag
            )


def setup(bot):
    bot.add_cog(Database(bot))
