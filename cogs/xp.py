import os
import discord
from discord.ext import commands
from pymongo import MongoClient
import dns

client = commands.Bot(
    command_prefix=">", intents=discord.Intents.all(), case_insensitive=True
)

# channels = [853694702410792960]

# levelRoles = ["Dirt (Level 1)", "Stone (Level 5)", "Copper (Level 10)", "Iron (Level 20)", "Gold (Level 30)", "Diamond (Level 40)", "Platinum (Level 50)"]

# levelNumber = [1, 5, 10, 20, 30, 40, 50]

# MONGO_SRV = os.environ['MONGO_SRV']
# cluster = MongoClient(MONGO_SRV)

# XPdb = cluster["Discord"]
# XP_collection = XPdb["XP"]


class XP(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def xp2(self, ctx):
        await ctx.send(f"The Experience Module is Coming Soon!")

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.channel.id in channels:
    #         stats = XP_collection.find_one({"_id": message.author.id})
    #         if not message.author.bot:
    #             if stats is None:
    #                 newUser = {"_id": message.author.id, "xp": 0}
    #                 XP_collection.insert_one(newUser)
    #             else:
    #                 xp = stats["xp"] + 5
    #                 XP_collection.update_one({"_id": message.author.id}, {"set":{"xp": xp}})
    #                 lvl = 0
    #                 while True:
    #                     if xp < ((50*(lvl**2))+(50*(lvl-1))):
    #                         break
    #                     lvl += 1
    #                 xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
    #                 if xp == 0:
    #                     await message.channel.send(f"Contragulations {message.author.mention}! You leveled up to **level {lvl}**.")
    #                     for i in range(len(levelRoles)):
    #                         if lvl == levelNumber[i]:
    #                             await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=levelNumber[i]))
    #                             embed = discord.Embed(title="XP Rank", description=f"{message.author.mention} you have recived {levelRoles[i]}!")
    #                             embed.set_thumbnail(url=message.author.avatar_url)
    #                             await message.channel.send(embed=embed)

    # @commands.command()
    # async def rank(self, ctx):
    #     stats = XP_collection.find_one({"_id": ctx.author.id})
    #     if stats is None:
    #         embed = discord.Embed(description="You have no rank! Send some more messages and check again.")
    #         await ctx.channel.send(embed=embed)
    #     else:
    #         xp = stats["xp"]
    #         lvl = 0
    #         rank = 0
    #         while True:
    #             if xp < ((50*(lvl**2))+(50*(lvl-1))):
    #                 break
    #             lvl += 1
    #         xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
    #         boxes = int((xp/(200*((1/2)*lvl)))*20)
    #         rankings = XP_collection.find().sort("xp",-1)
    #         for x in rankings:
    #             rank+= 1
    #             if stats["_id"] == x["_id"]:
    #                 break
    #         embed = discord.Embed(title = "{}'s XP Statistics".format(ctx.author.name))
    #         embed.add_field(name="Name", value=ctx.author.mention, inline=True)
    #         embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2),*lvl))}", inline=True)
    #         embed.add_field(name="Rank", value=f"{rank}/{ctx.guild.member_count}", inline=True)
    #         embed.add_field(name="Progress Bar [lvl]", value=boxes * ":bllue_square:" + (20-boxes) * "white_large_square:", inline=True)
    #         embed.set_thumbnail(url=ctx.author.avatar_url)
    #         await ctx.channel.send(embed=embed)

    # @commands.command()
    # async def xp(self, ctx):
    #     rankings = XP_collection.find().sort("xp", -1)
    #     i = 1
    #     embed = discord.Embed(title="XP")
    #     for x in rankings:
    #         try:
    #             temp = ctx.guild.get_member(x["_id"])
    #             tempXP = x["xp"]
    #             embed.add_field(name=f"{i}: {temp.name}", value=f"Total XP: {tempXP}", inline=False)
    #             i += 1
    #         except:
    #             pass
    #         if i == 0:
    #             break
    #     await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(XP(client))
