import requests
from bs4 import BeautifulSoup

import datetime

from model.Currency import Currency

def get_daily_rate():
    URL = 'https://rate.bot.com.tw/xrt?Lang=en-US'

    res = requests.get(URL)

    soup = BeautifulSoup(res.text, 'html.parser')

    quoted_date_str = soup.find('span', class_='time').get_text().strip()
    
    quoted_date = datetime.strftime(quoted_date_str, '%Y/%m/%d %H:%m')
    
    quoted_date.timezone = 'Asia/Taipei'

    data_set = soup.find('tbody').find_all('tr')

    list = []

    for data in data_set:
        currency_object = Currency()

        currency_object.quoted_date = quoted_date
        currency_object.currency = data.find('div', class_='visible-phone print_hide').get_text().strip()
        currency_object.cash_buying = data.find(attrs={"data-table" : "Cash Buying"}).get_text().strip()
        currency_object.cash_selling = data.find(attrs={"data-table" : "Cash Selling"}).get_text().strip()
        currency_object.spot_buying = data.find(attrs={"data-table" : "Spot Buying"}).get_text().strip()
        currency_object.spot_selling = data.find(attrs={"data-table" : "Spot Selling"}).get_text().strip()

        list.append(currency_object)
    
    return list
