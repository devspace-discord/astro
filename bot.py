import os
import dotenv
import asyncio
import asyncpg
import discord
from discord.ext import commands

# loads environment variables
dotenv.load_dotenv()
TOKEN = os.getenv("token")
DB_HOST = os.getenv('DB_HOST')
DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DISBOTS_AUTH = os.getenv('disbots_auth')

bot = commands.Bot(
    command_prefix=["!", "!!", "-", "/", ">"],
    case_insensitive=True
)

async def database_setup():
    """Creates the database connection"""

    bot.db = await asyncpg.create_pool(
        host=DB_HOST,
        database=DATABASE,
        user=DB_USER,
        password=DB_PASSWORD,
        command_timeout=5
    )
asyncio.get_event_loop().run_until_complete(database_setup())

bot.cog_list = [
    "cogs.core.database",
    "cogs.core.staff",
    "cogs.commands.tags"
]
for cog in bot.cog_list:
    bot.load_extension(cog)

bot.run(TOKEN)
