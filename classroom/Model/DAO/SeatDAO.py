from Utils.Database import MongoConnection
from Model.Beans.seat import Seat
from bson import ObjectId


class SeatDAO:

    def __init__(self):
        self.connection = MongoConnection()

    @staticmethod
    def construct_seat_meta_data(meta_data):
        idx = meta_data["_id"]
        name = meta_data["name"]
        is_special = meta_data["is_special"]
        classroom = meta_data["classroom"]

        return Seat(idx, name, is_special, classroom)

    def construct_preserve_list(self, meta_data):

        return {
            "idx": str(meta_data["_id"]),
            "start_time": meta_data["start_time"],
            "end_time": meta_data["end_time"]
        }

    def select_seats_by_classroom_id(self, classroom_idx):
        if isinstance(classroom_idx, str):
            classroom_idx = ObjectId(classroom_idx)
        try:
            seat_list_meta = self.connection.db["seat"].find({"classroom": classroom_idx})
            if seat_list_meta is None:
                return None
            else:
                seat_list = []

                for meta_data in seat_list_meta:
                    seat_obj = self.construct_seat_meta_data(meta_data)
                    pre_list = self.connection.db["preserve"].find({"seat_id": seat_obj.idx})
                    if pre_list is None:
                        seat_list.append(seat_obj)
                    else:
                        for pre_meta_data in pre_list:
                            seat_obj.preserve_list.append(self.construct_preserve_list(pre_meta_data))
                    seat_list.append(seat_obj)
                return seat_list
        except Exception as e:
            print("Select seats by classroom_id failed ! ", e)
            return None

    def select_seat_by_seat_id(self, seat_idx):

        assert isinstance(seat_idx, str)
        seat_oid = ObjectId(seat_idx)
        try:
            # seat_meta = self.connection.db["seat"].find_one({"_id": seat_idx})
            seat_meta = self.connection.db["seat"].find_one({"_id": seat_oid})
            if seat_meta is None:
                return None
            else:

                seat_obj = self.construct_seat_meta_data(seat_meta)
                pre_list = self.connection.db["preserve"].find({"seat_id": seat_obj.idx})
                if pre_list is None:
                    return seat_obj
                else:
                    for pre_meta_data in pre_list:
                        seat_obj.preserve_list.append(self.construct_preserve_list(pre_meta_data))
                    return seat_obj
        except Exception as e:
            print("Select seats by classroom_id failed ! ", e)
            return None

