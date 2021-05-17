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
    comp = datetime(now.year, now.month, now.day, now.hour + hour, now.minute + min, 0)
    diff = comp - now

    #if int(diff.days) >= 0:
    #    scheduler = sched.scheduler(time.time, time.sleep)
    #    scheduler.enter(diff.seconds, 1, def1, ("hoge", ))
    #    scheduler.run()
    #else:
    #    print "do nothing"
    await ctx.send(str(hour)+"時"+str(min)+"分後（"+str(comp)+"）にレイドが始まります！出陣準備...")

    time.sleep(diff.seconds)

    for i in range(times):
        now = datetime.now()
        next = datetime(now.year, now.month, now.day, now.hour + 12, now.minute, 0)
        await ctx.send("レイド攻撃回復。いざ出陣！")
        await ctx.send("次は"+str(next)+"に始まります。")
        time.sleep(12)

@bot.command()
async def close(ctx):
    await bot.close()
    print("レイド終了！お疲れさまでした")

bot.run(token)
