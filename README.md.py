import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='because yes'):
    slapped = " and ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped {reason}')

bot.run("MTIxNjkyMjkyNDk5MzIxNjUyMg.GN4JL0.6a1Qs8ooAnQGNB26zHaFbPatwzkmRZaaDeVA_k")

