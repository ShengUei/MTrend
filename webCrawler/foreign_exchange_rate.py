import requests
from bs4 import BeautifulSoup

from datetime import datetime, timezone
import time
import random

from model.Currency import Currency
from logger.logger import get_logger, close_handler

def get_daily_rate():
    URL = 'https://rate.bot.com.tw/xrt?Lang=en-US'

    logger = get_logger()

    try:
        #先 sleep 幾秒，再開始 run
        time.sleep(random.uniform(1.0, 60.0))

        res = requests.get(URL)

        soup = BeautifulSoup(res.text, 'html.parser')
        
        #抓取本機時間(UTC)
        now = datetime.now(timezone.utc)

        data_set = soup.find('tbody').find_all('tr')

        list = []

        for data in data_set:
            currency_object = Currency()

            currency_object.quoted_date = now
            currency_object.currency = data.find('div', class_='visible-phone print_hide').get_text().strip()

            cash_buying = data.find(attrs={"data-table" : "Cash Buying"}).get_text().strip()
            currency_object.cash_buying = cash_buying if cash_buying != '-' else 0

            cash_selling = data.find(attrs={"data-table" : "Cash Selling"}).get_text().strip()
            currency_object.cash_selling = cash_selling if cash_selling != '-' else 0

            spot_buying = data.find(attrs={"data-table" : "Spot Buying"}).get_text().strip()
            currency_object.spot_buying = spot_buying if spot_buying != '-' else 0

            spot_selling = data.find(attrs={"data-table" : "Spot Selling"}).get_text().strip()
            currency_object.spot_selling = spot_selling if spot_selling != '-' else 0

            list.append(currency_object)

    except Exception as e:
        logger.error("BaseException : %s" % e, exc_info=True)
        return []

    else:
        return list
    
    finally:
        res.close()
        close_handler(logger)
