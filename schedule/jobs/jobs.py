from datetime import datetime, timezone
from sendEmail.send_email import send_email
from webCrawler.foreign_exchange_rate import get_daily_rate
from dataAccess.postgresql.data_access import insert_all_exchange_rate

def get_and_save_exchange_rate():
    dailyRateList = get_daily_rate()

    if not dailyRateList:
        title = "Get Daily Exchange Rate Failure From web"
        content = "Get Daily Exchange Rate Failure From web at {}".format(datetime.now(timezone.utcoffset(+8)))
        send_email(title, content)
    
    else:
        insert_all_exchange_rate(dailyRateList)

        title = "Get Daily Exchange Rate Success"
        content = "Get Daily Exchange Rate Success at {}".format(datetime.now(timezone.utcoffset(+8)))
        send_email(title, content)
