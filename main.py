import discord
from discord.ext import commands
from discord import colour
import time
import os
import random
from requests import get
import json

#=================================================================================

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='w!', intents=intents)

#=================================================================================
#gifs
cry_gifs = ['https://c.tenor.com/q0nNfTktQ7wAAAAC/crying-anime.gif','https://c.tenor.com/0qj0aqZ0nucAAAAC/anya-spy-x-family-anime-anya-crying.gif','https://c.tenor.com/6qJBThILOTcAAAAC/shikimoris-not-just-cute-shikimori.gif','https://c.tenor.com/oOxmN9bPrYcAAAAd/anime-cry-anime-girl.gif','https://c.tenor.com/yn-FwjzdvzMAAAAC/my-dress-up-darling-marin-kitagawa.gif','https://c.tenor.com/hW78kMxAU4kAAAAC/faluchovich-crying-girl.gif','https://c.tenor.com/NHkQKH5CR2kAAAAC/anime-igarashi.gif']
cry_opciones = ['esta llorando','se siente mal y esta llorando','oh no esta llorando']
cry_opciones2 = ['esta llorando junto con ','se siente mal y esta llorando con','llora con ']

happy_gifs = ['https://c.tenor.com/0hgRWZ9VBCAAAAAC/nao-tomori-anime.gif','https://c.tenor.com/-n2jhe7c1MUAAAAC/anime-my-dress-up-darling.gif','https://c.tenor.com/C14UrfBl8OwAAAAC/anime-smile-asai-akira-smile.gif','https://c.tenor.com/bVm05NUoyF0AAAAC/bokuno-hero-academia-izuku.gif','https://c.tenor.com/nPNyng1D6pYAAAAC/chinatsu-yoshikawa-yuruyuri.gif','https://c.tenor.com/A8Xon5cq5sQAAAAC/bell-cranel-dan-machi.gif','https://c.tenor.com/nBWlYPbKxzwAAAAC/anime-happy.gif']
happy_opciones = ['Esta muy feliz','Esta feliz','Esta muy contento!','Esta happy!']
happy_opciones2 = ['Esta feliz con ','Esta muy felix con', 'Esta muy contento junto con']

joya_gifs = ['https://i.pinimg.com/474x/18/d4/ee/18d4eeeea521d00eb1dbd3cbad8fa42a.jpg','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCIR4z17pBKc-jamTx-bpIFE--OB-j3HMB0Q&usqp=CAU','https://c.tenor.com/jLclEBv5WukAAAAd/el-risitas-laughing.gif','https://c.tenor.com/QgTx6fv4IpAAAAAd/el-risitas-juan-joya-borja.gif','https://tenor.com/view/spdegguk-cloudvmink-sponge-bob-sponge-bob-old-gif-25382352']
joya_opciones = ['Esta frezco como lechuga', 'Ta pana', 'Ta joya']
joya_opciones2 = ['Esta pana con','Esta increible junto con','Ta joya con','Se desvelo y esta joya con']
#=================================================================================
#comandos
#https://python.plainenglish.io/send-an-embed-with-a-discord-bot-in-python-61d34c711046 embeds creacion

@bot.command()
async def whox(ctx):
    embed = discord.Embed(title="Lista de comandos", description="**Lista de todos los comandos de whox**", colour=(discord.Colour.random()))
    embed.add_field(name="Comandos utiles", value="Ping " "invite " "say ")
    embed.add_field(name="Comandos Interaccion", value="cry " "happy " "joya ")
    embed.set_footer(text="Creado por: Dasan#7305")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    antes = time.monotonic()
    mensaje = await ctx.send("Mi ping")
    ping1 = (time.monotonic() - antes)*1000
    ping2 = (str(ping1).split('.'))[0]
    await mensaje.edit(content="Mi ping (" + ping2 + "ms)")

