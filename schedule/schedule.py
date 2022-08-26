from apscheduler.schedulers.background import BackgroundScheduler
from jobs.jobs import get_and_save_exchange_rate

scheduler = BackgroundScheduler()

#每週一 ~ 五 18:00 ，由網路抓匯率與存匯率至DB
scheduler.add_job(get_and_save_exchange_rate, 'cron', day_of_week = '1-5', hour = 18)

scheduler.start()

