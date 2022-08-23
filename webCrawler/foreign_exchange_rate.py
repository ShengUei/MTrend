import requests
from bs4 import BeautifulSoup

from datetime import datetime

from model.Currency import Currency

def get_daily_rate():
    URL = 'https://rate.bot.com.tw/xrt?Lang=en-US'

    res = requests.get(URL)

    soup = BeautifulSoup(res.text, 'html.parser')

    quoted_date_str = soup.find('span', class_='time').get_text().strip()
    
    quoted_date = datetime.strptime(quoted_date_str, '%Y/%m/%d %H:%M')

    data_set = soup.find('tbody').find_all('tr')

    list = []

    for data in data_set:
        currency_object = Currency()

        currency_object.quoted_date = quoted_date
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
    
    return list