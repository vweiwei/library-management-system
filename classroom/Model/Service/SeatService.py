from Model.DAO.ClassroomDAO import ClassroomDAO
from Model.DAO.SeatDAO import SeatDAO


class SeatService:

    def __init__(self):
        self.cla_dao = ClassroomDAO()
        self.seat_dao = SeatDAO()

    def seat_detail_service(self, seat_idx):
        seat = self.seat_dao.select_seat_by_seat_id(seat_idx)
        if seat is None:
            return {"msg": "按id获取座位失败", "data": None}

        return {"msg": "ok", "data": seat.construct_dict()}

    @staticmethod
    def is_used(start_time, end_time, preserve_list):
        total_time = end_time - start_time
        total_pre_time = 0
        for pre in preserve_list:
            pre_end_time = int(pre['end_time'].split(" ")[1].split(":")[0])
            pre_start_time = int(pre['start_time'].split(" ")[1].split(":")[0])
            total_pre_time += pre_end_time - pre_start_time

        if total_pre_time >= total_time:
            return False
        else:
            return True
