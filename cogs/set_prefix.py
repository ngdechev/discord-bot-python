import discord
from discord.ext import commands
import os
import asyncpg

class SetPrefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} is ready!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(self, message, *, new_prefix: str):
        try:
            old_prefix_fetch = await self.client.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)
            old_prefix = old_prefix_fetch[0].get("prefix")
            await self.client.db.execute('UPDATE guilds SET prefix = $1 WHERE guild_id = $2', new_prefix, message.guild.id)
            
            new_prefix_embed = discord.Embed(colour=discord.Color.random())
            new_prefix_embed.set_author(name=f"{self.client.user.display_name} || New Server Prefix", icon_url=f"{self.client.user.display_avatar}")
            new_prefix_embed.add_field(name="Old Server Prefix", value=f"**{old_prefix}**", inline=False)
            new_prefix_embed.add_field(name="New Server Prefix", value=f"**{new_prefix}**", inline=False)
            new_prefix_embed.set_thumbnail(url=f"{message.guild.icon.url}")

            await message.send(embed=new_prefix_embed)                

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
        
    @setprefix.error
    async def setprefix_error(self, message, error):
        get_guild_prefix = await self.client.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)
        prefix = get_guild_prefix[0].get("prefix")

        if isinstance(error, commands.MissingRequiredArgument):
            await message.send(f"Missing required arguments. **Usage: {prefix}setprefix <new prefix>**")

        if isinstance(error, commands.MissingPermissions):
            await message.send("You don't have permissions to use this command!")

        if isinstance(error, commands.BotMissingPermissions):
            await message.send("I don't have permissions! Please check my role and add the required permissions!")
            
async def setup(client):
    await client.add_cog(SetPrefix(client))
