import requests
import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.AccountService import *
from Utils.utils import *

url_root = "http://127.0.0.1:5000"

account_service = AccountService()
Mongo = MongoConnection()
s_account = Mongo.db['s_account']
student = Mongo.db['student']
def test_student_login_service():
    username = "Scy"
    passwd = "123123"
    ans = account_service.student_login_service(username, passwd)
    assert ans['msg'] == "登陆成功"
    assert ans['data'] == ObjectId('64760d55b6f00d801a5e5499')


def test_admin_login_service():
    username = "admin"
    passwd = "123123"
    ans = account_service.admin_login_service(username, passwd)
    assert ans['msg'] == "登陆成功"
    assert ans['data'] == 1

def test_sign_up_service():
    username = "Blz"
    passwd = "123123"
    name = "Blz"
    email = "3043642553@qq.com"
    ans = account_service.sign_up_service(username, passwd, name, email)
    assert ans['status'] == 1
    assert ans['msg'] == '注册成功！'
    Rollback({
        "username": "Blz",
        "passwd": "123123",
        "name": "Blz",
        "email": "1234567890@163.com"
    }, "sign_up_service")

