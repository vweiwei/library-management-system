from Utils.Database import MongoConnection
from bson import ObjectId


class PreserveDAO:

    def __init__(self):
        self.connection = MongoConnection()

    def insert_one_preserve(self, stu_idx, seat_idx, start_time, end_time):
        if isinstance(stu_idx, str):
            stu_idx = ObjectId(stu_idx)
        if isinstance(seat_idx, str):
            seat_idx = ObjectId(seat_idx)
        try:
            insert_data = {"stu_id": stu_idx,
                           "seat_id": seat_idx,
                           "start_time": start_time,
                           "end_time": end_time,
                           "is_check_in": 0}
            insert_meta = self.connection.db["preserve"].insert_one(insert_data)
            if insert_meta is None:
                return False
            else:
                return True
        except Exception as e:
            print("Insert one preserve failed ! ", e)
            return False

    def update_check_in_by_pid(self, pid):
        if isinstance(pid, str):
            pid = ObjectId(pid)

        try:
            update_query = {"_id": pid}
            update_data = {"$set": {"is_check_in": 1}}
            insert_meta = self.connection.db["preserve"].update_one(update_query, update_data)
            if insert_meta is None:
                return False
            else:
                return True
        except Exception as e:
            print("Check in update failed ! ", e)
            return False

    def delete_check_in_by_pid(self, pid):
        if isinstance(pid, str):
            pid = ObjectId(pid)

        try:
            delete_query = {"_id": pid}
            insert_meta = self.connection.db["preserve"].delete_one(delete_query)
            if insert_meta is None:
                return False
            else:
                return True
        except Exception as e:
            print("preserve delete failed ! ", e)
            return False
