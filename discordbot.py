import discord
from discord.ext import commands
import os
import traceback
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    print(times)
    print(type(times))
    #for i in range(times):
    await bot.send(content)


bot.run(token)
