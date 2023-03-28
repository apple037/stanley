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


def getAnswer(question, api_key):
    openai.api_key = api_key
    temperature = random.randint(0, 100) / 100
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=temperature,
        messages=[
            {'role': 'user', 'content': question}
        ],
        stream=True
    )
    # create variables to collect the stream of chunks
    collected_chunks = []
    collected_messages = []

    for chunk in response:
        collected_chunks.append(chunk)  # save the event response
        chunk_message = chunk['choices'][0]['delta']  # extract the message
        collected_messages.append(chunk_message)  # save the message

    full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
    print(f"Full conversation received: {full_reply_content}")
    print('Temperature: ' + str(temperature))
    # print('Generated answer: ' + full_reply_content)
    return full_reply_content

