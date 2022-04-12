import os
import aiohttp
import json
import asyncpraw
import random
import discord
import asyncio
from discord.ext import commands
from discordTogether import DiscordTogether
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import (
    create_button,
    create_actionrow,
    create_select,
    create_select_option,
)
from discord_components import *

client = commands.Bot(command_prefix=">")
slash = SlashCommand(client, sync_commands=True)

CAT_API_KEY = os.environ["CAT_API_KEY"]

reddit = asyncpraw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    username=os.environ["REDDIT_USERNAME"],
    password=os.environ["REDDIT_PASSWORD"],
    user_agent="PyGoose",
)


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.together_control = DiscordTogether(client)

    @commands.command()
    async def betrayal(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "betrayal"
            )
            embed = discord.Embed(
                title="Betrayal.io",
                description="Initiate Betrayal.io by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @cog_ext.cog_slash(
        name="betrayal",
        description="Play Betrayal.io with the new Discord Party Games feature",
    )
    async def slash_betrayal(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "betrayal"
            )
            embed = discord.Embed(
                title="Betrayal.io",
                description="Initiate Betrayal.io by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @commands.command()
    async def chess(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "chess"
            )
            embed = discord.Embed(
                title="Chess In The Park",
                description="Initiate Chess In The Park by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @cog_ext.cog_slash(
        name="chess",
        description="Play Chess In The Park with the new Discord Party Games feature",
    )
    async def slash_chess(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "chess"
            )
            embed = discord.Embed(
                title="Chess In The Park",
                description="Initiate Chess In The Park by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @commands.command()
    async def fishing(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "fishing"
            )
            embed = discord.Embed(
                title="Fishington.io",
                description="Initiate Fishington.io by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @cog_ext.cog_slash(
        name="fishing",
        description="Play Fishington.io with the new Discord Party Games feature",
    )
    async def slash_fishing(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "fishing"
            )
            embed = discord.Embed(
                title="Fishington.io",
                description="Initiate Fishington.io by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @commands.command()
    async def poker(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "poker"
            )
            embed = discord.Embed(
                title="Poker Night",
                description="Initiate Poker Night by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @cog_ext.cog_slash(
        name="poker",
        description="Play Poker Night with the new Discord Party Games feature",
    )
    async def slash_poker(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "poker"
            )
            embed = discord.Embed(
                title="Poker Night",
                description="Initiate Poker Night by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @commands.command()
    async def youtube(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "youtube"
            )
            embed = discord.Embed(
                title="YouTube Together",
                description="Initiate YouTube Together by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @cog_ext.cog_slash(
        name="youtube",
        description="Watch YouTube Together with the new Discord Party Games feature",
    )
    async def slash_youtube(self, ctx):
        if not ctx.author.voice:
            embed = discord.Embed(
                title="Voice Channel Error",
                description="Please connect to a voice channel!",
            )
            await ctx.send(embed=embed)
        else:
            link = await self.together_control.create_link(
                ctx.author.voice.channel.id, "youtube"
            )
            embed = discord.Embed(
                title="YouTube Together",
                description="Initiate YouTube Together by clicking the Discord invite link! Other users may join by clicking the `Play` or `Spectate` button.",
            )
            await ctx.send(embed=embed)
            await ctx.send(f"{link}")

    @commands.command()
    async def meme(self, ctx):
        subreddit = await reddit.subreddit("memes")

        all_subs = []

        hot = subreddit.hot(limit=100)
        new = subreddit.new(limit=50)

        async for submission in hot or new:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title=name, url=random_sub.url)

        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="meme", description="Sends memes from Reddit")
    async def slash_meme(self, ctx):
        subreddit = await reddit.subreddit("memes")

        all_subs = []

        hot = subreddit.hot(limit=100)

        async for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title=name)

        embed.set_image(url=url)

        await ctx.send(embed=embed)

    # Coin flip command
    @commands.command()
    async def flip(self, ctx):
        sides = ["Heads", "Tails"]
        embed = discord.Embed(title="Flip", description=f"{random.choice(sides)}!")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="flip", description="Flip a coin in Discord")
    async def slash_flip(self, ctx):
        sides = ["Heads", "Tails"]
        embed = discord.Embed(title="Flip", description=f"{random.choice(sides)}!")
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.thecatapi.com/v1/images/search") as r:
                data = await r.json()
                pairs = data.items()

                embed = discord.Embed(title="Cat")

                embed.set_image(url=json.loads(pairs)["url"])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                data = await r.json()

                embed = discord.Embed(title="Dog", url=data["message"])
                embed.set_image(url=data["message"])
        await ctx.send(embed=embed)

    # Rock paper scissors
    @commands.command()
    async def rps(self, ctx):
        rps_choices = ["Rock", "Paper", "Scissors"]
        rps_bot = random.choice(rps_choices)
        yet = discord.Embed(
            title=f"RPS",
            description="Click on the button options to continue the game!",
        )

        message = await ctx.send(
            embed=yet,
            components=[
                [
                    Button(style=4, label="Rock", emoji="🪨"),
                    Button(style=3, label="Paper", emoji="📄"),
                    Button(style=1, label="Scissors", emoji="✂️"),
                ]
            ],
        )

        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            res = await self.client.wait_for("button_click", check=check, timeout=15)
            player = res.component.label
            win = discord.Embed(
                title="RPS: You Won!",
                description=f"You won, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )
            lose = discord.Embed(
                title="RPS: You Lost!",
                description=f"You lost, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )
            tie = discord.Embed(
                title="RPS: You Tied!",
                description=f"You tied, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )

            if player == rps_bot:
                await message.edit(
                    embed=tie,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Rock" and rps_bot == "Paper":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Rock" and rps_bot == "Scissors":
                await message.edit(
                    embed=win,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Paper" and rps_bot == "Rock":
                await message.edit(
                    embed=win,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Paper" and rps_bot == "Scissors":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Scissors" and rps_bot == "Rock":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Scissors" and rps_bot == "Paper":
                await message.edit(
                    embed=win,
                    components=[
                        #     [
                        #         Button(
                        #             style=4,
                        #             label="Rock",
                        #             emoji="🪨",
                        #             disabled=True
                        #         ),
                        #         Button(
                        #             style=3,
                        #             label="Paper",
                        #             emoji="📄",
                        #             disabled=True
                        #         ),
                        #         Button(
                        #             style=1,
                        #             label="Scissors",
                        #             emoji="✂️",
                        #             disabled=True
                        #         )
                        #     ]
                    ],
                )

        except asyncio.TimeoutError:
            await message.edit(
                embed=yet,
                components=[
                    [
                        Button(style=4, emoji="🪨", disabled=True),
                        Button(style=3, emoji="📄", disabled=True),
                        Button(style=1, emoji="✂️", disabled=True),
                        Button(
                            style=2,
                            label="Session Terminated",
                            emoji=discord.PartialEmoji(
                                name="XWhite", id="873265936357011476"
                            ),
                            disabled=True,
                        ),
                    ]
                ],
            )

    @cog_ext.cog_slash(name="rps", description="Play Rock Paper Scissors with the bot")
    async def slash_rps(self, ctx):
        rps_choices = ["Rock", "Paper", "Scissors"]
        rps_bot = random.choice(rps_choices)
        yet = discord.Embed(
            title=f"RPS",
            description="Click on the button options to continue the game!",
        )

        message = await ctx.send(
            embed=yet,
            components=[
                create_actionrow(
                    create_button(style=4, label="Rock", emoji="🪨"),
                    create_button(style=3, label="Paper", emoji="📄"),
                    create_button(style=1, label="Scissors", emoji="✂️"),
                )
            ],
        )

        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel

        try:
            res = await self.client.wait_for("button_click", check=check, timeout=15)
            player = res.component.label
            win = discord.Embed(
                title="RPS: You Won!",
                description=f"You won, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )
            lose = discord.Embed(
                title="RPS: You Lost!",
                description=f"You lost, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )
            tie = discord.Embed(
                title="RPS: You Tied!",
                description=f"You tied, {ctx.author.mention}! PyGoose chose **{rps_bot}** and you chose **{player}**",
            )

            if player == rps_bot:
                await message.edit(
                    embed=tie,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Rock" and rps_bot == "Paper":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Rock" and rps_bot == "Scissors":
                await message.edit(
                    embed=win,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Paper" and rps_bot == "Rock":
                await message.edit(
                    embed=win,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Paper" and rps_bot == "Scissors":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Scissors" and rps_bot == "Rock":
                await message.edit(
                    embed=lose,
                    components=[
                        # [
                        #     Button(
                        #         style=4,
                        #         label="Rock",
                        #         emoji="🪨",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=3,
                        #         label="Paper",
                        #         emoji="📄",
                        #         disabled=True
                        #     ),
                        #     Button(
                        #         style=1,
                        #         label="Scissors",
                        #         emoji="✂️",
                        #         disabled=True
                        #     )
                        # ]
                    ],
                )

            if player == "Scissors" and rps_bot == "Paper":
                await message.edit(
                    embed=win,
                    components=[
                        #     [
                        #         Button(
                        #             style=4,
                        #             label="Rock",
                        #             emoji="🪨",
                        #             disabled=True
                        #         ),
                        #         Button(
                        #             style=3,
                        #             label="Paper",
                        #             emoji="📄",
                        #             disabled=True
                        #         ),
                        #         Button(
                        #             style=1,
                        #             label="Scissors",
                        #             emoji="✂️",
                        #             disabled=True
                        #         )
                        #     ]
                    ],
                )

        except asyncio.TimeoutError:
            await message.edit(
                embed=yet,
                components=[
                    create_actionrow(
                        create_button(style=4, emoji="🪨", disabled=True),
                        create_button(style=3, emoji="📄", disabled=True),
                        create_button(style=1, emoji="✂️", disabled=True),
                        create_button(
                            style=2,
                            label="Session Terminated",
                            emoji=discord.PartialEmoji(
                                name="XWhite", id="873265936357011476"
                            ),
                            disabled=True,
                        ),
                    )
                ],
            )

    @commands.command()
    async def rickroll(self, ctx):
        await ctx.send("https://youtu.be/dQw4w9WgXcQ")

    @cog_ext.cog_slash(name="rickroll", description="😉")
    async def slash_rickroll(self, ctx):
        await ctx.send("https://youtu.be/dQw4w9WgXcQ")


def setup(client):
    client.add_cog(Fun(client))
