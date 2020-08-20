import discord
from discord.ext import commands


class Staff(commands.Cog):

    def __init__(self, bot):
        """Initialized the Staff cog"""
        self.bot = bot
        self.database = self.bot.get_cog("Database")

    @commands.command()
    @commands.is_owner()
    async def add_staff(self, ctx, user: discord.User):
        """Adds a user as to the staff member list"""

        await self.database.add_staff(user.id)
        await ctx.send(f"{self.bot.emoji["yes"]} Successfully added ``{user.name+'#'+user.discriminator}`` to the staff member list!")


def setup(bot):
    bot.add_cog(Staff(bot))
