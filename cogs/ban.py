import discord
from discord.ext import commands
import os

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{os.path.basename(__file__)} is ready!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, message, member: discord.Member, *, reason="No reason provided"):
        try:
            channel = discord.utils.get(message.guild.channels, name="kick-ban")

            await member.ban(reason=reason)

            ban_embed = discord.Embed(colour=discord.Color.red())
            ban_embed.set_author(name=f"{self.client.user.display_name} || Member Ban", icon_url=f"{self.client.user.display_avatar}")
            ban_embed.add_field(name="Banned User", value=f"{member.name}")
            ban_embed.add_field(name="ID", value=f"{member.id}", inline=False)
            ban_embed.add_field(name="Banned By", value=f"{message.author.mention}")
            ban_embed.add_field(name="Reason", value=f"{reason}")
            ban_embed.set_thumbnail(url=f"{member.display_avatar}")

            await channel.send(embed=ban_embed)
                
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            await message.channel.send(f"{member.name} is not in the server!")
            raise

async def setup(client):
    await client.add_cog(Ban(client))
