import requests
from bs4 import BeautifulSoup

from Currency import Currency

url = 'https://rate.bot.com.tw/xrt?Lang=en-US'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

quoted_date = soup.find('span', class_='time').get_text().strip()

data_set = soup.find('tbody').find_all('tr')

list = []

for data in data_set:

    object = Currency()

    object.quoted_date = quoted_date
    object.currency = data.find('div', class_='visible-phone print_hide').get_text().strip()
    object.cash_buying = data.find(attrs={"data-table" : "Cash Buying"}).get_text().strip()
    object.cash_selling = data.find(attrs={"data-table" : "Cash Selling"}).get_text().strip()
    object.spot_buying = data.find(attrs={"data-table" : "Spot Buying"}).get_text().strip()
    object.spot_selling = data.find(attrs={"data-table" : "Spot Selling"}).get_text().strip()

    list.append(object)

for data in list:
    print(data.quoted_date)
    print(data.currency)
    print(data.cash_buying)
    print(data.cash_selling)
    print(data.spot_buying)
    print(data.spot_selling)