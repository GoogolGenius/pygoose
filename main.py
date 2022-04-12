import os
import json
import discord
import asyncio
import DiscordUtils
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
from web.server import keep_alive


def get_prefix(client, message):
    with open("prefix.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]


# mongo_url_connect = os.environ.get("CONNECTION_URL")
# cluster = MongoClient(mongo_url_connect)
token = os.environ["PG_APPLICATION_TOKEN"]
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, intents=intents, case_insensitive=True)
slash = SlashCommand(client, sync_commands=True)
tracker = DiscordUtils.InviteTracker(client)
# guild_ids = client.get_guild(id)
guild_ids = [732289171783155823]  # Goose Empire Guild ID

# Help Command
client.remove_command("help")


@client.event
async def on_guild_join(guild):
    with open("prefix.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = ">"

    with open("prefix.json", "w") as f:
        json.dump(prefix, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("prefix.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("prefix.json", "w") as f:
        json.dump(prefix, f, indent=4)


@client.command()
async def setprefix(ctx, value):
    with open("prefix.json", "r") as f:
        prefix = json.load(f)

    prefix[str(ctx.guild.id)] = value

    with open("prefix.json", "w") as f:
        json.dump(prefix, f, indent=4)

    embed = discord.Embed(
        title="SetPrefix", description=f"Modified server prefix to `{value}`!"
    )

    await ctx.send(embed=embed)


# For commands in which only devs should access, accomplished with @commands.check
def dev_access(ctx):
    return ctx.author.id == 732271287002726402 or ctx.author.id == 565292950020685844


# Loads specified cog
@client.command()
@commands.check(dev_access)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    embed = discord.Embed(title="Load", description=f"Enabled module `{extension}`!")
    await ctx.send(embed=embed)


# Unloads specified cog
@client.command()
@commands.check(dev_access)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    embed = discord.Embed(title="Unload", description=f"Disabled module `{extension}`!")
    await ctx.send(embed=embed)


# Reloads specified cog
@client.command()
@commands.check(dev_access)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    embed = discord.Embed(title="Reload", description=f"Reloaded module `{extension}`!")
    await ctx.send(embed=embed)


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# Setting Playing Status
@client.event
async def on_ready():
    print("Ready.")
    DiscordComponents(client)
    await client.change_presence(
        status=discord.Status.idle, activity=discord.Game(name="Invite Scripty")
    )
    # while True:
    #     await client.change_presence(activity=discord.Game(name="cmds | >help"))
    #     await asyncio.sleep(5)
    #     await client.change_presence(activity=discord.Game(name="with Python!"))
    #     await asyncio.sleep(5)


# Keep Web Server Running
keep_alive()


# Run Bot with Token
client.run(token)
