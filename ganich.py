import json
import requests
import discord
import glob
import os
import random
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    print('я не сплю')

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    print(f'Уважаемый, {author.name}. Хочу вас приветствовать и поприветствовать.')
    await ctx.send(f'Уважаемый, {author.mention}. Хочу вас приветствовать и поприветствовать.') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff990, title = 'Random fox')
    embed.set_image(url = json_data['link'])
    print('random fox')
    await ctx.send(embed = embed)

@bot.command()
async def cutie(ctx):
    images = glob.glob('img/*jpg')
    image = random.choice(images)
    print('random ganich')
    await ctx.send(file=discord.File(image))

@bot.command()
async def join(ctx):
    connected = ctx.author.voice
    if connected:
        print(ctx.author.voice.channel.id, ctx.author.voice.channel.name)
        await connected.channel.connect()
    else: 
        print(f'Уважаемый {ctx.author.name}, сначала сам зайди, потом зови. (ты никто и звать тебя никта)')
        await ctx.send(f'Уважаемый {ctx.author.mention}, сначала сам зайди, потом зови. (ты никто и звать тебя никта)')

@bot.command()
async def ping(ctx):
    print(ctx.author.name, 'ping')
    await ctx.send('Руки убрал, РУКИ УБРАЛ Я СКАЗАЛ! Трогать будешь свою Палину бл*ть.', file=discord.File(r'd:/py/valya/img/ping.gif'))


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена