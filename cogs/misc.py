import discord
import datetime
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import (
    create_button,
    create_actionrow,
    create_select,
    create_select_option,
)
from discord_slash.model import ButtonStyle
from discord_components import *


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def goose(self, ctx):
        author = ctx.message.author
        embed = discord.Embed(
            title="PyGoose",
            description="This is the avatar of Goose Dictator",
            # color = 0xff0000
        )
        embed.set_footer(text="This is a footer.")
        embed.set_image(
            url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
        )
        embed.set_author(name="PyGoose", icon_url=author.avatar_url)
        embed.add_field(name="Field Name", value="Field Value", inline=False)
        embed.add_field(name="Field Name", value="Field Value", inline=True)
        embed.add_field(name="Field Name", value="Field Value", inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, *, member: commands.MemberConverter = None):
        embed = discord.Embed(title="Avatar")
        if member is None:
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_image(url=ctx.author.avatar_url)
        else:
            embed.set_author(name=member, icon_url=member.avatar_url)
            embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    buttons = [
        [
            Button(style=ButtonStyle.grey, label="1"),
            Button(style=ButtonStyle.grey, label="2"),
            Button(style=ButtonStyle.grey, label="3"),
            Button(style=ButtonStyle.blue, label="×"),
            Button(style=ButtonStyle.red, label="Exit"),
        ],
        [
            Button(style=ButtonStyle.grey, label="4"),
            Button(style=ButtonStyle.grey, label="5"),
            Button(style=ButtonStyle.grey, label="6"),
            Button(style=ButtonStyle.blue, label="÷"),
            Button(style=ButtonStyle.red, label="←"),
        ],
        [
            Button(style=ButtonStyle.grey, label="7"),
            Button(style=ButtonStyle.grey, label="8"),
            Button(style=ButtonStyle.grey, label="9"),
            Button(style=ButtonStyle.blue, label="+"),
            Button(style=ButtonStyle.red, label="Clear"),
        ],
        [
            Button(style=ButtonStyle.blue, label="^"),
            Button(style=ButtonStyle.grey, label="0"),
            Button(style=ButtonStyle.grey, label="."),
            Button(style=ButtonStyle.blue, label="-"),
            Button(style=ButtonStyle.green, label="="),
        ],
    ]

    def calculate(self, exp):
        o = exp.replace("×", "*")
        o = o.replace("÷", "/")
        o = o.replace("^", "**")
        result = ""
        try:
            result = str(eval(o))
        except:
            result = "```[An error occurred]```"
        return result

    @commands.command()
    async def calculator(self, ctx):
        author = ctx.author
        m = await ctx.send(content="Loading calculator...")
        expression = "```[0]```"
        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        e = discord.Embed(
            title=f"Calculator.exe running...‏‏‎‏‏‎‏ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ",  # User: {ctx.author.name} ID: {ctx.author.id}
            description=expression,
            timestamp=delta,
        )
        e.set_author(name=author, icon_url=author.avatar_url)
        await m.edit(content="Opened calculator.exe", components=self.buttons, embed=e)
        while m.created_at < delta:
            res = await self.client.wait_for("button_click")
            if res.message.embeds[0].timestamp < delta:
                expression = res.message.embeds[0].description
                if (
                    expression == "```[0]```"
                    or expression == "```[An error occurred]```"
                ):
                    expression = ""
                if res.component.label == "Exit":
                    await res.respond(content="Calculator closed.", type=7)
                    break
                elif res.component.label == "←":
                    expression = expression[:-1]
                elif res.component.label == "Clear":
                    expression = "```[0]```"
                elif res.component.label == "=":
                    expression = self.calculate(expression)
                else:
                    expression += res.component.label
                f = discord.Embed(
                    title=f"Calculator.exe running...‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎  ‎‏‏‎ ‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‏‏‎‏‏‎",  # User: {ctx.author.name} ID: {ctx.author.id}
                    description=expression,
                    timestamp=delta,
                )
                f.set_author(name=author, icon_url=author.avatar_url)
                await res.respond(
                    content="Calculator.exe", embed=f, components=self.buttons, type=7
                )


def setup(client):
    client.add_cog(Misc(client))
