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

    @clear.error
    async def clear_error(self, message, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await message.send("Missing required arguments. **Usage: !clear <number of messages to clear>**")
        
        if isinstance(error, commands.MissingPermissions):
            await message.send("You don't have permissions to use this command!")
        
        if isinstance(error, commands.BotMissingPermissions):
            await message.send("I don't have permissions! Please check my role and add the required permissions!")

async def setup(client):
    await client.add_cog(Clear(client))
