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
        await ctx.send(f"{self.bot.emoji['yes']} Successfully created the tag - ``{tag}``")

    @commands.command()
    async def tag(self, ctx, *, tag):
        """Gets a custom tag from the database"""

        tag = await self.database.get_tag(tag.lower())
        if not tag:
            await ctx.send(f"{self.bot.emoji['no']} This tag does not exist.")
            return
        user = self.bot.get_user(tag['author'])

        await ctx.send(tag["content"])

    @commands.command(aliases=["remove_tag"])
    @commands.check(staff_check)
    async def delete_tag(self, ctx, *, tag):
        """Removes a custom tag from the database"""

        await self.database.remove_tag(tag.lower())
        await ctx.send(f"{self.bot.emoji['yes']} Successfully deleted the tag - ``{tag}``!")

    @commands.command()
    @commands.check(staff_check)
    async def edit_tag(self, ctx, tag, *, content):
        """Edits a tag in the database"""

        await self.database.edit_tag(tag, content)
        await ctx.send(f"{self.bot.emoji['yes']} Successfully edited the tag - ``{tag}``")


def setup(bot):
    bot.add_cog(Tags(bot))
