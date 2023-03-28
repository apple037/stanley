# 導入Discord.py
import io
import os

import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

import func

load_dotenv()
discord_api_key = os.getenv("DISCORD_API_KEY")
open_api_key = os.getenv("OPENAI_API_KEY")
sd_url = os.getenv("STABLE_DIFFUSION_URL")

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('機油好好喝')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)


@client.event
# 當有訊息時
async def on_message(message):
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    # 如果以「#」開頭
    if message.content.startswith('#'):
        # 分割訊息成兩份
        tmp = message.content.split("#")
        # 如果分割後串列長度只有1
        if len(tmp) == 0:
            await message.channel.send("逼逼逼？")
        else:
            order = tmp[1]
            if " " in order:
                tmp2 = order.split(" ")
                order = tmp2[0]
                arg = tmp2[1]
                multi_arg = ''
                for i in range(1, len(tmp2)):
                    multi_arg = multi_arg + ' ' + tmp2[i]
            if order == "greet":
                await message.channel.send("Greeting")
            elif order == "fuck":
                msg = "{0} minds your own business".format(str(message.author))
                await message.channel.send(msg)
                sta = discord.Game('fuck')
                await client.change_presence(status=discord.Status.idle, activity=sta)
            elif str(order).upper() == "PRICE" or str(order).upper() == "F":
                msg = func.get_currency_price(arg)
                await message.channel.send(msg)
            elif str(order).upper() == "HELP":
                await message.channel.send(func.get_help())
            elif str(order).upper() == "MAP":
                await message.channel.send(func.get_map())
            elif str(order).upper() == "ASK":
                msg = func.get_answer(multi_arg, open_api_key)
                await message.channel.send("Hi " + message.author.mention + " Here is my reply: \n" + msg)
            elif str(order).upper() == "INFO":
                info = await func.sd_info(sd_url)
                await message.channel.send("Hi " + message.author.mention + " " + info)
            elif str(order).upper() == "IMAGE":
                await message.channel.send("Image generating ..." + message.author.mention + " please wait patiently!")
                img = await func.generate_image(multi_arg, sd_url)
                img_buffer = io.BytesIO()
                img.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                await message.channel.send("Hi " + message.author.mention + "The image generated with the "
                                                                            "corresponding prompts (" +
                                           multi_arg + ") is below:",
                                           file=discord.File(fp=img_buffer, filename='image.png'))
            else:
                await message.channel.send("#help or #Help for usage")


client.run(discord_api_key)
