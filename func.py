import requests
import json
import openai
import random


def get_currency_price(name):
    f = open('mapping.json', encoding='utf-8')
    data = json.load(f)
    res = ""
    maps = data["mapping"]
    match = False
    for i in range(0, len(maps)):
        if name == maps[i]["name"] or inObject(name, maps[i]["alias"]):
            name = maps[i]["name"]
            match = True
    if not match:
        name = "all"
    r = requests.get('https://poe.ninja/api/data/CurrencyOverview?league=Scourge&type=Currency&language=en')
    j = r.json()
    lines = j["lines"]
    for x in range(0, len(lines)):
        if name == "all":
            c = str(lines[x]['currencyTypeName']) + ": " + str(lines[x]['chaosEquivalent'])
            res = res + "\n" + json.dumps(c)
        else:
            if lines[x]['currencyTypeName'] == name:
                res = lines[x]['chaosEquivalent']
    return res


def get_help():
    res = "#price(#f) {currency_name}: 查詢通貨價格"
    res = res + "\n" + "#item {item_name}: 查詢物品最多上架價格(還沒做)"
    return res


def inObject(name, maps):
    flag = False
    for i in range(0, len(maps)):
        if str(name) == maps[i]:
            flag = True
    return flag


def getMap():
    f = open('mapping.json', encoding='utf-8')
    data = json.load(f)
    res = ""
    maps = data["mapping"]
    for i in range(0, len(maps)):
        if i == 0:
            res = str(maps[i]["name"]) + " : " + str(maps[i]["alias"])
        else:
            res = res + "\n" + str(maps[i]["name"]) + " : " + str(maps[i]["alias"])
    return res


def getAnswer(question):
    openai.api_key = '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'
    temperature = random.randint(0, 100) / 100
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=200,
        temperature=temperature,
    )
    reply_msg = completion["choices"][0]["text"].replace('\n', ' ').strip()
    if reply_msg.startswith("."):
        reply_msg = reply_msg[1::]
    print('Temperature: ' + str(temperature))
    print('Generated answer: ' + reply_msg)
    return reply_msg

