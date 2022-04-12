from datetime import datetime
import discord
import DiscordUtils
import asyncio
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option


intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=">", intents=intents)
slash = SlashCommand(client, sync_commands=True)


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tracker = DiscordUtils.InviteTracker(client)

    # Invite tracker for member join
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        inviter = await self.tracker.fetch_inviter(member)
        channel = self.client.get_channel(867861928624783370)
        embed = discord.Embed(
            title="Member Joined",
            description=f"{member.mention} joined; invited by {inviter.mention}",
        )
        await channel.send(embed=embed)

    # Member leave tracker
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        inviter = await self.tracker.fetch_inviter(member)
        if inviter == None:
            inviter = "Unknown"
        channel = self.client.get_channel(867861928624783370)
        embed = discord.Embed(
            title="Member Left",
            description=f"{member.mention} left the server",  # ; invited by {inviter} \n(Not working - currently still in development)
        )
        await channel.send(embed=embed)

    # Delete Messages
    @commands.command(aliases=["purge", "clear"])
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, amount=0):
        if amount == 0:
            embed = discord.Embed(
                title="Delete Error",
                description=f"Amount is not defined. Please input `/delete <number>`",
            )
            await ctx.send(embed=embed)
        if amount == 1:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(
                title="Delete", description=f"`{amount} Message` deleted!"
            )
            await ctx.send(embed=embed, delete_after=5)
        if amount > 1:
            await ctx.channel.purge(limit=amount + 1)
            embed = discord.Embed(
                title="Delete", description=f"`{amount} Messages` deleted!"
            )
            await ctx.send(embed=embed, delete_after=5)

    # Delete Messages Error if Permissions not Sufficient
    @delete.error
    async def delete_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            perm_error_embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=perm_error_embed)

    # Slash Delete Messages
    @cog_ext.cog_slash(
        name="delete",
        description="Purges messages as specified",
        options=[
            create_option(
                name="amount",
                description="Input amount to delete",
                required=True,
                option_type=4,
            )
        ],
    )
    @commands.has_permissions(manage_messages=True)
    async def slash_delete(self, ctx: SlashContext, amount):
        if amount == 0:
            embed = discord.Embed(
                title="Delete Error",
                description=f"Amount is not defined. Please input `/delete <number>`",
            )
            await ctx.send(embed=embed)
        if amount == 1:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(
                title="Delete", description=f"`{amount} Message` deleted!"
            )
            await ctx.send(embed=embed, delete_after=5)
        if amount > 1:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(
                title="Delete", description=f"`{amount} Messages` deleted!"
            )
            await ctx.send(embed=embed, delete_after=5)

    # Slash Command Delete Error
    @slash_delete.error
    async def slash_delete_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Kick Member
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Undefined"):
        if member == ctx.message.author:
            embed = discord.Embed(
                title="Command Error",
                description=f"Prohibited. Command user attempted to kick command user.",
            )
            await ctx.send(embed=embed)
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kick", description=f"Kicked {member.mention}!")
            await ctx.send(embed=embed)

            self.log_channel = self.client.get_channel(779338353895800872)
        embed = discord.Embed(
            title="User Kicked",
            description=f"{ctx.author.mention} kicked {member.mention} in{ctx.channel.mention}.",
            timestamp=datetime.utcnow(),
        )

        await self.log_channel.send(embed=embed)

    # Kick Member Error if Permissions not Sufficient
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(
        name="kick",
        description="Kicks member from the server",
        options=[
            create_option(
                name="member",
                description="Specify user",
                required=True,
                option_type=6,
            ),
            create_option(
                name="reason",
                description="Reasoning for member kick",
                required=False,
                option_type=3,
            ),
        ],
    )
    @commands.has_permissions(kick_members=True)
    async def slash_kick(
        self, ctx: SlashContext, member: commands.MemberConverter, *, reason="Undefined"
    ):
        if member == ctx.author:
            embed = discord.Embed(
                title="Command Error",
                description=f"Prohibited. Command user attempted to kick command user.",
            )
            await ctx.send(embed=embed)
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title="Kick", description=f"Kicked {member.mention}!")
            await ctx.send(embed=embed)

    @slash_kick.error
    async def slash_kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Ban Member
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason="Undefined"):
        if member == ctx.message.author:
            embed = discord.Embed(
                title="Command Error",
                description=f"Prohibited. Command user attempted to ban command user.",
            )
            await ctx.send(embed=embed)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(title="Ban", description=f"Banned {member.mention}!")
            await ctx.send(embed=embed)

            self.log_channel = self.client.get_channel(779338353895800872)
        embed = discord.Embed(
            title="Banned User",
            description=f"{ctx.author.mention} banned {member.mention} in{ctx.channel.mention}.",
            timestamp=datetime.utcnow(),
        )

        await self.log_channel.send(embed=embed)

    # Ban Member Error if Permissions not Sufficient
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
                title="Member Not Found",
                description=f"Unable to recognize the specified member. Please try again.",
            )
            await ctx.send(embed=embed)

    # Slash ban member
    @cog_ext.cog_slash(
        name="ban",
        description="Bans member from the server",
        options=[
            create_option(
                name="member",
                description="Specify user",
                required=True,
                option_type=6,
            ),
            create_option(
                name="reason",
                description="Reasoning for member ban",
                required=False,
                option_type=3,
            ),
        ],
    )
    @commands.has_permissions(ban_members=True)
    async def slash_ban(self, ctx, member: discord.Member, *, reason="Undefined"):
        if member == ctx.author:
            ban_author_msg = f"Prohibited. Command user attempted to ban command user."
            ban_author_embed = discord.Embed(
                title="Command Error", description=ban_author_msg
            )
            await ctx.send(embed=ban_author_embed)
        else:
            await member.ban(reason=reason)
            user = member
            ban_msg = f"Banned {user.mention}!"
            ban_embed = discord.Embed(title="Ban", description=ban_msg)
            await ctx.send(embed=ban_embed)

    @slash_ban.error
    async def slash_ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            perm_error_embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=perm_error_embed)

    # Unban User
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: commands.UserConverter, *, reason="Undefined"):
        banned_users = await ctx.guild.bans()
        # member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban(user, reason=reason)
            embed = discord.Embed(
                title="Unban", description=f"Unbanned {user.mention}!"
            )
            await ctx.send(embed=embed)

            # if (user.name, user.discriminator == member_name, member_discriminator):
            #     await ctx.guild.unban(user)
            #     embed = discord.Embed(
            #         title="Unban",
            #         description=f"Unbanned {user.mention}"
            #     )
            #     await ctx.send(embed=embed)

        self.log_channel = self.client.get_channel(779338353895800872)
        embed = discord.Embed(
            title="User Unbanned",
            description=f"{ctx.author.mention} Unbanned {user.mention}.",
            timestamp=datetime.utcnow(),
        )

        await self.log_channel.send(embed=embed)

    class DurationConverter(commands.Converter):
        async def convert(self, ctx, argument):
            amount = argument[:-1]
            unit = argument[-1]

            if amount.isdigit() and unit in ["s", "m", "h"]:
                return (int(amount), unit)

            raise commands.BadArgument(message="Invalid duration")

    # Tempban User (in progress)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(
        self,
        ctx,
        member: commands.MemberConverter,
        duration: DurationConverter,
        *,
        reason="Undefined",
    ):
        multiplier = {"s": 1, "m": 60, "h": 3600}
        amount, unit = duration

        if member == ctx.message.author:
            embed = discord.Embed(
                title="Command Error",
                description=f"Prohibited. Command user attempted to tempban command user.",
            )
            await ctx.send(embed=embed)
        else:
            await ctx.guild.ban(member, reason=reason)
            embed = discord.Embed(
                title="TempBan",
                description=f"Temporarily banned {member.mention} for `{amount}{unit}`!",
            )

            await ctx.send(embed=embed)
            await asyncio.sleep(amount * multiplier[unit])
            await ctx.guild.unban(member)

    # Tempban Error
    @tempban.error
    async def tempban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(
                title="Member Not Found",
                description=f"Unable to recognize the specified member. Please try again.",
            )
            await ctx.send(embed=embed)

    # Setup Mute Command
    # @commands.command(description="Creates the Muted role")
    # @commands.has_permissions(manage_messages=True)
    # async def setupmute(self, ctx):
    #     guild = ctx.guild
    #     mutedRole = discord.utils.get(guild.roles, name="Muted")

    #     if mutedRole:
    #         embed = discord.Embed(
    #             title="Error",
    #             description="Muted role has already been created."
    #         )
    #         await ctx.send(embed=embed)

    #     if not mutedRole:
    #         mutedRole = await guild.create_role(name='Muted')
    #         embed = discord.Embed(
    #             title="Complete",
    #             description="The `Muted` role has been setup for the server."
    #         )
    #         await ctx.send(embed=embed)

    #         for self.channel in guild.channels:
    #             await self.channel.set_permissions(mutedRole, speak=False, send_messages=False, add_reactions=False)

    # # Setup Mute Permissions Error
    # @setupmute.error
    # async def setupmute_error(self, ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         embed = discord.Embed(
    #             title="Permissions Error",
    #             description="Permissions `not sufficient`. Command prohibited.",
    #         )
    #         await ctx.send(embed=embed)

    # Mute User
    @commands.command(description="Mutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: commands.MemberConverter, *, reason="Undefined"):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        # member_muted = discord.utils.find(guild.roles, name="Muted")

        if member == ctx.message.author:
            embed = discord.Embed(
                title="Command Error",
                description=f"Prohibited. Command user attempted to mute command user.",
            )
            await ctx.send(embed=embed)
        else:
            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")

                for self.channel in guild.channels:
                    await self.channel.set_permissions(
                        mutedRole, speak=False, send_messages=False, add_reactions=False
                    )

            await member.add_roles(mutedRole, reason=reason)

            embed = discord.Embed(title="Mute", description=f"Muted {member.mention}!")
            await ctx.send(embed=embed)

            self.log_channel = self.client.get_channel(779338353895800872)
            embed = discord.Embed(
                title="User Muted",
                description=f"{ctx.author.mention} muted {member.mention} in{ctx.channel.mention}.",
                timestamp=datetime.utcnow(),
            )

            await self.log_channel.send(embed=embed)

    # Mute User Permissions Error
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Unmute User
    @commands.command(description="Unmutes a specified user.")
    @commands.has_permissions(manage_messages=True)
    async def unmute(
        self, ctx, member: commands.MemberConverter, *, reason="Undefined"
    ):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole, reason=reason)
        embed = discord.Embed(title="Unmute", description=f"Unmuted {member.mention}!")
        await ctx.send(embed=embed)

        self.log_channel = self.client.get_channel(779338353895800872)
        embed = discord.Embed(
            title="User Unmuted",
            description=f"{ctx.author.mention} unmuted {member.mention}.",
            timestamp=datetime.utcnow(),
        )

        await self.log_channel.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Tempmute User
    @commands.command(description="Temporarily mutes a user.")
    @commands.has_permissions(manage_messages=True)
    async def tempmute(
        self,
        ctx,
        member: commands.MemberConverter,
        duration: DurationConverter,
        *,
        reason="Undefined",
    ):
        multiplier = {"s": 1, "m": 60, "h": 3600}
        amount, unit = duration
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        await member.add_roles(mutedRole, reason=reason)
        embed = discord.Embed(
            title="Tempmute", description=f"Tempmuted {member.mention}!"
        )
        await ctx.send(embed=embed)
        await asyncio.sleep(amount * multiplier[unit])
        await member.remove_roles(mutedRole)

        self.log_channel = self.client.get_channel(779338353895800872)
        embed = discord.Embed(
            title="User Tempmuted",
            description=f"{ctx.author.mention} tempmuted {member.mention} for {duration} in {ctx.channel.mention}.",
            timestamp=datetime.utcnow(),
        )

        await self.log_channel.send(embed=embed)

    # Tempmute Permissions Error
    @tempmute.error
    async def tempmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Slowmode command
    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, duration: DurationConverter):
        multiplier = {"s": 1, "m": 60, "h": 3600}
        amount, unit = duration
        if amount * multiplier[unit] > 21600:
            embed = discord.Embed(
                title="Duration Error",
                description="Invalid duration! Amount exceeds Discord limits.",
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Slowmode", description=f"Slowmode updated to `{amount}{unit}`!"
            )
            await ctx.channel.edit(slowmode_delay=(amount * multiplier[unit]))
            await ctx.send(embed=embed)

    @slowmode.command(aliases=["ofF", "oFf", "oFF", "Off", "OfF", "OFf", "OFF"])
    async def off(self, ctx, channel: discord.TextChannel = None):
        if ctx.channel.slowmode_delay == 0:
            embed = discord.Embed(
                title="Slowmode Error", description="Slowmode is already disabled!"
            )
            await ctx.send(embed=embed)
        else:
            await ctx.channel.edit(slowmode_delay=0)
            embed = discord.Embed(
                title="Slowmode",
                description=f"Slowmode is disabled for {ctx.channel.mention}!",
            )
            await ctx.send(embed=embed)

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permissions Error",
                description="Permissions `not sufficient`. Command prohibited.",
            )
            await ctx.send(embed=embed)

    # Channel lockdown command
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(
                    send_messages=False, add_reactions=False, speak=False
                )
            }
            await channel.edit(overwrites=overwrites)
            embed = discord.Embed(
                title="Lock", description=f"Locked {channel.mention}!"
            )
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(
                title="Lock", description=f"Locked {channel.mention}!"
            )
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].add_reactions == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.add_reactions = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(
                title="Lock", description=f"Locked {channel.mention}!"
            )
            await ctx.send(embed=embed)
        elif channel.overwrites[ctx.guild.default_role].speak == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.speak = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            embed = discord.Embed(
                title="Lock", description=f"Locked {channel.mention}!"
            )
            await ctx.send(embed=embed)
        # else:
        #     overwrites = channel.overwrites[ctx.guild.default_role]
        #     overwrites.send_messages = None
        #     overwrites.add_reactions = None
        #     overwrites.speak = None
        #     await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
        #     embed = discord.Embed(
        #         title="Unlock",
        #         description=f"Unlocked {channel.mention}!"
        #     )
        #     await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrites = channel.overwrites[ctx.guild.default_role]
        overwrites.send_messages = None
        overwrites.add_reactions = None
        overwrites.speak = None
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
        embed = discord.Embed(
            title="Unlock", description=f"Unlocked {channel.mention}!"
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Mod(client))
