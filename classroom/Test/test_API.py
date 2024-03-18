import requests
import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Utils.utils import Rollback

url_root = "http://127.0.0.1:8080"


def test_root():
    r = requests.get(url=url_root)
    assert r.status_code == 200


def test_student_login():
    url_student_login = url_root + "/login/student"
    data = {
        'username': 'Scy',
        'passwd': '123123'
    }
    r = requests.post(url=url_student_login, data=data)
    assert r.status_code == 200
    print(r.json())
    file = r.json()
    assert file['results']['data']['name'] == data['username']
    assert file['results']['login_status'] == 1


def test_admin_login():
    url_admin_login = url_root + "/login/admin"
    data = {
        'username': 'admin',
        'passwd': '123123'
    }
    r = requests.post(url=url_admin_login, data=data)
    print("state", r.status_code)
    assert r.status_code == 200


def test_student_sign_up():
    url_student_sign_up = url_root + "/sign_up/student"
    data = {
        "username": "Blz",
        "passwd": "123123",
        "name": "Blz",
        "email": "1234567890@163.com"
    }
    r = requests.post(url=url_student_sign_up, data=data)
    print(r.json())
    assert r.status_code == 200
    assert r.json()['results']['sign_up_status'] == 1

    Rollback(data, 'student_sign_up')


def test_student_preserve():
    url_student_preserve = url_root + "/students/preserve"
    data = {
        'uid': ObjectId('64760d55b6f00d801a5e5499'),
        'sid': ObjectId('646b613606b11a421a63e1dd'),
        'start_time': '15',
        'end_time': '18'
    }
    r = requests.post(url=url_student_preserve, data=data)
    assert r.status_code == 200
    print(r.json())
    assert r.json()['results']['preserve'] == 1

    Rollback(data, 'preserve')


def test_get_classroom_overview():
    url_classroom_overview = url_root + "/classrooms/overview"
    r = requests.get(url=url_classroom_overview)
    print(r.json())
    assert r.status_code == 200


def test_get_classrooms_detail():
    url_classroom_detail = url_root + "/classrooms/detail"
    data = {
        'cid': ObjectId('646b602906b11a421a63e1d1')
    }
    r = requests.get(url=url_classroom_detail, data=data)
    print(r.json())
    assert r.status_code == 200

# Error
def test_get_seats_detail():
    url_get_seats_detail = url_root + "/seats/detail/"
    data = {
        'sid': ObjectId('646b613606b11a421a63e1dd')
    }
    r = requests.get(url=url_get_seats_detail, data=data)
    print("!!!!r: ", r.content)
    assert r.status_code == 200


def test_get_students_detail():
    url_students_detail = url_root + "/students/detail"
    data = {
        'uid': ObjectId('64760d55b6f00d801a5e5499')
    }
    r = requests.get(url=url_students_detail, data=data)
    assert r.status_code == 200


def test_cancel_preserve():
    url_cancel_preserve = url_root + "/preserve/cancel"
    data = {
        'pid': ObjectId('64902a5e44b7657c00685170')
    }

    Mongo = MongoConnection()
    preserve = Mongo.db['preserve']
    former_data = preserve.find_one({'_id': data['pid']})
    r = requests.post(url=url_cancel_preserve, data=data)
    print(r.content)
    assert r.content
    Rollback(data, "cancel_preserve", former_data)


def test_check_in():
    url_check_in = url_root + "/preserve/check_in"
    data = {
        'pid': ObjectId('64902a5e44b7657c00685170')
    }
    r = requests.post(url=url_check_in, data=data)
    print(r.json())
    assert r.json()['msg'] == 'ok'
    Rollback(data, "check_in")


def test_modify_time():
    url_modify_time = url_root + "/classrooms/modify_time"
    data = {
        'cid': ObjectId('646b602906b11a421a63e1d1'),
        'start_time': '6',
        'end_time': '20',
    }
    Mongo = MongoConnection()
    preserve = Mongo.db['classroom']
    former_data = preserve.find_one({'_id': data['cid']})
    r = requests.post(url=url_modify_time, data=data)
    print(former_data)
    assert r.json()['msg'] == 'ok'
    Rollback(data, "modify_time", former_data)

