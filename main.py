# 導入Discord.py
import io
import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

from script import func, common

load_dotenv()
discord_api_key = os.getenv("DISCORD_API_KEY")
open_api_key = os.getenv("OPENAI_API_KEY")
sd_url = os.getenv("STABLE_DIFFUSION_URL")

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='#', intents=intents)


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('機油好好喝')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.command()
async def greet(ctx):
    await ctx.channel.send("Greeting")


@client.command()
async def fuck(ctx):
    msg = "{0} minds your own business".format(str(ctx.author))
    await ctx.channel.send(msg)
    sta = discord.Game('fuck')
    await client.change_presence(status=discord.Status.idle, activity=sta)


@client.command()
async def price(ctx, arg):
    msg = func.get_currency_price(arg)
    await ctx.channel.send(msg)


@client.command()
async def mapping(ctx):
    await ctx.channel.send(func.get_map())


@client.command(
    help="Use openAI chatGPT 3.5 api to achieve the chat completion"
)
async def ask(ctx, *args):
    prompt = ''
    for arg in args:
        prompt = prompt + ' ' + arg
    prompt = prompt.lstrip()
    print(prompt)
    msg = func.get_answer(prompt, open_api_key)
    await ctx.channel.send("Hi " + ctx.author.mention + " Here is my reply: \n" + msg)


@client.command()
async def info(ctx):
    sd_info = await func.sd_info(sd_url)
    await ctx.channel.send("Hi " + ctx.author.mention + " " + sd_info)


@client.command()
async def image(ctx, *args):
    prompt = ''
    for arg in args:
        prompt = prompt + ' ' + arg
    prompt = prompt.lstrip()
    # print(prompt)
    await ctx.channel.send("Image generating ..." + ctx.author.mention + " please wait patiently!")
    img = await func.generate_image(prompt, sd_url)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    await ctx.channel.send("Hi " + ctx.author.mention + "The image generated with the "
                                                        "corresponding prompts (" +
                           prompt + ") is below:",
                           file=discord.File(fp=img_buffer, filename='image.png'))


@client.command(help="Use BLIP2 to perform image to text conversion")
async def img2txt(ctx, arg):
    # 檢查是否為有效的url
    if not common.is_valid_url(arg):
        await ctx.channel.send(ctx.author.mention + " the input: " + arg + " is not a valid url")
    await ctx.channel.send("Image to text converting ..." + ctx.author.mention + " please wait patiently!")
    parsed_text = await func.img2txt(arg)
    await ctx.channel.send("Hi " + ctx.author.mention + "The text generated with the "
                                                        "corresponding image (" +
                           arg + ") is below: " + "\n" + parsed_text)


# Get a random cat image
@client.command(help="Get a random cat image")
async def cat(ctx):
    await ctx.channel.send("Cat image generating ..." + ctx.author.mention + " please wait patiently!")
    img = await func.get_cat_image()
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    await ctx.channel.send("Hi " + ctx.author.mention + "The cat image generated is below:",
                           file=discord.File(fp=img_buffer, filename='cat.png'))


@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
    await ctx.send(file=discord.File(fp='./resource/no.jpeg', filename='no.jpeg'))


client.run(discord_api_key)
