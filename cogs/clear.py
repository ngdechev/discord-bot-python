import discord
from discord.ext import commands
import os


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} is ready!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, message, message_count: int):
        await message.channel.purge(limit=message_count)
        await message.send(f"{message_count} message's have been deleted!")


async def setup(client):
    await client.add_cog(Clear(client))
