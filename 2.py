import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def wads (ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=dQw4w9WgXcQ {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTUwMjY4MzM4MDU1MzIyNDIwMg.GS0_tP.3JE0T8eUoGHw2Xlhz1q-4jBHse042A7ebNACIE")