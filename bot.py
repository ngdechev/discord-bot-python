import os
import asyncio

import discord
from discord.ext import commands, tasks

from itertools import cycle

from dotenv import load_dotenv
from pathlib import Path

# Protect the bot token with .env file
dotenv_path = Path('assets/.env')
load_dotenv(dotenv_path=dotenv_path)

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Bot status variable
bot_status = cycle(["Developing using Python!", "Currently under developing!"])


# Changing the bot status every 10 seconds
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    print("Bot is ready!")
    change_status.start()

# Cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with client:
        await load()
        await client.start(os.getenv('BOT_TOKEN'))


asyncio.run(main())
