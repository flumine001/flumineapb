import math
import discord
from discord.ext import commands
TOKEN = 'OTI5NTE2Mzk2Njg0MTIwMDY1.Ydodmg.5VJGOeINUyP95Iq6C2YgDP8e0g4'
bot = commands.Bot(command_prefix='!')
d= 166461.6
bot.remove_command('help')
@bot.command(name="sens")
async def sens_cm(ctx, x: float,cm:str, y: float,dpi):
  if cm=="ingame":
       await ctx.send(f'>>> {d/(x*y)} cm')
  elif cm=="cm":
       await ctx.send(f'>>> {d/(x*y)} ingame')
  else:
       await ctx.send("Invalid argument")
@bot.command(name="help")
async def help(ctx):
    await ctx.send(">>> !sens n cm m dpi чтобы узнать значение в игре, где n сантиметры, m ваш dpi.\nЧтобы узнать вашу текущую сенсу в сантиметрах, нужно прописать !sens n ingame m dpi где n значение сенсы в игре m ваш текущий dpi.\ncm dpi и ingame обязательно нужно прописывать после ваших значений." )

@sens_cm.error
async def sens_cm_error(ctx, error):
  if isinstance(error, commands.BadArgument):
        await ctx.send('>>> Ошибка. Пример комманды "!sens 40 cm 800 dpi" Обязательно нужно прописать cm и dpi после ваших значений и обязательно должен быть пробел между ними')
bot.run(TOKEN)
