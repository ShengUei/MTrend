from datetime import datetime, timedelta

from util.request import get_request
from logger.logger import get_logger

def get_daily_trading_details():
    try:
        utc_now = datetime.utcnow()
        local_datetime = utc_now + timedelta(hours = 8)
        local_weekday = local_datetime.isoweekday()
        date_str = local_datetime.strftime('%Y%m%d')

        HOST = 'www.twse.com.tw'
        url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType=ALL'.format(date_str)
        stat_code = {0: 'OK', 1: 'No Data!'}
        
        logger = get_logger()

        if(local_weekday > 5):
            print('Today is holiday.')
            logger.info('Today is holiday.')
            return {}

        res_dict = get_request(url, HOST)

        if not res_dict:
            print('Get Data Failures From web.')
            logger.error('Get Data Failures From web.')
            return {}
        
        if(res_dict['stat'] != stat_code[0]):
            print('No data.')
            logger.error('No data.')
            return {}

    except Exception as e:
        print("Excetion $s", e)
        logger.error("Exception : %s" % e)
        return {}

    else:
        print("Get Daily Trading Details Success From web")
        logger.info("Get Daily Trading Details Success From web")
        data_dict = {
            'current_datetime': utc_now,
            'data_list': res_dict['data']
        }
        return data_dict
    
    finally:
        print("Get Daily Trading Details Done")
        logger.info("Get Daily Trading Details Done")

