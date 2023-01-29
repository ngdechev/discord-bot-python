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


async def setup(client):
    await client.add_cog(Unban(client))