@bot.command()
async def invite(ctx):
  await ctx.send("Hola aqui esta mi invitacion gracias por apoyarme uniendome a tu servidor!")
  await ctx.send("|| https://discord.com/api/oauth2/authorize?client_id=972320050537168906&permissions=8&scope=bot ||")

@bot.command()
async def say(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"{text}")

@bot.command(pass_context = True)
async def clear(ctx, number):
  msg = []
  number = int(number)
async for x in Client.logs_from(ctx.message.channel, limit = number):
  msg.append(x)
  await Client.delete_message(msg)

#https://youtu.be/V4ekOOPMg1k
#meme https://youtu.be/xYsosWmdvK4
#=================================================================================
#reaccion

@bot.command()
async def cry(ctx, member: discord.Member = None):
  if member is None:
    await ctx.send(f'{ctx.author.mention} {random.choice(cry_opciones)}')
    await ctx.send(f'{random.choice(cry_gifs)}')
  else:
    await ctx.send(f'{ctx.author.mention} {random.choice(cry_opciones2)} {member.mention}!')
    await ctx.send(f'{random.choice(cry_gifs)}')

@bot.command()
async def happy(ctx, member: discord.Member = None):
  if member is None:
    await ctx.send(f'{ctx.author.mention} {random.choice(happy_opciones)}')
    await ctx.send(f'{random.choice(happy_gifs)}')
  else:
    await ctx.send(f'{ctx.author.mention} {random.choice(happy_opciones2)} {member.mention}!')
    await ctx.send(f'{random.choice(happy_gifs)}')

@bot.command()
async def joya(ctx, member: discord.Member = None):
  if member is None:
    await ctx.send(f'{ctx.author.mention} {random.choice(joya_opciones)}')
    await ctx.send(f'{random.choice(joya_gifs)}')
  else:
    await ctx.send(f'{ctx.author.mention} {random.choice(joya_opciones2)} {member.mention}!')
    await ctx.send(f'{random.choice(joya_gifs)}')
    
#===============================================================================
#eventos y iniciador del bot


@bot.event
async def on_ready():
    total_servers = len(bot.guilds)
    game = discord.Game(f" w!whox | en {total_servers} servidores | Project Whox by Dasan")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(""" ⠀⠀⠀        ⠀⠀⠀⠀    ⢀⡴⠞⢳⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠋⠀⢰⠎⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢆⣤⡞⠃⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢠⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣀⣾⢳⠀⠀⠀⠀⢸⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣀⡤⠴⠊⠉⠀⠀⠈⠳⡀⠀⠀⠘⢎⠢⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
    ⠳⣄⠀⠀⡠⡤⡀⠀⠘⣇⡀⠀⠀⠀⠉⠓⠒⠺⠭⢵⣦⡀⠀⠀⠀
    ⠀⢹⡆⠀⢷⡇⠁⠀⠀⣸⠇⠀⠀⠀⠀⠀⢠⢤⠀⠀⠘⢷⣆⡀⠀
    ⠀⠀⠘⠒⢤⡄⠖⢾⣭⣤⣄⠀⡔⢢⠀⡀⠎⣸⠀⠀⠀⠀⠹⣿⡀
    ⠀⠀⢀⡤⠜⠃⠀⠀⠘⠛⣿⢸⠀⡼⢠⠃⣤⡟⠀⠀⠀⠀⠀⣿⡇
    ⠀⠀⠸⠶⠖⢏⠀⠀⢀⡤⠤⠇⣴⠏⡾⢱⡏⠁⠀⠀⠀⠀⢠⣿⠃
    ⠀⠀⠀⠀⠀⠈⣇⡀⠿⠀⠀⠀⡽⣰⢶⡼⠇⠀⠀⠀⠀⣠⣿⠟⠀
    ⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⡶⠤⣷⣅⡀⠀⠀⠀⣀⡠⢔⠕⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠫⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀
    Estoy Despierdo !""")

bot.run(os.environ['tk'])