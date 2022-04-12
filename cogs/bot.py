import discord, asyncio, json
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext

# from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import (
    create_button,
    create_actionrow,
    create_select,
    create_select_option,
)
from discord_slash.model import ButtonStyle
from discord_components import *


client = commands.Bot(command_prefix=">")
slash = SlashCommand(client, sync_commands=True)


class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    DiscordComponents(client)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Ping",
            description=f"Pong! `{round(self.client.latency * 1000)}ms`",
            # color = 0x5865F2
        )
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(
        name="ping",
        description="Displays message containing bot latency",
    )
    async def slash_bing(self, ctx: SlashContext):
        embed = discord.Embed(
            title="Ping",
            description=f"Pong! `{round(self.client.latency * 1000)}ms`",
            # color = 0x5865F2
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title="Invite",
            description="Invite PyGoose Pre-Alpha to your Discord Server!",
        )
        await ctx.send(
            embed=embed,
            components=[
                Button(
                    style=ButtonStyle.URL,
                    label="Invite Now",
                    url="https://discord.com/api/oauth2/authorize?client_id=861341470904942622&permissions=8&scope=bot%20applications.commands",
                )
            ],
        )

    @cog_ext.cog_slash(
        name="invite", description="Invite PyGoose Pre-Alpha to your Discord Server"
    )
    async def slash_invite(self, ctx):
        embed = discord.Embed(
            title="Invite",
            description="Invite PyGoose Pre-Alpha to your Discord Server!",
        )
        await ctx.send(
            embed=embed,
            components=[
                create_actionrow(
                    create_button(
                        style=ButtonStyle.URL,
                        label="Invite Now",
                        url="https://discord.com/api/oauth2/authorize?client_id=861341470904942622&permissions=8&scope=bot%20applications.commands",
                    )
                )
            ],
        )


def setup(client):
    client.add_cog(Bot(client))
