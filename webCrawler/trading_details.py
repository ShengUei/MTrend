from datetime import datetime, timedelta

from util.request import get_request
from logger.logger import get_logger, close_handler

def get_daily_trading_details():
    selectType = {
                    'Cement': '01', 'Food': '02', 'Plastic': '03', 'Textile': '04', 'Electric, Machinery': '05', 
                    'Electrical and Cable': '06', 'Chemical, Biotechnology, and Medical Care Industry': '07', 'Glass and Ceramic': '08', 'Paper and Pulp': '09', 'Iron and Steel': '10', 
                    'Rubber': '11', 'Automobile': '12', 'Electronic': '13', 'Building Material and Construction': '14', 'Shipping and Transportation': '15', 
                    'Tourism': '16', 'Financial and Insurance': '17', 'Trading and Consumers Goods Industry': '18', 'General': '19', 'Other Industry': '20', 
                    'Chemical Industry': '21', 'Biotechnology and Medical Care Industry': '22', 'Oil, Gas and Electricity Industry': '23', 'Semiconductor Industry': '24', 'Computer and Peripheral Equipment Industry': '25', 
                    'Computer and Peripheral Equipment Industry': '26', 'Communications and Internet Industry': '27', 'Electronic Parts/Components Industry': '28', 'Electronic Products Distribution Industry': '29', 'Information Service Industry': '30',
                    'Information Service Industry': '31'
                }
    
    try:
        for type in selectType.values():
            get_trading_details(type)

    except Exception as e:
        print("Excetion $s", e)


def get_trading_details(self, selectType: str):
    logger = get_logger()

    try:
        utc_now = datetime.utcnow()
        local_datetime = utc_now + timedelta(hours = 8)
        local_weekday = local_datetime.isoweekday()
        date_str = local_datetime.strftime('%Y%m%d')

        HOST = 'www.twse.com.tw'
        url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType={1}'.format(date_str, selectType)
        stat_code = {0: 'OK', 1: 'No Data!'}

        if(local_weekday > 5):
            return {}

        res_dict = get_request(url, HOST)

        if not res_dict:
            return {}
        
        if(res_dict['stat'] != stat_code[0]):
            return {}

    except Exception as e:
        print("Excetion $s", e)
        logger.error("Exception : %s" % e, exc_info=True)
        return {}

    else:
        data_dict = {
            'current_datetime': utc_now,
            'data_list': res_dict['data']
        }
        return data_dict
    
    finally:
        close_handler(logger)
        