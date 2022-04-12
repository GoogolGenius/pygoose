import discord
from discord.ext import commands


class Auto(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Infinite Chill Loop
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        elif "chill" in message.content.lower():
            await message.channel.send("bruh")
        elif "bruh" in message.content.lower():
            await message.channel.send("chill")


def setup(client):
    client.add_cog(Auto(client))
