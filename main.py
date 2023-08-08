# 導入Discord.py
import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
discord_api_key = os.getenv("DISCORD_API_KEY")

# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='#', intents=intents)


# 調用event函式庫
@bot.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', bot.user)
    game = discord.Game('機油好好喝')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)


# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    count = 0
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded {filename[:-3]}.")
            count += 1
    print(f"Loaded {count} cogs.")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(discord_api_key)


# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())
