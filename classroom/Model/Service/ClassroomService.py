from Model.DAO.ClassroomDAO import ClassroomDAO
from Model.DAO.SeatDAO import SeatDAO
from datetime import datetime


class ClassroomService:

    def __init__(self):
        self.cla_dao = ClassroomDAO()
        self.seat_dao = SeatDAO()

    def classroom_overview_service(self):
        classrooms = self.cla_dao.select_classroom_overview()
        classrooms_data = []
        for classroom in classrooms:
            data = classroom.construct_dict()
            print(data["start_time"], data["end_time"])
            if int(data["start_time"]) >= int(data["end_time"]):
                data["is_open"] = False
            else:
                data["is_open"] = True
            print(data["is_open"])
            classrooms_data.append(data)
        if classrooms is None:
            return {"msg": "获取教室总体信息失败", "data": classrooms_data}
        else:
            return {"msg": "ok", "data": classrooms_data}

    def classroom_detail_service(self, classroom_idx):
        classroom = self.cla_dao.select_one_classroom_by_id(classroom_idx)
        if classroom is None:
            return {"msg": "按id获取单个教室信息失败", "data": None}

        seats = self.seat_dao.select_seats_by_classroom_id(classroom_idx)
        seats_info = []
        start_time = classroom.start_time
        end_time = classroom.end_time
        # 一个教室可以没有座位
        if seats is None:
            return {"msg": "ok", "data": seats_info, "start_time": start_time, "end_time": end_time}

        for seat in seats:

            info_dict = {"id": str(seat.idx),
                         "name": seat.name,
                         "is_special": seat.is_special,
                         "is_used": self.is_used(start_time, end_time, seat.preserve_list)}
            seats_info.append(info_dict)

        return {"msg": "ok", "data": seats_info, "start_time": start_time, "end_time": end_time}

    @staticmethod
    def is_used(start_time, end_time, preserve_list):
        total_time = int(end_time) - int(start_time)
        print(total_time)
        total_pre_time = 0
        for pre in preserve_list:
            pre_end_time = datetime.strptime(pre['end_time'], "%Y-%m-%d %H:%M").hour
            pre_start_time = datetime.strptime(pre['start_time'], "%Y-%m-%d %H:%M").hour

            total_pre_time += int(pre_end_time - pre_start_time)
            print(total_pre_time)

        if total_pre_time < total_time:
            print("Fa")
            return False
        else:
            return True

    def change_time_service(self, cid, start_time, end_time):
        result = self.cla_dao.update_classroom_time(cid, start_time, end_time)
        if result:
            return {"msg": "ok", "data": {"is_change": 1}}
        else:
            return {"msg": "修改自习室开放时间失败！", "data": None}
