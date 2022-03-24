import discord
from discord.ext import commands
import asyncio
import random
import datetime

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod cog loaded successfully \n----------------------------")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def date(self, ctx):
        datetoday = datetime.today().strftime('%Y-%m-%d-%H:%M')
        await ctx.send(datetoday)

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def clear(self, ctx, amount=None):
        if amount == None:
            await ctx.send('Dude I can\'t delete nothing?')
        amount = int(amount)+1
        if amount >= 100:
            await ctx.send("I can\'t delete more than 100 messages.")
        else:
            await ctx.channel.purge(limit = amount)
            await ctx.send(f"{amount} messages were cleared.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        if reason is None:
            await ctx.send(f'{member} was kicked from the server. Reason: No reasons provided.')
        if member is None:
            await ctx.send("You need to mention a user.")           
        else:
            await ctx.send(f'{member} was kicked from the server. Reason: {reason}.')

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == None:
            await ctx.send("My G you need to mention a user.")
        else:
            await member.ban(reason=reason)
        if reason is None:
            await ctx.send(f'{member} was banned from the server. Reason: No reasons provided')
        else:
            await ctx.send(f'{member} was banned from the server. Reason: {reason}')

    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def unban(self, ctx, *, member: discord.Member):
        if member == None:
            await ctx.send("Dude you need to mention a user.")
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return

    @commands.command(name='info', aliases=['userinfo'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def info(self, ctx, member : discord.Member):
        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar.url)
        embed.set_author(name="User Info: ")
        embed.set_thumbnail(url = member.avatar.url)
        embed.add_field(name="User ID:", value=member.id, inline=False)
        embed.add_field(name="User Name:",value=member.display_name, inline=False)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
        embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
        embed.add_field(name="Bot?:", value=member.bot, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def role(self, ctx, member: discord.Member, *, role_name = None):
        guild_id = ctx.message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
        if role_name is not None:
            role = discord.utils.get(guild.roles, name=role_name)

            if role is not None:
                res = await member.add_roles(role)
                await ctx.send(f'Role "{role}" is added to member: {member}')
            else:
                await ctx.send(f'Role "{role_name}" was not found')
        else:
            await ctx.send('Please make sure you message contains a role name')

    @commands.has_permissions(administrator=True)
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def takerole(self, ctx, member: discord.Member, *, role_name= None):
        guild_id = ctx.message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, self.client.guilds)
        if role_name is not None:
            role = discord.utils.get(guild.roles, name=role_name)

            if role is not None:
                res = await member.remove_roles(role)
                await ctx.send(f'Role "{role}" is removed from member: {member}')
            else:
                await ctx.send(f'Role "{role_name}" was not found')
        else:
            await ctx.send('Please make sure you message contains a role name')

    @commands.has_permissions(administrator=True)
    @commands.command(name='mute')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        role = ctx.guild.get_role(859989640118927363)
        res = await member.add_roles(role)
        if reason is None:
            await ctx.send(f'Muted {member}. Reason: No reasons provided')
        else:
            await ctx.send(f'Muted {member}. Reason: {reason}')

    @commands.has_permissions(administrator=True)
    @commands.command(name='unmute')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def unmute(self, ctx, member: discord.Member):
        role = ctx.guild.get_role(859989640118927363)
        res = await member.remove_roles(role)
        await ctx.send(f'{member} has been unmuted')
        
    @commands.has_permissions(administrator=True)
    @commands.command(name='createchannel')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def createchannel(self, ctx, channel_name=None):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def avatar(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        await ctx.send(f'{user.avatar.url}')
        
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(title = 'Invite Me!', description = 'https://discord.com/api/oauth2/authorize?client_id=850392624154148905&permissions=8&scope=bot', colour = discord.Colour.random(), timestamp = ctx.message.created_at)
        embed.add_field(name = "Invite Ah Beng:", value = "https://discord.com/api/oauth2/authorize?client_id=889357799006568458&permissions=8&scope=bot")
        embed.set_footer(text = f"Requested by {ctx.author.name}, thanks for using me!")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def reminder(self, ctx, time, *, task):
        def convert(time):
            pos = ['s', 'm', 'h', 'd']

            time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

            unit = time[-1]

            if unit not in pos:
                return -1
            try:
                val = int(time[:-1])
            except:
                return -2
            
            return val * time_dict[unit]

        converted_time = convert(time)

        if converted_time == -1:
            await ctx.send(f"You didn't type the time correctly")
            return

        if converted_time == -2:
            await ctx.send(f"The time must be an integer!")
            return

        await ctx.send(f"Started reminder for **{task}** and will last **{time}**.")
        
        await asyncio.sleep(converted_time)
        await ctx.send(f"{ctx.author.mention} your reminder for {task} has finished.")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def timer(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 86400:
                await ctx.send("I don\'t think Im allowed to go above 1 day.")
                raise BaseException
            if secondint <= 0:
                await ctx.send("Bro how do I count negative numbers or nothing")
                raise BaseException
            message = await ctx.send(f"Timer: {seconds}")
            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="Ended!")
                    break
                await message.edit(content=f"Timer: {secondint}")
                await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention} Your timer has ended!")
        except ValueError:
            await ctx.send("Dude you have to put a number!")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userid(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        await ctx.send(f'{user.name}\'s User ID: {user.id}')

def setup(client):
    client.add_cog(Mod(client))