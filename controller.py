from flask import Flask
from webCrawler.foreign_exchange_rate import get_daily_rate

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get('/DailyExchangeRate')
def get_daily_exchange_rate():
    list = get_daily_rate()

    s = ''

    s += '<table>'

    s += '<tr>'
    s += '<th>currency</th>'
    s += '<th>cash_buying</th>'
    s += '<th>data.cash_selling</th>'        
    s += '<th>data.spot_buying</th>'
    s += '<th>data.spot_selling</th>'
    s += '</tr>'

    for data in list:
        s += '<tr>'
        s += '<td>' + data.currency + '</td>'
        s += '<td>' + data.cash_buying + '</td>'
        s += '<td>' + data.cash_selling + '</td>'
        s += '<td>' + data.spot_buying + '</td>'
        s += '<td>' + data.spot_selling + '</td>'
        s += '</tr>'
    
    s += '</table>'

    return s