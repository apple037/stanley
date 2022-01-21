import unittest
import requests
import re
import json


def inObject(name, maps):
    flag = False
    for i in range(0, len(maps)):
        if str(name) == maps[i]:
            flag = True
    return flag


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = requests.get("https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now")
        self.assertEqual(200,r.status_code)

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
        print(inObject(name,maps[0]["alias"]))


if __name__ == '__main__':
    unittest.main()

