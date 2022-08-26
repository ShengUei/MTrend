from datetime import datetime, timezone
from logger.logger import get_logger
from sendEmail.send_email import send_email
from webCrawler.foreign_exchange_rate import get_daily_rate
from dataAccess.postgresql.data_access import insert_all_exchange_rate

def get_and_save_exchange_rate():
    logger = get_logger()

    dailyRateList = get_daily_rate()

    insert_all_exchange_rate(dailyRateList)

    title = "Get Daily Exchange Rate Success"
    content = "Get Daily Exchange Rate Success at {}".format(datetime.now(timezone.utcoffset(+8)))
    send_email(title, content)

    logger.info("Get Daily Exchange Rate Success")