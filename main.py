# 導入Discord.py
import discord
import requests
import json
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
            if " " in order:
                tmp2 = order.split(" ")
                order = tmp2[0]
                arg = tmp2[1]
            if order == "greet":
                await message.channel.send("Greeting")
            elif order == "fuck":
                msg = "{0} minds your own business".format(str(message.author))
                await message.channel.send(msg)
                sta = discord.Game('fuck')
                await client.change_presence(status=discord.Status.idle, activity=sta)
            elif order == "find":
                msg = get_currency_price(arg)
                await message.channel.send(msg)
            else:
                await message.channel.send("Beep Beep Beep?")


def get_currency_price(name):
    res = ""
    if name == "ex" or name == "EX" or name == "崇高石":
        name = "Exalted Orb"
    elif name == "alch" or name == "ALCH" or name == "點金石":
        name = "Orb of Alchemy"
    else:
        if name != "all":
            res = "what are you looking for? ouo"
    r = requests.get('https://poe.ninja/api/data/CurrencyOverview?league=Scourge&type=Currency&language=en')
    j = r.json()
    lines = j["lines"]
    for x in range(0, len(lines)):
        if name == "all":
            c = str(lines[x]['currencyTypeName']) + ": " + str(lines[x]['chaosEquivalent'])
            res = res + "\n" + json.dumps(c)
        elif name == "Exalted Orb":
            if lines[x]['currencyTypeName'] == "Exalted Orb":
                res = lines[x]['chaosEquivalent']
        elif name == "Orb of Alchemy":
            if lines[x]['currencyTypeName'] == "Orb of Alchemy":
                res = lines[x]['chaosEquivalent']
    return res


client.run('OTMxNDU4MTA5Njk0Njc3MDI0.YeEt9w.Zp6KUJaSJxKzYShVBy8R4-7HM5U')
