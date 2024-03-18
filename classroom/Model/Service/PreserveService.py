from Model.DAO.PreserveDAO import PreserveDAO


class PreserveService:

    def __init__(self):
        self.pre_dao = PreserveDAO()

    def preserve_service(self, stu_id, seat_id, start_time, end_time):
        result = self.pre_dao.insert_one_preserve(stu_id, seat_id, start_time, end_time)
        if result:
            return {"msg": "ok", "data": {"preserve": 1}}
        else:
            return {"msg": "按id获取座位失败！", "data": None}

    def check_in_service(self, pid):
        result = self.pre_dao.update_check_in_by_pid(pid)
        if result:
            return {"msg": "ok", "data": {"isSignUp": 1}}
        else:
            return {"msg": "签到失败！", "data": None}

    def cancel_preserve_service(self, pid):
        result = self.pre_dao.delete_check_in_by_pid(pid)
        if result:
            return {"msg": "ok", "data": {"isCancel": 1}}
        else:
            return {"msg": "取消失败！", "data": None}


