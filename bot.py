import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

from pathlib import Path

dotenv_path = Path('assets/.env')
load_dotenv(dotenv_path=dotenv_path)

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")

client.run(os.getenv('BOT_TOKEN'))