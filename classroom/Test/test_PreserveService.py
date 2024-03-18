import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.PreserveService import *
from Utils.utils import *

preserveservice = PreserveService()


def test_preserve_service():
    stu_id = ObjectId('64760d55b6f00d801a5e5499')
    seat_id = ObjectId('646b613606b11a421a63e1dd')
    start_time = "15"
    end_time = "18"
    ans = preserveservice.preserve_service(stu_id, seat_id, start_time, end_time)
    assert ans['msg'] == 'ok'
    Rollback({
        'uid': ObjectId('64760d55b6f00d801a5e5499'),
        'sid': ObjectId('646b613606b11a421a63e1dd'),
        'start_time': '15',
        'end_time': '18'
    }, "preserve")


def test_check_in_service():
    pid = ObjectId('64902a5e44b7657c00685170')
    ans = preserveservice.check_in_service(pid)
    assert ans['msg'] == 'ok'
    preserveservice.cancel_preserve_service(pid)


def test_cancel_preserve_service():
    pid = ObjectId('64902a5e44b7657c00685170')
    preserveservice.check_in_service(pid)
    ans = preserveservice.cancel_preserve_service(pid)
    assert ans['msg'] == 'ok'