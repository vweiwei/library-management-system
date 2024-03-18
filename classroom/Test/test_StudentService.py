import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.StudentService import *


studentservice = StudentService()


def test_student_detail_service():
    stu_idx = ObjectId('64760d55b6f00d801a5e5491')
    ans = studentservice.student_detail_service(stu_idx)
    assert ans['msg'] == 'ok'