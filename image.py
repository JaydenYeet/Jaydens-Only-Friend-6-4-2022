import discord
from discord.ext import commands

class Image(commands.Cog, name="image"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Image cog loaded successfully \n----------------------------")

    @commands.command(
        help="Generates an image with epic triggered filter!",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='triggered [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def triggered(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/triggered?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates an image with epic GTA 5 wasted filter!",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='wasted [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def wasted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/wasted?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates a change my mind meme with provided text!",
        description="`text` (Optional): The text to use on image.",
        brief='image/filters',
        usage='changemymind <text>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def changemymind(self, ctx, *, text=None):
        if text == None:
            await ctx.send(" You need to provide the text.")
            return

        text = text.replace(' ', '%20')
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/changemymind?text="+text)
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates an image with blurry filter!",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='blur [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def blur(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/blur?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Sends someone to jail lol.",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='jail [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def jail(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author        
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/jail?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates an image with facepalm filter.",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='facepalm [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def facepalm(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/facepalm?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates an image with trash filter.",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='trash [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def trash(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.toxy.ga/api/trash?avatar={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Hands over a gun to a person's avatar.",
        description="`user` (Optional): The person whose avatar should be used, defaults to command's user.",
        brief='image/filters',
        usage='gun [user]'
        )

    @commands.cooldown(1, 3, commands.BucketType.user)

    async def gun(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/gun?image={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates a two button meme.",
        description="`text1` (Required): The first text.\n`text2` (Required): The second text.",
        brief='image/filters',
        usage='twobuttons <text1> ;; <text2>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def twobuttons(self, ctx, *, text=None):
        if text == None:
            await ctx.send(Emoji.info+" You need to specify the text like: `TEXT 1 HERE ;; TEXT 2 HERE`.")
            return

        text = text.split(";;")
        t1 = text[0]
        t1 = t1.replace(' ', '%20')
        t2 = text[1]
        t2 = t2.replace(' ', '%20')
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/two-buttons?button1={t1}&button2={t2}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates a drake meme.",
        description="`text1` (Required): The first text.\n`text2` (Required): The second text.",
        brief='image/filters',
        usage='drake <text1> ;; <text2>'
        )
    
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def drake(self, ctx, *, text=None):
        if text == None:
            await ctx.send(Emoji.info+" You need to specify the text like: `TEXT 1 HERE ;; TEXT 2 HERE`.")
            return

        text = text.split(";;")
        t1 = text[0]
        t1 = t1.replace(' ', '%20')
        t2 = text[1]
        t2 = t2.replace(' ', '%20')
        
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/drake?top={t1}&bottom={t2}")
        await ctx.send(embed=embed)

    @commands.command(
        help="This one is for simps.",
        description="`user` (Optional): The simp whose avatar should be used, If not provided, you will be the target so be careful lol.",
        brief='image/filters',
        usage='simp [user]'
        )

    @commands.cooldown(1, 3, commands.BucketType.user)

    async def simp(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/simp?image={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates a tuxedo pooh image.",
        description="`text1` (Required): The first text.\n`text2` (Required): The second text.",
        brief='image/filters',
        usage='pooh <text1> ;; <text2>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def pooh(self, ctx, *, text=None):
        if text == None:
            await ctx.send(Emoji.info+" You need to specify the text like: `TEXT 1 HERE ;; TEXT 2 HERE`.")
            return

        text = text.split(";;")
        t1 = text[0]
        t1 = t1.replace(' ', '%20')
        t2 = text[1]
        t2 = t2.replace(' ', '%20')
        
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/tuxedo-pooh?normal={t1}&tuxedo={t2}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Generates a panik meme.",
        description="`text1` (Required): The first text.\n`text2` (Required): The second text.\n`text3` (Required): The third text.",
        brief='image/filters',
        usage='panik <text1> ;; <text2> ;; <text3>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def panik(self, ctx, *, text=None):
        if text == None:
            await ctx.send(Emoji.info+" You need to specify the text like: `TEXT 1 HERE ;; TEXT 2 HERE ;; TEXT 3 HERE`.")
            return

        text = text.split(";;")
        t1 = text[0]
        t1 = t1.replace(' ', '%20')
        t2 = text[1]
        t2 = t2.replace(' ', '%20')
        t3 = text[2]
        t3 = t3.replace(' ', '%20')
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/panik?panik={t1}&kalm={t2}&panik2={t3}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Puts on \"Everyone liked that\" filter on an image.",
        description="`image` (Required): The image to apply filter on.",
        brief='image/filters',
        usage='like <image>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def like(self, ctx):
        if len(ctx.message.attachments) == 0:
            await ctx.send(Emoji.info+" You need to attach an image in order for this command to function.")
            return

        image= ctx.message.attachments[0]

        if not image.content_type.startswith('image/'):
            await ctx.send(Emoji.info+" The message attachement has to be an image!")
            return
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/like?image={image.url}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Puts on \"Everyone disliked that\" filter on an image.",
        description="`image` (Required): The image to apply filter on.",
        brief='image/filters',
        usage='dislike <image>'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def dislike(self, ctx):
        if len(ctx.message.attachments) == 0:
            await ctx.send(Emoji.info+" You need to attach an image in order for this command to function.")
            return

        image= ctx.message.attachments[0]

        if not image.content_type.startswith('image/'):
            await ctx.send(Emoji.info+" The message attachement has to be an image!")
            return    
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/dislike?image={image.url}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Puts on \"beautiful painting\" filter on an image.",
        description="`image` (Required): The image to apply filter on.",
        brief='image/filters',
        usage='beautiful <image>'
        )

    @commands.cooldown(1, 3, commands.BucketType.user)

    async def beautiful(self, ctx):
        if len(ctx.message.attachments) == 0:
            await ctx.send(Emoji.info+" You need to attach an image in order for this command to function.")
            return

        image= ctx.message.attachments[0]

        if not image.content_type.startswith('image/'):
            await ctx.send(Emoji.info+" The message attachement has to be an image!")
            return
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/beautiful?image={image.url}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Deletes the trash.",
        description="`user` (Optional): The user's whose avatar should be memified.",
        brief='image/filters',
        usage='delete [user]'
        )

    @commands.cooldown(1, 3, commands.BucketType.user)

    async def delete(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/delete?image={user.avatar}")
        await ctx.send(embed=embed)

    @commands.command(
        help="Applies the communist filter on user's avatar.",
        description="`user` (Optional): The user's whose avatar should be memified.",
        brief='image/filters',
        usage='communist [user]'
        )
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def communist(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        
        embed = discord.Embed(color=discord.Colour.random())
        embed.set_image(url=f"https://api.devs-hub.xyz/communist?image={user.avatar}")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Image(client))