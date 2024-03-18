from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
from Model.Service.EmailService import EmailService


def email_job_1():
    current_time = datetime.now()
    prefix = str(current_time.strftime("%Y-%m-%d"))
    hour = str(int(current_time.strftime("%H")) + 1)
    start_time = prefix + " " + hour + ":00"
    EmailService().send_email_service(start_time)


def email_job_2():
    current_time = datetime.now()
    prefix = str(current_time.strftime("%Y-%m-%d"))
    hour = str(current_time.strftime("%H"))
    start_time = prefix + " " + hour + ":00"
    EmailService().send_second_email_service(start_time)


def email_job_3():
    current_time = datetime.now()
    prefix = str(current_time.strftime("%Y-%m-%d"))
    hour = str(current_time.strftime("%H"))
    start_time = prefix + " " + hour + ":00"
    print(start_time)
    EmailService().send_final_email_service(start_time)

def start_email_scheduler():
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
