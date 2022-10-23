from datetime import datetime, timedelta

from util.request import get_request
from logger.logger import get_logger, close_handler

def get_daily_trading_details():
    logger = get_logger()

    try:
        utc_now = datetime.utcnow()
        local_datetime = utc_now + timedelta(hours = 8)
        local_weekday = local_datetime.isoweekday()
        date_str = local_datetime.strftime('%Y%m%d')

        HOST = 'www.twse.com.tw'
        selectType = ['ALL', 24] #24: 半導體業
        url = 'https://www.twse.com.tw/en/fund/T86?response=json&date={0}&selectType={1}'.format(date_str, selectType[1])
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

