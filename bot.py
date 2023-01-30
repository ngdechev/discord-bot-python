import os
import asyncio

import discord
from discord.ext import commands, tasks

from itertools import cycle

from dotenv import load_dotenv
from pathlib import Path

import asyncpg

# Protect the bot data with .env file
dotenv_path = Path('assets/.env')
load_dotenv(dotenv_path = dotenv_path)

# Set Prefix
async def get_prefix(client, message):
    if not message.guild:
        return commands.when_mentioned_or(os.getenv('DEFAULT_PREFIX'))(client, message)

    prefix = await client.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)

    if len(prefix) == 0:
        await client.db.execute('INSERT INTO guilds(guild_id, prefix) VALUES ($1, $2)', message.guild.id, os.getenv('DEFAULT_PREFIX'))
        prefix = os.getenv('DEFAULT_PREFIX')
    else:
        prefix = prefix[0].get("prefix")
    
    return commands.when_mentioned_or(prefix)(client, message)

async def create_db_pool():
    client.db = await asyncpg.create_pool(database = os.getenv('DB_NAME'), user = os.getenv('DB_USER'), password = os.getenv('DB_PASSWORD'))
    print(f"Connected to {os.getenv('DB_NAME')} database!")

client = commands.Bot(command_prefix = get_prefix, intents=discord.Intents.all())

# Bot status variable
bot_status = cycle(["Developing using Python!", "Currently under developing!"])

# Changing the bot status every 10 seconds
@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

# On Ready
@client.event
async def on_ready():
    print("Bot is ready!")
    change_status.start()

# Cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

# Main
async def main():
    async with client:
        await load()
        await create_db_pool()
        await client.start(os.getenv('BOT_TOKEN'))

asyncio.run(main())