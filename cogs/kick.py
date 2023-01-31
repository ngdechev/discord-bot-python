import discord
from discord.ext import commands
import os


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} is ready!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, message, member: discord.Member, *, reason="No reason provided"):
        try:
            await member.kick(reason=reason)
            
            channel = discord.utils.get(message.guild.channels, name="kick-ban")

            kick_embed = discord.Embed(colour=discord.Color.orange())
            kick_embed.set_author(name=f"{self.client.user.display_name} || Member Kick", icon_url=f"{self.client.user.display_avatar}")
            kick_embed.add_field(name="Kicked User", value=f"{member.name}")
            kick_embed.add_field(name="ID", value=f"{member.id}", inline=False)
            kick_embed.add_field(name="Kicked By", value=f"{message.author.mention}")
            kick_embed.add_field(name="Reason", value=f"{reason}")
            kick_embed.set_thumbnail(url=f"{member.display_avatar}")

            await channel.send(embed=kick_embed)

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    @kick.error
    async def kick_error(self, message, error):
        get_guild_prefix = await self.client.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)
        prefix = get_guild_prefix[0].get("prefix")

        if isinstance(error, commands.MissingRequiredArgument):
            await message.send(f"Missing required arguments. **Usage: {prefix}kick @user <reason>**")

        if isinstance(error, commands.MissingPermissions):
            await message.send("You don't have permissions to use this command!")

        if isinstance(error, commands.BotMissingPermissions):
            await message.send("I don't have permissions! Please check my role and add the required permissions!")
            
async def setup(client):
    await client.add_cog(Kick(client))
