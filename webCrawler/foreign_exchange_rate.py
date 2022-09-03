import requests
from bs4 import BeautifulSoup

from datetime import datetime, timezone

from model.Currency import Currency
from logger.logger import get_logger

def get_daily_rate():
    URL = 'https://rate.bot.com.tw/xrt?Lang=en-US'

    logger = get_logger()

    try:
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
        print("Excetion $s", e)
        logger.error("BaseException : %s" % e)
        return []

    else:
        print("Get Daily Exchange Rate Success From web")
        logger.info("Get Daily Exchange Rate Success From web")
        return list
    
    finally:
        res.close()
