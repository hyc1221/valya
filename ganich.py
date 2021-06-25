import json
import requests
import discord
import glob
import os
import random
from discord.ext import commands
from config import settings
from text import phrases, send_hello, send_join_error

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    print(phrases['on_ready'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    print(send_hello(author.name))
    await ctx.send(send_hello(author.mention)) # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff990, title = 'Random fox')
    embed.set_image(url = json_data['link'])
    print('random fox')
    await ctx.send(embed = embed)

@bot.command()
async def cutie(ctx):
    images = glob.glob('img/*jpg')
    image = random.choice(images)
    print(phrases['cutie_debug'])
    await ctx.send(file=discord.File(image))

@bot.command()
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        print(ctx.author.voice.channel.id, ctx.author.voice.channel.name)
        await connected.channel.connect()
        await ctx.send(phrases['join_connect'])
    else: 
        print(send_join_error(ctx.author.name))
        await ctx.send(send_join_error(ctx.author.mention))

@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(phrases['leave'])

@bot.command()
async def ping(ctx):
    print(ctx.author.name, 'ping')
    await ctx.send(phrases['ping'], file=discord.File(r'd:/py/valya/img/ping.gif'))


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена