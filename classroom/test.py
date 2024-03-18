import requests
import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.ClassroomService import *
from Utils.utils import *

classroom_service = ClassroomService()

def is_used():
    start_time = "8"
    end_time = "22"
    preserve_list = [{'idx': '64902a5e44b7657c00685171', 'start_time': '2023-06-23 13:00', 'end_time': '2023-06-23 15:00'}]
    ans = classroom_service.is_used(start_time, end_time, preserve_list)
    assert ans == True

is_used()