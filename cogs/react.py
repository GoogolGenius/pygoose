from discord.ext import commands


class React(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(React(client))
