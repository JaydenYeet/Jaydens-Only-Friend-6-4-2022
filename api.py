import discord
import requests
from discord.ext import commands
import aiohttp
import json

class Api(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Api Cog Initiated\n----------------------------")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def meme(self, ctx):
        URL = f"https://meme-api.herokuapp.com/gimme"

        def check_valid_status_code(request):
            if request.status_code == 200:
                return request.json()

            return False

        def get_meme():
            request = requests.get(URL)
            data = check_valid_status_code(request)

            return data

        memee = get_meme()
        if not memee:
            await ctx.channel.send("Couldn't get meme from API. Try again later.")

        else:
            caption = memee["title"]
            img = memee["url"]
            nsfw = memee["nsfw"]
            spoiler = memee["spoiler"]
            if nsfw == "true" or spoiler == "true":
                embed = discord.Embed(
                    timestamp=ctx.message.created_at,
                    title=f"||{caption}||",
                    color=0xFF0000,
                )
                embed.set_image(url=f"SPOILER_{img}")
                embed.set_footer(
                    text=f"Requested By: {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar.url}",
                )
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    timestamp=ctx.message.created_at, title=f"{caption}", color=discord.Color.random()
                )
                embed.set_image(url=f"{img}")
                embed.set_footer(
                    text=f"Requested By: {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar.url}",
                )
                await ctx.send(embed=embed)
                
    @commands.command(aliases=["insult"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def roast(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://insult.mattbas.org/api/insult"
                ) as response:
                    insult = await response.text()
                    embed = discord.Embed(
                        timestamp=ctx.message.created_at,
                        title=f"{member.name}",
                        description=f"{insult}",
                        color=discord.Colour.random()
                    )
                    await ctx.send(embed=embed)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://insult.mattbas.org/api/insult"
                ) as response:
                    insult = await response.text()
                    embed = discord.Embed(
                        timestamp=ctx.message.created_at,
                        title=f"{member.name}",
                        description=f"{insult}",
                        color=discord.Colour.random()
                    )
                    await ctx.send(embed=embed)
                    
    @commands.command(name="covid", help="Shows the countries Covid infomation")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def covid(self, ctx, *, countryName = None):
        try:
            if countryName is None:
                await ctx.send("You have to input a name of a country!")

            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                embed2 = discord.Embed(title=f"**Covid-19 Status Of {country}**!", description="This Information Isn't Always Updated, Hence It May Not Be Accurate!", colour=discord.Colour.random(), timestamp=ctx.message.created_at)
                embed2.add_field(name="**Total Cases**", value=totalCases, inline=True)
                embed2.add_field(name="**Today Cases**", value=todayCases, inline=True)
                embed2.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
                embed2.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
                embed2.add_field(name="**Recovered**", value=recovered, inline=True)
                embed2.add_field(name="**Active**", value=active, inline=True)
                embed2.add_field(name="**Critical**", value=critical, inline=True)
                embed2.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
                embed2.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
                embed2.add_field(name="**Total Tests**", value=totalTests, inline=True)
                embed2.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)
                embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
                await ctx.send(embed=embed2)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again!", colour=discord.Colour.random(), timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)

def setup(client):
    client.add_cog(Api(client))