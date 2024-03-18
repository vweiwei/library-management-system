import pytest
import pymongo
from Utils.Database import MongoConnection
from bson import ObjectId
from Model.Service.SeatService import *

seatservice = SeatService()


def test_seat_detail_service():
    seat_idx = ObjectId('646b614506b11a421a63e1db')
    ans = seatservice.seat_detail_service(seat_idx)
    print(ans)
    assert ans['msg'] == 'ok'


def test_is_used():
    start_time = ""
    end_time = ""
    preserve_list = []
    ans = seatservice.is_used(start_time, end_time, preserve_list)
    assert ans == True

