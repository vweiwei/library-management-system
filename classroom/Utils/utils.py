import smtplib
from email.mime.text import MIMEText
# DEIEHFVJLJOEULQI

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pymongo
from bson import ObjectId
from Utils.Database import MongoConnection


def send_email(email_list, content, subject):
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "kuusou_class_test@163.com"  # 用户名
    mail_pass = "DEIEHFVJLJOEULQI"  # 口令

    sender = 'kuusou_class_test@163.com'
    # receivers = ['2457732990@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    receivers = email_list
    for receiver in receivers:

        message = MIMEText(content, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = receiver

        subject = subject
        message['Subject'] = Header(subject, 'utf-8')


        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


def Rollback(data, task_name, former_data=None):
    if task_name == "student_sign_up" or task_name == "sign_up_service":
        Mongo = MongoConnection()
        s_account = Mongo.db['s_account']
        s_account.delete_one({'username': data['username']})
        student = Mongo.db['student']
        student.delete_one({'name': data['username']})

    elif task_name == 'preserve':
        Mongo = MongoConnection()
        preserve = Mongo.db['preserve']
        preserve.delete_one({
            'seat_id': data['sid'],
            'stu_id': data['uid'],
            'start_time': data['start_time'],
            'end_time': data['end_time']
        })

    elif task_name == 'cancel_preserve':
        Mongo = MongoConnection()
        preserve = Mongo.db['preserve']
        preserve.insert_one(former_data)

    elif task_name == 'check_in':
        Mongo = MongoConnection()
        preserve = Mongo.db['preserve']
        update_query = {"_id": data['pid']}
        update_data = {"$set": {"is_check_in": 0}}
        preserve.update_one(update_query, update_data)

    elif task_name == 'modify_time' or task_name == 'change_time_service':
        Mongo = MongoConnection()
        preserve = Mongo.db['classroom']
        update_query = {"_id": data['cid']}
        update_data = {"$set": {"start_time": former_data['start_time'], "end_time": former_data['end_time']}}
        preserve.update_one(update_query, update_data)

    elif task_name == 'send_final_email_service':
        Mongo = MongoConnection()
        preserve = Mongo.db['preserve']
        student = Mongo.db['student']
        for data in former_data:
            preserve.insert_one(data)
            student.update_one({"_id": ObjectId(data['stu_id'])}, {"$set": {"violate": False}})

    elif task_name == 'is_used':
        pass






