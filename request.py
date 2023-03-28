import os
from dotenv import load_dotenv
import unittest
import requests
import re
import json
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def inObject(name, maps):
    flag = False
    for i in range(0, len(maps)):
        if str(name) == maps[i]:
            flag = True
    return flag


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now")
        self.assertEqual(200, r.status_code)

    def testTime(self):
        r = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now")
        x = re.sub(r"\D", " ", str(r.content))
        self.assertTrue(int(x) > 1642672605)
        # print(x)

    def test_upper(self):
        self.assertEqual('ouo'.upper(), 'OUO')  # add assertion here

    def testGet(self):
        name = "ex"
        f = open('mapping.json', encoding='utf-8')
        data = json.load(f)
        maps = data["mapping"]
        print(inObject(name, maps[0]["alias"]))

    def testPost(self):
        completion = openai.Completion.create(
            engine='text-davinci-003',
            prompt='Describe Elon Musk in three words',
            max_tokens=20,
            temperature=0.25,
        )
        reply_msg = completion["choices"][0]["text"].replace('\n', '')
        print(reply_msg)

    def testChatPost(self):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature=0,
            messages=[
                {'role': 'user', 'content': "How to buy a car"}
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


    def testParse(self):
        order = '#ASK Describe Elon Musk in Three words'
        if " " in order:
            tmp2 = order.split(" ")
            order = tmp2[0]
            arg = tmp2[1]
            multiArg = ''
            for i in range(1, len(tmp2)):
                multiArg = multiArg + ' ' + tmp2[i]


if __name__ == '__main__':
    unittest.main()
