import requests
from bs4 import BeautifulSoup
import json

from Currency import Currency

url = 'https://rate.bot.com.tw/xrt?Lang=en-US'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# currencies = soup.find_all('div', class_='visible-phone print_hide')

# for currency in currencies:
#     print(currency.get_text().strip())

# cash_buyings = soup.find_all(attrs={"data-table": "Cash Buying"})

# for cash_buying in cash_buyings:
#     print(cash_buying.get_text().strip())

data_set = soup.find('tbody').find_all('tr')

list = []

for data in data_set:
    # dict = {}
    # dict.update({'Currency' : data.find('div', class_='visible-phone print_hide').get_text().strip()})
    # dict.update({'Cash Buying' : data.find(attrs={"data-table" : "Cash Buying"}).get_text().strip()})
    # dict.update({'Cash Sellingg' : data.find(attrs={"data-table" : "Cash Selling"}).get_text().strip()})
    # dict.update({'Spot Buying' : data.find(attrs={"data-table" : "Spot Buying"}).get_text().strip()})
    # dict.update({'Spot Selling' : data.find(attrs={"data-table" : "Spot Selling"}).get_text().strip()})
    # list.append(dict)

    object = Currency()
    object.currency = data.find('div', class_='visible-phone print_hide').get_text().strip()
    object.cash_buying = data.find(attrs={"data-table" : "Cash Buying"}).get_text().strip()
    object.cash_selling = data.find(attrs={"data-table" : "Cash Selling"}).get_text().strip()
    object.spot_buying = data.find(attrs={"data-table" : "Spot Buying"}).get_text().strip()
    object.spot_selling = data.find(attrs={"data-table" : "Spot Selling"}).get_text().strip()

    list.append(object)
    # dict.clear()
    # x = json.load(data.get_text().strip())
    # print('x = ' + x)

for data in list:
    print(data.currency)
    print(data.cash_buying)
    print(data.cash_selling)
    print(data.spot_buying)
    print(data.spot_selling)