import unittest
import requests
import re
import json


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
        r = requests.get('https://poe.ninja/api/data/CurrencyOverview?league=Scourge&type=Currency&language=en')
        j = r.json()
        lines = j["lines"]
        res = ""
        for x in range(0, len(lines)):
            # if lines[x]['currencyTypeName'] == "Exalted Orb":
            #     c = {"currency": lines[x]['currencyTypeName'],
            #          "chaosEquivalent": lines[x]['chaosEquivalent']}
            #     res = json.dumps(c)
            #     print(res)
            c = str(lines[x]['currencyTypeName']) + ":" + str(lines[x]['chaosEquivalent'])
            res = res + "\n" + json.dumps(c)
        print(res)


if __name__ == '__main__':
    unittest.main()

