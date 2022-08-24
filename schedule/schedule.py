# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job():
    print("No is: %s" % datetime.now())

# scheduler = BackgroundScheduler()
scheduler = BlockingScheduler()

print("start : %s" % datetime.now())

# 每一分鐘會去執行 job function
scheduler.add_job(job, 'interval', seconds = 5)

scheduler.start()

