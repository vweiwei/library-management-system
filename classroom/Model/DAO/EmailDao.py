from Utils.Database import MongoConnection
from bson import ObjectId

class EmailDAO:

    def __init__(self):
        self.connection = MongoConnection()

    def construct_preserve_list(self, pre_meta_data, seat_name, class_name):

        return {
            "pid": str(pre_meta_data["_id"]),
            "seat_id": str(pre_meta_data["seat_id"]),
            "c_name": class_name,
            "s_name": seat_name,
            "start_time": pre_meta_data["start_time"],
            "end_time": pre_meta_data["end_time"],
            "is_check_in": pre_meta_data["is_check_in"],
            "countdownIntervalid": None,
            "remainingTime": None
        }

    def select_preserves_by_start_time(self, start_time):
        try:
            query = {"start_time": start_time}
            pre_meta_list = self.connection.db["preserve"].find(query)
            if pre_meta_list is None:
                return None
            else:
                email_list = []
                for pre_meta_data in pre_meta_list:
                    is_check_in = pre_meta_data["is_check_in"]
                    if isinstance(is_check_in, str):
                        is_check_in = int(is_check_in)
                    assert isinstance(is_check_in, int)
                    if is_check_in == 0:
                        stu_id = pre_meta_data["stu_id"]
                        stu_data = self.connection.db["student"].find_one({"uid": ObjectId(stu_id)})
                        email = stu_data["email"]
                        email_list.append(email)

                    return email_list
        except Exception as e:
            print("Select email failed ! ", e)
            return None

    def select_preserves_by_start_time_and_delete_preserves(self, start_time):
        try:
            query = {"start_time": start_time}
            pre_meta_list = self.connection.db["preserve"].find(query)
            if pre_meta_list is None:
                return None
            else:
                email_list = []
                for pre_meta_data in pre_meta_list:
                    is_check_in = pre_meta_data["is_check_in"]
                    if isinstance(is_check_in, str):
                        is_check_in = int(is_check_in)
                    assert isinstance(is_check_in, int)
                    if is_check_in == 0:
                        stu_id = pre_meta_data["stu_id"]
                        stu_data = self.connection.db["student"].find_one({"_id": ObjectId(stu_id)})
                        email = stu_data["email"]
                        email_list.append(email)
                        self.connection.db["student"].update_one({"_id": ObjectId(stu_id)},
                                                                 {"$set": {"violate": True}})
                    pre_id = pre_meta_data["_id"]
                    print(pre_id)
                    self.connection.db["preserve"].delete_one({"_id": pre_id})
            return email_list
        except Exception as e:
            print("Select email and delete email failed ! ", e)
            return None
