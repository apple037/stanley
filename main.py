# 導入Discord.py
import os
from dotenv import load_dotenv
import discord
import func

load_dotenv()
discord_api_key = os.getenv("DISCORD_API_KEY")
open_api_key = os.getenv("OPENAI_API_KEY")

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


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
                multiArg = ''
                for i in range(1, len(tmp2)):
                    multiArg = multiArg + ' ' + tmp2[i]
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
                await message.channel.send(func.getMap())
            elif str(order).upper() == "ASK":
                msg = func.getAnswer(multiArg, open_api_key)
                await message.channel.send("Hi " + message.author.mention + " Here is my reply: \n" + msg)
            else:
                await message.channel.send("#help or #Help for usage")

client.run(discord_api_key)
