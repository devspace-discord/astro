import random
import discord
import traceback
from ..exceptions import *
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, bot):
        """Initialized the Errors cog"""

        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Error handling for all bot commands"""

        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            hours = error.retry_after // 3600
            minutes = (error.retry_after - (hours*3600)) // 60
            time = f"{str(hours)} hours and {str(minutes)} minutes"
            await ctx.send(message)
            await ctx.send(random.choice([
                f"You need to wait {time} to do that",
                f"Calm Down, wait {time}",
                f"Too fast for me, young child. Wait another {time}"
            ]))

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(random.choice([
                "You forgot something. Does that happen a lot?",
                "You're missing something, I don't have enough to work with",
                "Read what you just said and find the errors"
            ]))

        elif isinstance(error, commands.MissingPermissions) or isinstance(error, InsufficientPermissions):
            await ctx.send(random.choice([
                "You don't have enough power to do that",
                "You need to level up to do that",
                "You need someone stronger to do that for you"
            ]))

        try:
            if isinstance(error.original, TagAlreadyExists):
                await ctx.send(random.choice([
                    "Too late, this tag already exists",
                    "That tag name has already been used",
                    "You're a few million years late, someone already claimed that tag"
                ]))

            elif isinstance(error.original, InvalidTag):
                await ctx.send(random.choice([
                    "I can't find any tags with that name",
                    "There isn't any tag with that name",
                    "Typo alert :rotating_light: I can't find any tags with that name"
                ]))

            elif isinstance(error.original, MemberAlreadyStaff):
                await ctx.send(random.choice([
                    "It's really disappointing that you don't know who's in the staff team yourself",
                    "This user is already a staff member \:P",
                    "This user is already staff. Did we get hacked!?"
                ]))

            elif isinstance(error.original, InvalidStaff):
                await ctx.send(random.choice([
                    "It's really disappointing that you don't know who's in the staff team yourself",
                    "This user is not a staff member \:P",
                    "This user is not staff. Did we get hacked!?"
                ]))

            else:
                print(error)
                print(MemberAlreadyStaff)
                message = random.choice([
                    "Something went wrong \:P",
                    "I just broke, please tell someone"
                ])
                await ctx.send(message)

                etype = type(error)
                trace = error.__traceback__
                verbosity = 2
                lines = traceback.format_exception(etype, error, trace, verbosity)
                traceback_error = ''.join(lines)

                user_input = ctx.message.content

                embed = discord.Embed()

        except Exception as e:
            pass


def setup(bot):
    bot.add_cog(Errors(bot))
