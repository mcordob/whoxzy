import discord
from discord.ext import commands
from discord import colour
import time
import os
import random

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
#=================================================================================
#comandos

@bot.command()
async def whox(ctx):
    embed = discord.Embed(title="Lista de comandos", )
    embed.add_field(name="Comandos utiles", value="Ping " "invite ")
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

#=================================================================================
#reaccion

@bot.command()
async def cry(ctx):
  embed = discord.Embed(description=f"{ctx.author.mention} {random.choice(cry_opciones)}", colour=(discord.Colour.random()))
  embed.set_image(url=(random.choice(cry_gifs)))
  await ctx.send(embed=embed)

@bot.command()
async def feliz(ctx):
  embed = discord.Embed(description=f"{ctx.author.mention} {random.choice(happy_opciones)}", colour=(discord.Colour.random()))
  embed.set_image(url=(random.choice(happy_gifs)))
  await ctx.send(embed=embed)

@bot.command()
async def joya(ctx):
    await ctx.send("Toy joya")
    await ctx.send('https://tenor.com/view/spdegguk-cloudvmink-sponge-bob-sponge-bob-old-gif-25382352')

#===============================================================================
#eventos y iniciador del bot

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Project Whox by Dasan w!whox"))
    print(""" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⢳⠀⠀⠀⠀⠀
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

bot.run(os.environ['token'])