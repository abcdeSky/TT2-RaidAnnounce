import discord
from discord.ext import commands, tasks
import os
import traceback
import random
from datetime import datetime, timedelta
import sched
import time

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
async def raidstart(ctx, times : int, hour : int, min : int, content='repeating...'):
    """Repeats a message multiple times."""
    now = datetime.now()
    now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
    now = now + timedelta(hours=9)
    minutes = hour*60 + min
    comp = now + timedelta(minutes=minutes)
    diff = comp - now

    await ctx.send(str(hour)+"時"+str(min)+"分後（__"+comp.strftime('%m月%d日 %H:%M')+"__）にレイドが始まります！出陣準備...")

    time.sleep(diff.seconds)

    for i in range(times):
        now = datetime.now()
        now = datetime(now.year, now.month, now.day, now.hour, now.minute, 0)
        now = now + timedelta(hours=9)
        next = now + timedelta(hours=12)
        await ctx.send("レイド第"+i+1+"戦。いざ出陣！\n"+"次は"+next.strftime('%m月%d日 %H:%M')+"に始まります。")
        time.sleep(12)

@bot.command()
async def close(ctx):
    await ctx.send("レイド終了！お疲れさまでした")
    await bot.close()


bot.run(token)
