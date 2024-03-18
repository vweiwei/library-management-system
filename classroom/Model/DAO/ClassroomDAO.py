from Utils.Database import MongoConnection
from Model.Beans.classroom import Classroom
from bson import ObjectId


class ClassroomDAO:

    def __init__(self):
        self.connection = MongoConnection()

    @staticmethod
    def construct_classroom_meta_data(meta_data):

        idx = meta_data["_id"]
        name = meta_data["name"]
        start_time = meta_data["start_time"]
        end_time = meta_data["end_time"]

        return Classroom(idx, name, start_time, end_time)

    def select_one_classroom_by_id(self, idx):
        if isinstance(idx, str):
            idx = ObjectId(idx)
        try:
            classroom_meta = self.connection.db["classroom"].find_one({"_id": idx})
            if classroom_meta is None:
                return None
            else:
                student = self.construct_classroom_meta_data(classroom_meta)
                return student
        except Exception as e:
            print("Select classroom failed ! ", e)
            return None

    def select_classroom_overview(self):
        try:
            classroom_list_meta = self.connection.db["classroom"].find()
            if classroom_list_meta is None:
                return None
            classroom_list = []

            for meta_data in classroom_list_meta:
                data = self.construct_classroom_meta_data(meta_data)
                classroom_list.append(data)

            return classroom_list

        except Exception as e:
            print("Select classroom overview failed ! ", e)
            return None

    def update_classroom_time(self, cid, start_time, end_time):

        if isinstance(cid, str):
            cid = ObjectId(cid)

        # if isinstance(start_time, str):
        #     start_time = int(start_time)
        #
        # if isinstance(end_time, str):
        #     end_time = int(end_time)

        try:
            print("Trying")
            update_query = {"_id": cid}
            update_data = {"$set": {"start_time": start_time, "end_time": end_time}}
            insert_meta = self.connection.db["classroom"].update_one(update_query, update_data)
            if insert_meta is None:
                return False
            else:
                return True
        except Exception as e:
            print("preserve delete failed ! ", e)
            return False
