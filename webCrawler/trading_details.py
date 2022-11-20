from datetime import datetime

from util.request import get_request
from logger.logger import get_logger, close_handler

def get_trading_details(date: datetime, selectType: str):
    # logger = get_logger()

    try:
        date_str = date.strftime('%Y%m%d')

        HOST = 'www.twse.com.tw'
        url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType={1}'.format(date_str, selectType)
        stat_code = {0: 'OK', 1: 'No Data!'}

        res_dict = get_request(url, HOST)

        if not res_dict:
            print('Crawler fail.')
            return {}
        
        if(res_dict['stat'] != stat_code[0]):
            print('No Data!')
            return {}

    except Exception as e:
        print("Excetion $s", e)
        # logger.error("Exception : %s" % e, exc_info=True)
        return {}

    else:
        utc_now = datetime.utcnow()

        data_dict = {
            'current_datetime': utc_now,
            'data_list': res_dict['data']
        }
        return data_dict
    
    finally:
        # close_handler(logger)
        print('Crawler done.')
        