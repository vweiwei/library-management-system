from Model.DAO.EmailDao import EmailDAO
from Utils.utils import send_email


class EmailService:

    def __init__(self):
        self.ema_dao = EmailDAO()

    def send_email_service(self, start_time):
        email_list = self.ema_dao.select_preserves_by_start_time(start_time)
        if email_list is None:
            print("没有需要发的邮件")
            return 0
        else:
            send_email(email_list, "你的预约时间即将到达，还剩15分钟，请抓紧签到！", "预约提醒")
            return 1

    def send_second_email_service(self, start_time):
        email_list = self.ema_dao.select_preserves_by_start_time(start_time)
        if email_list is None:
            print("没有需要发的邮件")
            return 0
        else:
            send_email(email_list, "你的预约时间已超时10分钟，请抓紧签到，未签到将记为违约处理！", "预约提醒")
            return 1

    def send_final_email_service(self, start_time):
        email_list = self.ema_dao.select_preserves_by_start_time_and_delete_preserves(start_time)
        if email_list is None:
            print("没有需要发的邮件")
            return 0
        else:
            send_email(email_list, "你的预约时间已超时，已计入违约！", "预约提醒")
            return 1
