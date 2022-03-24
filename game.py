import discord
from discord.ext import commands
import random
import asyncio

class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Game cog loaded successfully \n----------------------------")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def choose(ctx, *choices: str):
        await ctx.send(random.choice(choices))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def say(self, ctx, *args: str):
        if args == None:
            await ctx.send("Bruv how do I say nothing?")

        response = ""

        for arg in args:
            response = response + " " + arg

        await ctx.send(response)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dm(self, user_id = None, *, args = None):
        if user_id != None and args != None:
            try:
                target = await client.fetch_user(user_id)
                await target.send(args)
                await ctx.channel.send("'" + args + "' sent to: " + target.name)
            except:
                await ctx.channel.send("Couldn't dm the given user.")
        else:
            await ctx.channel.send("You didn't provide a user's id and/or a message.")

    @commands.command(name='die', help='This command returns a random last words')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def die(self, ctx):
        die = ['Why have you brought my short life to an end', 'Take me Jesus', 'I have a family let me live man']
        await ctx.send(random.choice(die))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def jayden(self, ctx):
        jlist = ['You have celery sticks for legs you idiot', 'My table lamp has more iq than you', 'Wwhat you want nugget cheesepie', 'Idiot what u want', 'Im Jesus', 'You clown you want to die ah', 'Eat shit go die', 'You little shit']
        randomj = random.choice(jlist)
        await ctx.send(randomj)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kj(self, ctx):
        kjlist = ['I will cut your kukujiao.', 'Your parents are preparing the adoption letter for you.', 'Im Jesus Harold Christ.', 'Ah shit here we go again, have the balls? Ping me again and I will beat you up.', 'Would you like to have a cup of tea?']
        randomkj = random.choice(kjlist)
        await ctx.send(randomkj)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def monk(self, ctx):
        await ctx.send('namo guan jie yim bu sa ha namo guan jie yim kannina kannina kannina kong gan lah')
        await ctx.send(file=discord.File('wll.png'))

    @commands.command(name='choice', help='This command helps you make a choice you indesicive clown', aliases=['8ball'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def choice(self, ctx):
        responses = [
            'I\'m sure about that!',
            'Without a doubt.',
            'This is certain.',
            'Indeed',
            'Positive',
            'I reply positively',
            'Indeed yes!',
            'Oh hell ya!',
            'Ask again later bud!',
            'I\'m not in the mood of replying, ask again later',
            'I am not sure about that',
            'Nah! Not a chance.',
            'Too doubtful',
            'Don\'t count on it.',
            'I would say No.',
            'Nope!',
            'Oh hell nah!',
            'My sources say no.',
            'Negative!'
        ]

        randomresponses = random.choice(responses)

        embed = discord.Embed(title = "Responses", description = randomresponses, color = discord.Colour.random(), timestamp=datetime.datetime.utcfromtimestamp(1580842764))
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='coinflip', help='Flips a coin')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def coinflip(self, ctx):
        flip = ['Heads', 'Tails']
        await ctx.send(random.choice(flip))
            
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def rps2p(self, ctx, user: discord.Member = None):
        choices = ['rock', 'paper', 'scissors']
        answer = random.choice(choices)
        bot_choice = random.choice(choices)
        if user == None:
            await ctx.send("You need to mention a user for this to work bud.")
        else:
            if answer == 'rock':
                if bot_choice == 'rock':
                    await ctx.send(f'You both tied.\n{ctx.author}\'s and {user}\'s {answer}')
                elif bot_choice == 'paper':
                    await ctx.send(f'LMAO {user.mention} won!\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"Pog {ctx.author.mention} won!\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}")

            elif answer == 'paper':
                if bot_choice == 'rock':
                    await ctx.send(f'{ctx.author.mention} is the winner.\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}')
                elif bot_choice == 'paper':
                    await ctx.send(f'You both tied. I call a rematch!!\n{ctx.author}\'s and {user}\'s choice: {answer}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"HAH {user.mention} won! Get rekt boi.\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}")

            elif answer == 'scissors':
                if bot_choice == 'rock':
                    await ctx.send(f'{user.mention} just destroyed you!\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}')
                elif bot_choice == 'paper':
                    await ctx.send(f'Wow {user.mention} lost.\n{ctx.author}\'s choice: {answer}\n{user}\'s choice: {bot_choice}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"Oh well, you both tied.\n{ctx.author} and {user}\'s choice: {answer}")

    @commands.command(name='dice', help='Rolls a dice')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def dice(self, ctx):
        dice = ['1', '2', '3', '4', '5', '6']
        await ctx.send(random.choice(dice))

    @commands.command(name='botrate', help='The Bot-o-meter 1000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def botrate(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        number = random.randint(1, 100)
        embed = discord.Embed(title ='The Bot-o-meter 1000 🤖', description = f"{user.mention} is {number}% a bot", colour = discord.Colour.random())  
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='nerdrate', help='The Nerd-o-meter 2000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nerdrate(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        number = random.randint(1, 100)
        embed = discord.Embed(title ='The Nerd-o-meter 2000 🤓', description = f"{user.mention} is {number}% a nerd", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='simprate', help='The Simp-o-meter 3000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def simprate(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        number = random.randint(1, 100)
        embed = discord.Embed(title = 'The Simp-o-meter 3000 🥺', description = f"{user.mention} is {number}% a simp", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='ship', help='The Ship-o-meter 4000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ship(self, ctx, arg1 = None, arg2 = None):
        number = random.randint(1, 100)
        if arg1 == None:
            arg1 = ctx.author

        if arg2 == None:
            arg2 = ctx.author
        
        embed = discord.Embed(title = 'The Ship-o-meter 4000 ❤️', description = f"{arg1} and {arg2}: {number}% ❤️", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='hack', help='The Hacker Boi 5000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hack(self, ctx, *, user: discord.Member = None):
        if user == None:
            user = ctx.author

        hackchoice = ['bitcoin', 'vbucks', 'diamonds', 'robux', 'dogecoin']

        hackpercent = ['10% ■□□□□□□□□□', '20% ■■□□□□□□□□', '30% ■■■□□□□□□', '40% ■■■■□□□□□□', '50% ■■■■■□□□□□', '60% ■■■■■■□□□□', '70% ■■■■■■■□□□', '80% ■■■■■■■■□□', '90% ■■■■■■■■■□', '100% ■■■■■■■■■■', 'Failed Error - 101']

        randomhack1 = (random.choice(hackchoice))

        randomhack2 = (random.choice(hackpercent))

        message = await ctx.send(f'Hacking {user}')

        await message.edit(content='Bypassing firewall...')
        await asyncio.sleep(1)
        await message.edit(content='Bruteforcing password...')
        await asyncio.sleep(1)
        await message.edit(content=f'Found User ID: {user.id}...')
        await asyncio.sleep(1)
        await message.edit(content='Injecting SQL Nimba Virus...')
        await asyncio.sleep(1)
        await message.edit(content='Stealing user info...')
        await asyncio.sleep(1)
        await message.edit(content=f'Successfully hacked {user.name}, you stole all of their {randomhack1}!')

    @commands.command(name='iq', help='The IQ Meter 6000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def iq(self, ctx, *, user=None):
        if user == None:
            user = ctx.author

        iq = random.randint(1, 180)

        embed = discord.Embed(title = 'The IQ Meter 6000', description = f"{user.mention} has a IQ of {iq}", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='gayrate', help='The Gay-o-meter 6900')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gayrate(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        number = random.randint(1, 100)
        embed = discord.Embed(title = 'The Gay-o-meter 6900', description = f"{user.mention} is {number}% a gay", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(name='liferate', help='The Life-o-meter 8000')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def liferate(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        livelist = ["seconds", "minutes", "hours", "days", "weeks", "months", "years", "decades", "eon", "infinity"]

        live1 = (random.choice(livelist))
        
        live2 = random.randint(1, 65)
        
        embed = discord.Embed(title = 'The Life-o-meter 8000', description = f"{user.mention} is going to live for {live2} {live1}", colour = discord.Colour.random())
        embed.set_footer(icon_url = ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def spoonfeed(self, ctx):
        await ctx.send(file=discord.File('spoonfeed (2).png'))

    @commands.command(aliases=["na"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nobodyasked(self, ctx):
        files = ["nobodyasked1.gif", "nobodyasked2.gif", "nobodyasked3.gif", "nobodyasked4.gif", "nobodyasked5.gif"]
        randomna = random.choice(files)  
        await ctx.send(file=discord.File(randomna))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lzh(self, ctx):
        await ctx.send(file=discord.File('pig.png'))

    @commands.command(aliases=["happybirthday", "happybday"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hbd(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        await ctx.send(f"Happy Birthday {user.mention}!")
        await ctx.send(file=discord.File("hbd.gif"))

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nuke(self, ctx, target = None):
        codes = ["010808", "696969", "812629"]
        location = ["Moscow, Russia", "Kuala Lumpur, Malaysia", "Hiroshima, Japan", "Beijing, China", "Washington, United States", "Pyongyang, North Korea"]
        randomlocation = (random.choice(location))
        if target == None:
            target = randomlocation
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Nuclear Warhead Activation Code.")

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
                    message2 = await ctx.send('Successfully Verified Nuclear Warhead Activation Code. \nIntializing Protocol 69: Lauching Nuclear Warhead In 5')
                    await message2.edit(content='Successfully Verified Nuclear Warhead Activation Code. \nIntializing Protocol 69: Lauching Nuclear Warhead In 4')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Nuclear Warhead Activation Code. \nIntializing Protocol 69: Lauching Nuclear Warhead In 3')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Nuclear Warhead Activation Code. \nIntializing Protocol 69: Lauching Nuclear Warhead In 2')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Nuclear Warhead Activation Code. \nIntializing Protocol 69: Lauching Nuclear Warhead In 1')
                    await asyncio.sleep(1)
                    await message2.edit(content=f'Nuclear Warhead Successfully Launched, Target Is -({target})-.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('nuke.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Nuclear Warhead Activation Code, Connection Closed.")
            return

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def alphanuke(self, ctx, target = None):
        codes = ["alpha", "000000", "launch"]
        location = ["Moscow, Russia", "Kuala Lumpur, Malaysia", "Hiroshima, Japan", "Beijing, China", "Washington, United States", "Pyongyang, North Korea"]
        randomlocation = (random.choice(location))
        if target == None:
            target = randomlocation
        await ctx.send("Establishing Connection....")
        await ctx.send("Input Your Alpha Warhead Activation Code.")

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
                    message2 = await ctx.send('Successfully Verified Alpha Warhead Activation Code. \nIntializing Protocol 69: Lauching Alpha Warhead In 5')
                    await message2.edit(content='Successfully Verified Alpha Warhead Activation Code. \nIntializing Protocol 69: Lauching Alpha Warhead In 4')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Alpha Warhead Activation Code. \nIntializing Protocol 69: Lauching Alpha Warhead In 3')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Alpha Warhead Activation Code. \nIntializing Protocol 69: Lauching Alpha Warhead In 2')
                    await asyncio.sleep(1)
                    await message2.edit(content='Successfully Verified Alpha Warhead Activation Code. \nIntializing Protocol 69: Lauching Alpha Warhead In 1')
                    await asyncio.sleep(1)
                    await message2.edit(content=f'Alpha Warhead Successfully Launched, Target Is -({target})-.')
                    await asyncio.sleep(1)
                    await ctx.send(file=discord.File('alphanuke.gif'))
                    return
                else:
                    continue
            await ctx.send("Invalid Alpha Warhead Activation Code, Connection Closed.")
            return

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rps(self, ctx, answer = None):
        choices = ['rock', 'paper', 'scissors']
        bot_choice = random.choice(choices)
        if answer == None:
            await ctx.send('That is not a valid option! Please reply with rock, paper or scissors.')
            return

        if answer not in choices:
            await ctx.send('That is not a valid option! Please reply with rock, paper or scissors.')
            return
        else:
            if answer == 'rock':
                if bot_choice == 'rock':
                    await ctx.send(f'We tied.\nWe both picked {answer}')
                elif bot_choice == 'paper':
                    await ctx.send(f'LMAO I won!\nYour choice: {answer}\nMy choice: {bot_choice}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"Aw, you beat me.\nYour choice: {answer}\nMy choice: {bot_choice}")

            elif answer == 'paper':
                if bot_choice == 'rock':
                    await ctx.send(f'Oh noooo, you won.\nYour choice: {answer}\nMy choice: {bot_choice}')
                elif bot_choice == 'paper':
                    await ctx.send(f'We tied. I call a rematch!!\nOur choice: {answer}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"HAH I won! Get rekt boi.\nYour choice: {answer}\nMy choice: {bot_choice}")

            elif answer == 'scissors':
                if bot_choice == 'rock':
                    await ctx.send(f'I just destroyed you!\nYour choice: {answer}\nMy choice: {bot_choice}')
                elif bot_choice == 'paper':
                    await ctx.send(f'Bruh. I lost.\nYour choice: {answer}\nMy choice: {bot_choice}')
                elif bot_choice == 'scissors':
                    await ctx.send(f"Oh well, we tied.\nYour choice: {answer}\nMy choice: {bot_choice}")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tmyk(self, ctx):
        await ctx.send(file=discord.File('themoreyouknow.png'))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yes(self, ctx):
        await ctx.send(file=discord.File('yes.png'))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def no(self, ctx):
        await ctx.send(file=discord.File('no.png'))

'''
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rps(self, ctx, answer):
        choices = ["rock", "scissors", "paper"]
        bot_choice = random.choice(choices)

        if answer not in choices:
            await ctx.send("Please respond with rock, paper or scissors.")
            return

        start = discord.Embed(title=f"{ctx.author.name}'s Rock Paper Scissors Game", description = "Choose Rock, Paper Or Scissors", color = discord.Colour.blue(), timestamp=ctx.message.created_at)
        
        win = discord.Embed(title="You won!", description = f"I picked {bot_choice}", color = discord.Colour.green(), timestamp=ctx.message.created_at)
        
        out = discord.Embed(title="You didn't respond in time!", description = "Pick faster next time!", color = discord.Colour.red(), timestamp=ctx.message.created_at)
        
        lose = discord.Embed(title="You lost!", description = f"I picked {bot_choice} L", color = discord.Colour.red(), timestamp=ctx.message.created_at)
        
        tie = discord.Embed(title="We tied!", description = f"We both picked {bot_choice}", color = discord.Colour.gold(), timestamp=ctx.message.created_at)            
        
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        try:
            msg = await self.client.wait_for("message", check=check, timeout=20)

        except TimeoutError:
            await m.edit(embed=out)
            return

        else:
            if answer == 'rock':
                if bot_choice == 'rock':
                    await ctx.send(embed=tie)
                elif bot_choice == 'paper':
                    await ctx.send(embed=lose)
                elif bot_choice == 'scissors':
                    await ctx.send(embed=win)

            elif answer == 'paper':
                if bot_choice == 'rock':
                    await ctx.send(embed=win)
                elif bot_choice == 'paper':
                    await ctx.send(embed=tie)
                elif bot_choice == 'scissors':
                    await ctx.send(embed=lose)

            elif answer == 'scissors':
                if bot_choice == 'rock':
                    await ctx.send(embed=lose)
                elif bot_choice == 'paper':
                    await ctx.send(embed=win)
                elif bot_choice == 'scissors':
                    await ctx.send(embed=tie)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def guess(self, ctx):
        number = random.randint(1, 5)
        start = discord.Embed(title=f"{ctx.author}'s Number Guessing Game!", description="Try to guess the number. (1-5)", color=discord.Color.blue(), timestamp=ctx.message.created_at)
        
        win = discord.Embed(title=f"{ctx.author}, You Guessed It Right!", description="You won!", color=discord.Color.green(), timestamp=ctx.message.created_at)
        
        out = discord.Embed(title=f"{ctx.author}, You Didn't Respond On Time", description="Timed Out!", color=discord.Color.gold(), timestamp=ctx.message.created_at)
        
        lose = discord.Embed(title=f"{ctx.author}, You Lost!", description=f"The Number Was {number}", color=discord.Color.red(), timestamp=ctx.message.created_at)
      
        m = await ctx.send(embed=start)
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        try:
            msg = await self.client.wait_for('message', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await m.edit(embed=out)
            return
        else:
            if msg.content == str(number):
                await m.edit(embed=win)
            else:
                await m.edit(embed=lose)
                return
'''         

def setup(client):
    client.add_cog(Game(client))