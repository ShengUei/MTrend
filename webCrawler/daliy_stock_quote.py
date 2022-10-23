import random
import requests
import json

from datetime import datetime, timezone, timedelta

from test import get_json

def get_user_agent():
    CHROME = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    EDGE = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/104.0.1293.70'

    list = [CHROME, EDGE]
    
    return random.choice(list)

URL = 'https://query1.finance.yahoo.com/v8/finance/chart/^IXIC'

res = requests.get(url = URL,
                    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                                "Accept-Encoding": "gzip, deflate, br", 
                                "Accept-Language": "zh-TW,zh;q=0.9", 
                                "Host": "query1.finance.yahoo.com",  #目標網站 
                                "Sec-Fetch-Dest": "document", 
                                "Sec-Fetch-Mode": "navigate", 
                                "Sec-Fetch-Site": "none", 
                                "Upgrade-Insecure-Requests": "1",
                                "user-agent" : get_user_agent(),
                                "Referer": "https://www.google.com/"})


dict = json.loads(get_json())
# .result[0].indicators.quote[0].close
# ['result'][0]

def get_quote_volume_list(dict):
    return dict['chart']['result'][0]['indicators']['quote'][0]['volume']

def get_quote_open_list(dict):
    return dict['chart']['result'][0]['indicators']['quote'][0]['open']

def get_timestamp_list(dict):
    return dict['chart']['result'][0]['timestamp']

test1 =  datetime.fromtimestamp(get_timestamp_list(dict)[0])
print(test1)
print(test1.utcoffset())

test2 =  datetime.fromtimestamp(get_timestamp_list(dict)[0], tz = timezone(-timedelta(hours = 4)))
print('EDT :', test2)

test3 =  datetime.fromtimestamp(get_timestamp_list(dict)[0], tz = timezone.utc)
print('UTC :', test3)


