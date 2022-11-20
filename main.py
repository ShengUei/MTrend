from datetime import datetime, timedelta
from dataAccess.postgresql.connection import openConnection

from dataAccess.postgresql.data_access import insert_trading_details
from webCrawler.trading_details import get_trading_details

def get_daily_all_trading_details():
    selectType = {
                    'Cement': '01', 'Food': '02', 'Plastic': '03', 'Textile': '04', 'Electric, Machinery': '05', 
                    'Electrical and Cable': '06', 'Chemical, Biotechnology, and Medical Care Industry': '07', 'Glass and Ceramic': '08', 'Paper and Pulp': '09', 'Iron and Steel': '10', 
                    'Rubber': '11', 'Automobile': '12', 'Electronic': '13', 'Building Material and Construction': '14', 'Shipping and Transportation': '15', 
                    'Tourism': '16', 'Financial and Insurance': '17', 'Trading and Consumers Goods Industry': '18', 'General': '19', 'Other Industry': '20', 
                    'Chemical Industry': '21', 'Biotechnology and Medical Care Industry': '22', 'Oil, Gas and Electricity Industry': '23', 'Semiconductor Industry': '24', 'Computer and Peripheral Equipment Industry': '25', 
                    'Computer and Peripheral Equipment Industry': '26', 'Communications and Internet Industry': '27', 'Electronic Parts/Components Industry': '28', 'Electronic Products Distribution Industry': '29', 'Information Service Industry': '30',
                    'Information Service Industry': '31'
                }

    utc_now = datetime.utcnow()
    local_datetime = utc_now + timedelta(hours = 8)
    local_weekday = local_datetime.isoweekday()

    if(local_weekday > 5):
        print('Today is weekend')
        return
    
    try:
        for stock_type in selectType.values():
            print('stock_type: ' + stock_type)

            data = get_trading_details(local_datetime, stock_type)

            if data is not None:
                insert_trading_details(data)

        print('get_daily_all_trading_details done')

    except Exception as e:
        print("Excetion $s", e)

get_daily_all_trading_details()

