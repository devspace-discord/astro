import discord
from ..util import *
from discord.ext import commands


class Tags(commands.Cog):

    def __init__(self, bot):
        """Initialized the Tags cog"""

        self.bot = bot
        self.database = self.bot.get_cog("Database")

    @commands.command(aliases=["create_tag"])
    @commands.check(staff_check)
    async def make_tag(self, ctx, tag, *, content):
        """Adds a custom tag to the database"""

        await self.database.add_tag(tag.lower(), content, ctx.author.id)
        await ctx.send(f"Successfully created the ``{tag}`` tag!")


def setup(bot):
    bot.add_cog(Tags(bot))
