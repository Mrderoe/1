import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

def combin(O2, C):
    result = O2 + C
    return result

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def burning(ctx, O2: int, C: int):
    CO2 = combin(O2, C)
    await ctx.send(f'after amount of burned things, will be {CO2}')

@bot.command(name='поглотить_CO2')
async def absorb_co2(ctx, treesam: int, hours: int):
    removeco2 = 10 
    removedatall = calculate_co2_absorption(treesam, hours, removeco2)
    await ctx.send(f'{treesam} tree(s) by {hours} hours remove kinda {removedatall} CO2.')

def calculate_co2_absorption(treesam, hours, removeco2):
    removedatall = treesam * hours * removeco2
    return removedatall



bot.run('9xZOczQYO7ov1jn9qjO0tMSvVRm6JwvL')