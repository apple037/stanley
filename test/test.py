import base64
import json
import os
import random
import unittest
from io import BytesIO

import openai
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
sd_url = os.getenv("STABLE_DIFFUSION_URL")


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
        x = r.sub(r"\D", " ", str(r.content))
        self.assertTrue(int(x) > 1642672605)
        # print(x)

    def test_upper(self):
        self.assertEqual('ouo'.upper(), 'OUO')  # add assertion here

    def testGet(self):
        name = "ex"
        f = open('../resource/mapping.json', encoding='utf-8')
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
        temperature = random.randint(0, 100) / 100
        print('temperature: ', temperature)
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature=temperature,
            messages=[
                {'role': 'system', 'content': "You are a sexy girl and like to say something seductive"},
                {'role': 'user', 'content': "Good morning"},
                {'role': 'assistant', 'content': "It's morning time. Say something cute to greet and remind to eat "
                                                 "breakfast"},
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

    def testImgGeneration(self):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        false = False
        true = True
        request_body = {
            "enable_hr": false,
            "denoising_strength": 0,
            "firstphase_width": 0,
            "firstphase_height": 0,
            "hr_scale": 2,
            "hr_upscaler": "",
            "hr_second_pass_steps": 0,
            "hr_resize_x": 0,
            "hr_resize_y": 0,
            "styles": [],
            "seed": -1,
            "subseed": -1,
            "subseed_strength": 0,
            "seed_resize_from_h": -1,
            "seed_resize_from_w": -1,
            "sampler_name": "",
            "batch_size": 1,
            "n_iter": 1,
            "steps": 50,
            "cfg_scale": 7,
            "width": 512,
            "height": 512,
            "restore_faces": false,
            "tiling": false,
            "do_not_save_samples": false,
            "do_not_save_grid": false,
            "negative_prompt": "",
            "eta": 0,
            "s_churn": 0,
            "s_tmax": 0,
            "s_tmin": 0,
            "s_noise": 1,
            "override_settings": {},
            "override_settings_restore_afterwards": true,
            "script_args": [],
            "sampler_index": "Euler",
            "script_name": "",
            "send_images": true,
            "save_images": false,
            "alwayson_scripts": {},
            "prompt": "a dog walking at street"
        }
        txt2img_url = sd_url + "/sdapi/v1/txt2img"
        print(txt2img_url)
        response = requests.post(txt2img_url, headers=headers, data=json.dumps(request_body))
        if response.status_code == 200:
            images = response.json()['images'][0]
            byte_data = base64.b64decode(images)
            image_data = BytesIO(byte_data)
            img = Image.open(image_data)
            img.show("030")

    def test_random_cat(self):
        response = requests.get('https://cataas.com/cat')
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.show("cat")
        else:
            return None


if __name__ == '__main__':
    unittest.main()
