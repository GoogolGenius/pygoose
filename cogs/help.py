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
from discord_slash import *

client = commands.Bot(command_prefix=">")
slash = SlashCommand(client, sync_commands=True)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    DiscordComponents(client)

    # Defining Modules for help command
    key = "Arguments: [Required] (Optional) | Note: For commands that have not yet been updated with Discord Slash Commands, use the default or custom bot prefix."

    help_main = discord.Embed(
        title="Help: Table of Contents",
        description="Welcome to PyGoose Command Support! Use the buttons below to navigate to your query. Website: https://pygoose.webflow.io",
    )

    help_main.add_field(
        name="AV", value="Antivirus/malware protection\n`Page 3`", inline=False
    )

    help_main.add_field(name="Auto", value="Server automation\n`Page 4`", inline=False)

    help_main.add_field(
        name="Bot", value="Bot associated functions\n`Page 5`", inline=False
    )

    help_main.add_field(name="Custom", value="Custom commands\n`Page 6`")

    help_main_cont = discord.Embed(
        title="Help: Table of Contents (Continued)",
        description="Welcome to PyGoose Command Support! Use the buttons below to navigate to your query. Website: https://pygoose.webflow.io",
    )

    help_main_cont.add_field(name="Fun", value="Fun commands\n`Page 7`", inline=False)

    help_main_cont.add_field(
        name="Misc", value="Unrelated commands\n`Page 8`", inline=False
    )

    help_main_cont.add_field(
        name="Mod", value="Server moderation\n`Page 9`", inline=False
    )

    help_main_cont.add_field(
        name="React", value="Reaction roles\n`Page 10`", inline=False
    )

    help_main_cont.add_field(
        name="XP", value="Experience system\n`Page 11`", inline=False
    )

    help_main_cont.set_footer(text=key)

    help_main.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_main_cont.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )

    help_main.set_footer(text=f"{key}")

    help_av = discord.Embed(
        title="Help: AV Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )
    help_av.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_av.set_footer(text=f"{key}")

    help_auto = discord.Embed(
        title="Help: Auto Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )

    # help_auto.add_field(
    #     name="Add",
    #     value="Add keyword for message autoresponse\n`/autoresponder add [keyword]`",
    #     inline=False,
    # )

    # help_auto.add_field(
    #     name="Remove",
    #     value="Delete keyword for message autoresponse\n`/autoresponder remove [keyword]`",
    #     inline=False,
    # )

    # help_auto.add_field(
    #     name="List",
    #     value="Shows list of AutoResponses\n`/autoresponder list`",
    #     inline=False,
    # )

    help_auto.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_auto.set_footer(text=f"{key}")

    help_bot = discord.Embed(title="Help: Bot Module")
    help_bot.add_field(
        name="Ping",
        value="Displays message containing bot latency\n`/ping`",
        inline=False,
    )
    help_bot.add_field(
        name="SetPrefix",
        value="Change the default bot prefix for your server\n`/setprefix`",
    )
    help_bot.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_bot.set_footer(text=f"{key}")

    help_custom = discord.Embed(
        title="Help: Custom Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )

    help_custom.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_custom.set_footer(text=f"{key}")

    help_xp = discord.Embed(
        title="Help: XP Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )
    # help_xp.add_field(
    #     name="Rank",
    #     value="Displays member experience rank\n`/rank (member)`",
    #     inline=False,
    # )
    # help_xp.add_field(
    #     name="XP",
    #     value="Shows leading experience members\n`/xp`",
    #     inline=False,
    # )
    help_xp.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_xp.set_footer(text=f"{key}")

    help_fun = discord.Embed(title="Help: Fun Module")
    help_fun.add_field(name="Cat", value="Sends photos of cats\n`/cat`", inline=False)
    help_fun.add_field(name="Dog", value="Sends photoes of dogs\n`/dog`", inline=False)
    help_fun.add_field(
        name="Meme",
        value="Retrieves and sends memes from the Reddit SubReddit r/memes\n`/meme`",
        inline=False,
    )
    help_fun.add_field(
        name="Flip", value="Flip a coin in Discord\n`/flip`", inline=False
    )
    help_fun.add_field(
        name="RPS", value="Play Rock Paper Scissors with the bot\n`/rps`", inline=False
    )
    help_fun.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_fun.set_footer(text=f"{key}")

    help_misc = discord.Embed(title="Help: Misc Module", inline=False)
    help_misc.add_field(
        name="Calculator", value="Opens a basic calculator\n`/calculator`", inline=False
    )
    help_misc.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_misc.set_footer(text=f"{key}")

    help_mod = discord.Embed(title="Help: Mod Module")
    help_mod.add_field(
        name="Ban",
        value="Bans member from the server\n`/ban [member] (reason)`",
        inline=False,
    )
    help_mod.add_field(
        name="Delete",
        value="Purges messages as specified\n`/delete [integer amount]`",
        inline=False,
    )
    help_mod.add_field(
        name="Kick",
        value="Kicks member from the server\n`/kick [member] (reason)`",
        inline=False,
    )
    help_mod.add_field(
        name="Mute",
        value="Mute and prevent member from speaking, chatting, and reacting\n`/tempban [member] [time s, m, h]`",
        inline=False,
    )
    help_mod.add_field(
        name="Slowmode",
        value="Set text channel slowmode\n`/slowmode [time s, m, h]`",
        inline=False,
    )
    help_mod.add_field(
        name="Tempban",
        value="Temporarily ban member from the server\n`/tempban [member] [time s, m, h]`",
        inline=False,
    )
    help_mod.add_field(
        name="Tempmute",
        value="Temporarily mute member in the guild\n`/tempmute [member] [time s, m, h]`",
        inline=False,
    )
    help_mod.add_field(
        name="Unban",
        value="Unban user from the server\n`/unban [user#0000]`",
        inline=False,
    )
    help_mod.add_field(
        name="Unmute",
        value="Unmute user in the guild\n`/unmute [member]`",
        inline=False,
    )
    help_mod.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_mod.set_footer(text=f"{key}")

    help_react = discord.Embed(
        title="Help: React Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )

    help_react.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_react.set_footer(text=f"{key}")

    help_search = discord.Embed(
        title="Help: Search Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )

    help_xp = discord.Embed(
        title="Help: XP Module (Coming Soon)",
        description="Bob the Builder is still contructing this module. Check again another time!",
    )

    help_xp.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/861341470904942622/d4843ded1abc2ba3c09066a25aa999b0.webp?size=512"
    )
    help_xp.set_footer(text=f"{key}")

    pagination_list = [
        help_main,
        help_main_cont,
        help_av,
        help_auto,
        help_bot,
        help_custom,
        help_fun,
        help_misc,
        help_mod,
        help_react,
        help_search,
        help_xp,
    ]

    timeout = 60

    @commands.command()
    async def help(self, ctx):
        current = 0
        main_message = await ctx.send(
            embed=self.pagination_list[current],
            components=[
                [
                    Button(
                        id=("Previous"),
                        emoji=discord.PartialEmoji(
                            name="ArrowWhiteLeft", id="872556071863062558"
                        ),
                        style=ButtonStyle.blue,
                    ),
                    Button(
                        id=("Next"),
                        emoji=discord.PartialEmoji(
                            name="ArrowWhiteRight", id="872556071825334282"
                        ),
                        style=ButtonStyle.blue,
                    ),
                    Button(
                        id=("Page#"),
                        label=f"Page {int((self.pagination_list.index)(self.pagination_list[current])) + 1}/{len(self.pagination_list)}",
                        emoji=discord.PartialEmoji(
                            name="PageDocumentBlank", id="873391225728827473"
                        ),
                        style=ButtonStyle.gray,
                        disabled=True,
                    ),
                ]
            ],
        )

        while True:
            try:
                interaction = await self.client.wait_for(
                    "button_click",
                    check=lambda i: i.component.id in ["Previous", "Next"],
                    timeout=self.timeout,
                )

                if interaction.component.id == "Previous":
                    current -= 1
                elif interaction.component.id == "Next":
                    current += 1

                if current == len(self.pagination_list):
                    current = 0
                elif current < 0:
                    current = len(self.pagination_list) - 1

                await interaction.respond(
                    type=InteractionType.UpdateMessage,
                    embed=self.pagination_list[current],
                    components=[
                        [
                            Button(
                                id=("Previous"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteLeft", id="872556071863062558"
                                ),
                                style=ButtonStyle.blue,
                            ),
                            Button(
                                id=("Next"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteRight", id="872556071825334282"
                                ),
                                style=ButtonStyle.blue,
                            ),
                            Button(
                                id=("Page#"),
                                label=f"Page {int((self.pagination_list.index)(self.pagination_list[current])) + 1}/{len(self.pagination_list)}",
                                emoji=discord.PartialEmoji(
                                    name="PageDocumentBlank", id="873391225728827473"
                                ),
                                style=ButtonStyle.gray,
                                disabled=True,
                            ),
                        ]
                    ],
                )

            except asyncio.TimeoutError:
                await main_message.edit(
                    components=[
                        [
                            Button(
                                id=("Previous"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteLeft", id="872556071863062558"
                                ),
                                style=ButtonStyle.blue,
                                disabled=True,
                            ),
                            Button(
                                id=("Next"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteRight", id="872556071825334282"
                                ),
                                style=ButtonStyle.blue,
                                disabled=True,
                            ),
                            Button(
                                id=("Timeout"),
                                label=f"Session Terminated",
                                emoji=discord.PartialEmoji(
                                    name="XWhite", id="873265936357011476"
                                ),
                                style=ButtonStyle.gray,
                                disabled=True,
                            ),
                        ]
                    ]
                )
                break

    @cog_ext.cog_slash(
        name="help", description="Summon forth the PyGoose Command Support"
    )
    async def slash_help(self, ctx):
        current = 0
        main_message = await ctx.send(
            embed=self.pagination_list[current],
            components=[
                create_actionrow(
                    create_button(
                        custom_id=("Previous"),
                        emoji=discord.PartialEmoji(
                            name="ArrowWhiteLeft", id="872556071863062558"
                        ),
                        style=ButtonStyle.blue,
                    ),
                    create_button(
                        custom_id=("Next"),
                        emoji=discord.PartialEmoji(
                            name="ArrowWhiteRight", id="872556071825334282"
                        ),
                        style=ButtonStyle.blue,
                    ),
                    create_button(
                        custom_id=("Page#"),
                        label=f"Page {int((self.pagination_list.index)(self.pagination_list[current])) + 1}/{len(self.pagination_list)}",
                        emoji=discord.PartialEmoji(
                            name="PageDocumentBlank", id="873391225728827473"
                        ),
                        style=ButtonStyle.gray,
                        disabled=True,
                    ),
                )
            ],
        )

        while True:
            try:
                interaction = await self.client.wait_for(
                    "button_click",
                    check=lambda i: i.component.custom_id in ["Previous", "Next"],
                    timeout=self.timeout,
                )

                if interaction.component.custom_id == "Previous":
                    current -= 1
                elif interaction.component.custom_id == "Next":
                    current += 1

                if current == len(self.pagination_list):
                    current = 0
                elif current < 0:
                    current = len(self.pagination_list) - 1

                await interaction.respond(
                    type=InteractionType.UpdateMessage,
                    embed=self.pagination_list[current],
                    components=[
                        create_actionrow(
                            create_button(
                                custom_id=("Previous"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteLeft", id="872556071863062558"
                                ),
                                style=ButtonStyle.blue,
                            ),
                            create_button(
                                custom_id=("Next"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteRight", id="872556071825334282"
                                ),
                                style=ButtonStyle.blue,
                            ),
                            create_button(
                                custom_id=("Page#"),
                                label=f"Page {int((self.pagination_list.index)(self.pagination_list[current])) + 1}/{len(self.pagination_list)}",
                                emoji=discord.PartialEmoji(
                                    name="PageDocumentBlank", id="873391225728827473"
                                ),
                                style=ButtonStyle.gray,
                                disabled=True,
                            ),
                        )
                    ],
                )

            except asyncio.TimeoutError:
                await main_message.edit(
                    components=[
                        create_actionrow(
                            create_button(
                                custom_id=("Previous"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteLeft", id="872556071863062558"
                                ),
                                style=ButtonStyle.blue,
                                disabled=True,
                            ),
                            create_button(
                                custom_id=("Next"),
                                emoji=discord.PartialEmoji(
                                    name="ArrowWhiteRight", id="872556071825334282"
                                ),
                                style=ButtonStyle.blue,
                                disabled=True,
                            ),
                            create_button(
                                custom_id=("Timeout"),
                                label=f"Session Terminated",
                                emoji=discord.PartialEmoji(
                                    name="XWhite", id="873265936357011476"
                                ),
                                style=ButtonStyle.gray,
                                disabled=True,
                            ),
                        )
                    ]
                )
                break


def setup(client):
    client.add_cog(Help(client))
