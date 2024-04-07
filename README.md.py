import discord
import random 
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

problem = [
    "Calentamiento global.",
    "Lluvia acida.",
    "Deterioro del oxigeno",
    "Menor prosperidad de vida",
    "Calles sucias y en pesimo estado",
    "Incendios forestales"
]

@bot.command()
async def problemas(ctx):
    consejo = random.choice(problem)
    await ctx.send(consejo)

@bot.command()
async def reciclaje(ctx):
    with open('image/r1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(" escoge el producto con menor envase o envases que puedas reciclar. Separa la basura orgánica de los envases. Separa los envases dependiendo de su material: plásticos, vidrio, aluminio o metal. Coloca cada envase en el contenedor que corresponde.")

@bot.command()
async def contaminacion(ctx):
    with open('image/r2.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Se entiende por contaminación ambiental cuando existe la presencia de sustancias nocivas en el agua, aire o suelo.")

@bot.command()
async def mem1(ctx):
    with open('meme/sus.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('meme/troll.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("tu token xd")

