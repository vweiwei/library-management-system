from Utils.Database import MongoConnection
from Model.Beans.student import Students
from bson import ObjectId

class StudentDAO:

    def __init__(self):
        self.connection = MongoConnection()

    @staticmethod
    def construct_student_meta_data(meta_data):
        idx = meta_data["_id"]
        name = meta_data["name"]
        email = meta_data["email"]
        violate = meta_data["violate"]

        return Students(idx, name, email, violate)

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

    def select_one_student_by_id(self, idx):
        if isinstance(idx, str):
            idx = ObjectId(idx)
        try:
            student_meta = self.connection.db["student"].find_one({"_id": idx})
            print(student_meta)
            if student_meta is None:
                return None
            else:
                student = self.construct_student_meta_data(student_meta)

                pre_list = self.connection.db["preserve"].find({"stu_id": student.idx})
                if pre_list is None:
                    return student
                else:
                    for pre_meta_data in pre_list:
                        seat_id = pre_meta_data["seat_id"]
                        seat_data = self.connection.db["seat"].find_one({"_id": ObjectId(seat_id)})
                        class_data = self.connection.db["classroom"].find_one({"_id": ObjectId(seat_data["classroom"])})
                        if seat_data is None:
                            continue
                        student.preserve_list.append(self.construct_preserve_list(pre_meta_data,
                                                                                  seat_data["name"],
                                                                                  class_data["name"]))
                return student
        except Exception as e:
            print("Select student failed ! ", e)
            return None
