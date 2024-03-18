import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.EmailService import *
from Utils.utils import Rollback

emailservice = EmailService()


def test_send_email_service():
    start_time = "2023-06-23 13:00"
    ans = emailservice.send_email_service(start_time)
    assert ans == 1


def test_send_second_email_service():
    start_time = "2023-06-23 13:00"
    ans = emailservice.send_second_email_service(start_time)
    assert ans == 1


def test_send_final_email_service():
    start_time = "2023-06-23 13:00"
    Mongo = MongoConnection()
    preserve = Mongo.db['preserve']
    former_datas = preserve.find({'start_time': start_time})
    former_data = []
    for data in former_datas:
        former_data.append({
            '_id': data['_id'],
            'stu_id': data['stu_id'],
            'seat_id': data['seat_id'],
            'start_time': data['start_time'],
            'end_time': data['end_time'],
            'is_check_in': data['is_check_in']
        })
    ans = emailservice.send_final_email_service(start_time)
    assert ans == 1
    res = preserve.find_one({'start_time': start_time})
    assert res == None

    Rollback({"start_time": start_time}, "send_final_email_service", former_data)



