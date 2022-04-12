import discord
from discord.ext import commands
from datetime import datetime


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        log_channel = self.client.get_channel(867861928624783370)
        if "Edgar" in member.name:
            embed = discord.Embed(
                title="Prohibited Term", description="That name is not allowed!"
            )
            await log_channel.send(content={member.mention}, embed=embed)

    # Message Edit
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        self.log_channel = self.client.get_channel(779338353895800872)
        if not after.author.bot:
            if before.content != after.content:
                embed = discord.Embed(
                    title="Message Edited",
                    color=0xCB4335,
                    description=f"Edited by {after.author.mention} in {after.channel.mention}",
                    timestamp=datetime.utcnow(),
                )

                name = after.author
                embed.set_author(name=name, icon_url=after.author.avatar_url)

                fields = [
                    ("Before", before.content, False),
                    ("After", after.content, False),
                ]

                for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

                await self.log_channel.send(embed=embed)

    # Message Delete
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.log_channel = self.client.get_channel(779338353895800872)
        if not message.author.bot:
            embed = discord.Embed(
                title="Message Deletion",
                color=0xCB4335,
                description=f"Deleted by {message.author.mention} in {message.channel.mention}",
                timestamp=datetime.utcnow(),
            )
            name = message.author
            embed.set_author(name=name, icon_url=message.author.avatar_url)
            # embed.set_image(url=str(message.attachments.url))
            fields = [("Content", message.content, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

    # User Update
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        self.log_channel = self.client.get_channel(779338353895800872)
        if before.name != after.name:
            embed = discord.Embed(
                title="Username Change",
                color=0xCB4335,
                description=f"Action by {after.mention}.",
                timestamp=datetime.utcnow(),
            )

            name = after.name
            embed.set_author(name=name, icon_url=f"{after.avatar_url}")

            fields = [("Before", before.name, False), ("After", after.name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        if before.discriminator != after.discriminator:
            embed = discord.Embed(
                title="Discriminator change",
                color=0xCB4335,
                description=f"Action by {after.mention}.",
                timestamp=datetime.utcnow(),
            )

            name = after.name
            embed.set_author(name=name, icon_url=f"{after.avatar_url}")

            fields = [
                ("Before", before.discriminator, False),
                ("After", after.discriminator, False),
            ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        if before.avatar_url != after.avatar_url:
            embed = discord.Embed(
                title="Avatar change",
                color=0xCB4335,
                description="New image is below, old to the right.",
                timestamp=datetime.utcnow(),
            )

            name = after.name
            embed.set_author(name=name, icon_url=f"{after.avatar_url}")

            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)

            await self.log_channel.send(embed=embed)

    # Member Update
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        self.log_channel = self.client.get_channel(779338353895800872)
        if before.display_name != after.display_name:
            embed = discord.Embed(
                title="Nickname Modified",
                color=0xCB4335,
                description=f"Action by {after.mention}",
                timestamp=datetime.utcnow(),
            )

            name = after.name
            embed.set_author(name=name, icon_url=f"{after.avatar_url}")

            fields = [
                ("Before", before.display_name, False),
                ("After", after.display_name, False),
            ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)

        elif before.roles != after.roles:
            embed = discord.Embed(
                title="Roles Updated",
                description=f"Roles were updated for {after.mention}",
                color=0xCB4335,
                timestamp=datetime.utcnow(),
            )

            name = after.name
            embed.set_author(name=name, icon_url=f"{after.avatar_url}")

            fields = [
                ("Before", ", ".join([r.mention for r in before.roles]), False),
                ("After", ", ".join([r.mention for r in after.roles]), False),
            ]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            await self.log_channel.send(embed=embed)


def setup(client):
    client.add_cog(Log(client))
