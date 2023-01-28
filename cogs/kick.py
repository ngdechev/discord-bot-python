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

            kick_embed = discord.Embed(colour=discord.Color.orange())
            kick_embed.set_author(name=f"{self.client.user.display_name} || Member Kick", icon_url=f"{self.client.user.display_avatar}")
            kick_embed.add_field(name="Kicked User", value=f"{member.name}")
            kick_embed.add_field(name="ID", value=f"{member.id}", inline=False)
            kick_embed.add_field(name="Kicked By", value=f"{message.author.mention}")
            kick_embed.add_field(name="Reason", value=f"{reason}")
            kick_embed.set_thumbnail(url=f"{member.display_avatar}")

            await message.send(embed=kick_embed)

        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise


async def setup(client):
    await client.add_cog(Kick(client))
