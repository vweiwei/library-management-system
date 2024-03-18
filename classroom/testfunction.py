# a = ["and", "me"]
#
# print(list(map(int,a)))

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta


def email_job_1():
    current_time = datetime.now()
    prefix = str(current_time.strftime("%Y-%m-%d"))
    hour = str(int(current_time.strftime("%H")) + 1)
    start_time = prefix + " " + hour + ":00"


def email_job_2():
    current_time = datetime.now()
    start_time = current_time.strftime("%Y-%m-%d %H:%M")
    print("This is the result at", start_time)


def email_job_3():
    current_time = datetime.now()
    start_time = current_time.strftime("%Y-%m-%d %H:%M")
    print("This is the result at", start_time)


def start_scheduler():
    # 创建调度器
    scheduler = BlockingScheduler()

    # 添加整点前十五分钟触发的定时任务
    scheduler.add_job(email_job_1, 'cron', hour='*', minute=45)

    # 添加整点后十分钟触发的定时任务
    scheduler.add_job(email_job_2, 'cron', hour='*', minute=10)

    # 添加整点后十五分钟触发的定时任务
    scheduler.add_job(email_job_3, 'cron', hour='*', minute=15)

    # 启动调度器
    scheduler.start()


if __name__ == '__main__':
    email_job_1()
