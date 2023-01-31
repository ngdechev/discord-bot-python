import discord
from discord.ext import commands
import os


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} is ready!")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, message, member_id):
        try:
            user = discord.Object(id=member_id)
            channel = discord.utils.get(message.guild.channels, name="kick-ban")
            member = await self.client.fetch_user(member_id)

            await message.guild.unban(user)
            unban_embed = discord.Embed(colour=discord.Color.green())
            unban_embed.set_author(name=f"{self.client.user.display_name} || Member Unban",
                                 icon_url=f"{self.client.user.display_avatar}")
            unban_embed.add_field(name="Unbanned User", value=f"<@{member_id}>")
            unban_embed.add_field(name="Unbanned By", value=f"{message.author.mention}")
            unban_embed.set_thumbnail(url=f"{member.display_avatar}")

            await channel.send(embed=unban_embed)                

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            await message.channel.send("No user found!")
            raise
    
    @unban.error
    async def unban_error(self, message, error):
        get_guild_prefix = await self.client.db.fetch('SELECT prefix FROM guilds WHERE guild_id = $1', message.guild.id)
        prefix = get_guild_prefix[0].get("prefix")

        if isinstance(error, commands.MissingRequiredArgument):
            await message.send(f"Missing required arguments. **Usage: {prefix}unban <user id>**")

        if isinstance(error, commands.MissingPermissions):
            await message.send("You don't have permissions to use this command!")

        if isinstance(error, commands.BotMissingPermissions):
            await message.send("I don't have permissions! Please check my role and add the required permissions!")

async def setup(client):
    await client.add_cog(Unban(client))
