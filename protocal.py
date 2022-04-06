import discord
from discord.ext import commands
import random
import asyncio

class Protocal(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Protocal Cog Initiated\n----------------------------")
        
    @commands.command(name="protocal1")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal1(self, ctx):
        codes = ["p1", "fireout", "extinguish"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 1: Fire Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 1 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('fire.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal2")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal2(self, ctx):
        codes = ["p2", "antivenom", "cure"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 2: Poison Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 2 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('poison.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal3")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal3(self, ctx):
        codes = ["p3", "anticlown", "joker"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 3: Clown Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 3 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('clown.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal4")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal4(self, ctx):
        codes = ["p4", "antiwater", "evaporate"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 4: Water Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 4 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('water.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal5")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal5(self, ctx):
        codes = ["p5", "antiice", "melt"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 5: Ice Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 5 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('ice.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal6")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal6(self, ctx):
        codes = ["p6", "antinuclear", "radiation"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 6: Nuclear Insaneno')
                    await asyncio.sleep(4)                   
                    await message2.edit(content=f'Protocal 6 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('nuclear.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
    @commands.command(name="protocal7")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def protocal7(self, ctx):
        codes = ["p7", "antinull", "debug"]
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Protocal Activation Code.")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You Didn\'t Answer In Time, Connection Closed.')
            return
        else:
            for code in codes:
                if msg.content == code:
                    message2 = await ctx.send('Successfully Verified Protocal Activation Code. \nInitiating Protocol 7: Null Insaneno')
                    await asyncio.sleep(2)
                    await message2.edit(content=f'Initiating Omega Scranton Reality Anchor')
                    await asyncio.sleep(2)                   
                    await message2.edit(content=f'Protocal 7 Successfully Initiated, Target Has Been Neutralized.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('null.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Protocal Activation Code, Connection Closed.")
            return
        
def setup(client):
    client.add_cog(Protocal(client))
