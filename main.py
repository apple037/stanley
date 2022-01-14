# 導入Discord.py
import discord

# client是我們與Discord連結的橋樑
client = discord.Client()


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('努力學習py中')
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
            if order == "greet":
                await message.channel.send("Greeting")
            elif order == "fuck":
                await message.channel.send("Busy")
                sta = discord.Game('fuck')
                await client.change_presence(status=discord.Status.idle, activity=sta)
            else:
                await message.channel.send("Beep Beep Beep?")


client.run('OTMxNDU4MTA5Njk0Njc3MDI0.YeEt9w.Zp6KUJaSJxKzYShVBy8R4-7HM5U')
