import discord
from discord.ext import commands, tasks
from gtts import gTTS
from discord import FFmpegPCMAudio
import os
import speech_recognition as sr
import asyncio

intents = discord.Intents.all()
intents.messages = True
intents.voice_states = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command()
async def kelkk(ctx):
    if ctx.voice_client is None or ctx.voice_client.channel is None:
        await ctx.send(f"{ctx.author.mention} Inne voice channel kettada poori mone")
        return

    print("Worked")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio_data = recognizer.listen(source)
            text = recognizer.recognize_google(audio_data)
            print(audio_data)

            if "hello" in text:
                print("Success")
                await voice(ctx)

        except sr.UnknownValueError:
            print("Error")

@bot.command()
async def ker(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        await ctx.send("Voice channel kerada myraa")
        return
    
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
    
    voice_client = ctx.voice_client
    channel = ctx.author.voice.channel

    vc = await channel.connect()
    await ctx.send("Keri")

@bot.command()
async def hi(ctx):
    if ctx.voice_client is None or ctx.voice_client.channel is None:
        await ctx.send(f"{ctx.author.mention} Inne voice channel kettada poori mone")
        return

    path = '/home/unknown/Downloads/hello.mp3'

    if os.path.exists(path):
        speech = FFmpegPCMAudio(path)
        ctx.voice_client.play(speech)

@bot.command()
async def voice(ctx):
    print("Running")
    path = '/home/unknown/Downloads/How.mp3'

    speech = FFmpegPCMAudio(path)
    ctx.voice_client.play(speech)

@bot.command()
async def ara(ctx):
    await ctx.send(f"{ctx.author.mention} Njan {bot.user.name}")

@bot.command()
async def poda(ctx):
    if ctx.voice_client is None or ctx.voice_client.channel is None:
        await ctx.send(f"{ctx.author.mention} Njan poyida kunne")
        return
    
    await ctx.send("Ok bei")
    await ctx.voice_client.disconnect()

bot.run('MTIwNDQ3NTA5NzIxODQyMDc5Ng.G_5cB2.J1JwaBZmqT_TDm5uZfiPOWCoI3B_1aJqkJ0GPc')
