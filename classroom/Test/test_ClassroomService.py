import requests
import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.ClassroomService import *
from Utils.utils import *

classroom_service = ClassroomService()


def test_classroom_overview_service():
    ans = classroom_service.classroom_overview_service()
    assert ans['msg'] == "ok"


def test_classroom_detail_service():
    classroom_idx = ""
    ans = classroom_service.classroom_detail_service(classroom_idx)
    assert ans['msg'] == "ok"


def test_is_used():
    start_time = "8"
    end_time = "22"
    preserve_list = [{'idx': '64902a5e44b7657c00685171', 'start_time': '2023-06-23 13:00', 'end_time': '2023-06-23 15:00'}]
    ans = classroom_service.is_used(start_time, end_time, preserve_list)
    assert ans == True


def test_change_time_service():
    cid = ObjectId('646b602906b11a421a63e1d1')
    start_time = "6"
    end_time = "20"
    Mongo = MongoConnection()
    preserve = Mongo.db['classroom']
    former_data = preserve.find_one({'_id': cid})
    ans = classroom_service.change_time_service(cid, start_time, end_time)
    assert ans['msg'] == "ok"
    Rollback({'cid': ObjectId('646b602906b11a421a63e1d1'), 'start_time': '6', 'end_time': '20'},
             'change_time_service',
             former_data)
