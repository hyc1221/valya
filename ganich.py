import json
from discord import player
import requests
import discord
import glob
import os
import random
from discord.ext import commands
from config import settings
from text import *
from dbhelp import *
bot = commands.Bot(command_prefix = [settings['prefix'], settings['prefix'].upper()], case_insensitive = False)

@bot.event
async def on_ready():
    send_debug(phrases['on_ready'])

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    send_debug(send_hello(author.name))
    await ctx.send(send_hello(author.mention)) # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xff990, title = 'Random fox')
    embed.set_image(url = json_data['link'])
    send_debug('random fox')
    await ctx.send(embed = embed)

@bot.command()
async def cutie(ctx):
    images = glob.glob('img/*jpg')
    image = random.choice(images)
    send_debug(phrases['cutie_debug'])
    await ctx.send(file=discord.File(image))

@bot.command()
async def join(ctx):
    connected = ctx.author.voice
    if (not ctx.voice_client):
        if connected:
            send_debug(f'{ctx.author.voice.channel.id}, {ctx.author.voice.channel.name}')
            await connected.channel.connect()
            await ctx.send(phrases['join_connect'])
        else: 
            send_debug(send_join_error(ctx.author.name))
            await ctx.send(send_join_error(ctx.author.mention))
    else: 
        if (ctx.author.voice.channel.id != ctx.voice_client.channel.id):
            send_debug(f'{ctx.author.voice.channel.id}, {ctx.author.voice.channel.name}')
            await ctx.guild.voice_client.move_to(connected.channel)
            await ctx.send(phrases['join_another'])
        

@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send(phrases['leave'])

@bot.command()
async def ping(ctx):
    send_debug(f'{ctx.author.name}, ping')
    await ctx.send(phrases['ping'], file=discord.File(r'd:/py/valya/img/ping.gif'))

@bot.command()
async def test(ctx):
    connect = True
    connected = ctx.author.voice
    if (not ctx.voice_client):
        if connected:
            send_debug(f'{ctx.author.voice.channel.id}, {ctx.author.voice.channel.name}')
            await connected.channel.connect()
            await ctx.send(phrases['join_connect'])
        else: 
            connect = False
            send_debug(send_join_error(ctx.author.name))
            await ctx.send(send_join_error(ctx.author.mention))
    else:
        if (ctx.author.voice.channel.id != ctx.voice_client.channel.id):
            send_debug(f'{ctx.author.voice.channel.id}, {ctx.author.voice.channel.name}')
            await ctx.voice_client.move_to(connected.channel)
            await ctx.send(phrases['join_another'])
    if (connect):
        while (not ctx.voice_client.is_connected()):
            b = 1
        if (not ctx.voice_client.is_playing()):
            send_debug("test")
            voices = glob.glob('voice/*.ogg')
            source = discord.FFmpegPCMAudio(random.choice(voices))
            player = ctx.voice_client.play(source)
        else:
            await ctx.send(phrases['speak_int'])
        
@bot.command()
async def create(ctx):
    id = ctx.author.id
    name = ctx.author.name
    if (checkId(str(id))):
        send_debug(phrases['user_exists'])
        await ctx.send(phrases['user_exists'])
    else:
        newUser(str(id), name)
        send_debug(send_create_ok(name))
        await ctx.send(send_create_ok(name))

@bot.command()
async def gender(ctx, gender = None):
    id = ctx.author.id
    if (checkId(str(id))):
        if (gender == None):
            gender = checkGender(id)[0]
            if (gender == 'ХЗ'):
                await ctx.send(phrases['gender_not_entered'])
            else:
                await ctx.send(send_gender(gender))
        else:
            gender = gender.lower()
            if (gender == 'мужчина'):
                gender = 'male'
            else:
                if (gender == 'женщина'):
                    gender = 'female'
            if (gender == 'male' or gender == 'female'):
                send_debug(f'{ctx.author.name} changed gender to {gender}')
                if (gender == 'male' or gender == 'мужчина'):
                    await ctx.send(phrases['gender_male'])
                else:
                    await ctx.send(phrases['gender_female'])
                setGender(id, gender)
            else:
                send_debug(ctx.author.name + ' ' + phrases['gender_error'])
                await ctx.send(phrases['gender_error'])
    else:
        send_debug(ctx.author.name + ' ' + phrases['user_unknown'])
        await ctx.send(phrases['user_unknown'])

@bot.command()
async def info(ctx):
    id = ctx.author.id
    if (checkId(str(id))):
        result = checkinfo(id)
        send_debug(f'{ctx.author.name} info')
        await ctx.send(send_info(result))
    else:
        await ctx.send(phrases['user_unknown'])


bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена