from typing import Final


class APIStatus:

    def __init__(self):
        self.status_ok: Final = {"status": 0, "msg": "ok"}
        self.status_error: Final = {"status": 1}

        self.param_null: Final = {"code": 101, "msg": "参数为空"}
        self.get_data_failed: Final = {"code": 102, "msg": "获取数据失败"}
        self.preserve_failed: Final = {"code": 103, "msg": "预定失败"}
        self.check_in_failed: Final = {"code": 104, "msg": "签到失败"}
        self.cancel_preserve_failed: Final = {"code": 105, "msg": "取消预约失败"}
        self.change_time_failed: Final = {"code": 106, "msg": "修改自习室开放时间失败"}

    def construct_ok_data(self, ok_msg):
        result = self.status_ok
        result["results"] = ok_msg
        return result

    def construct_error_data(self, error_type):

        result_status = self.status_error

        assert isinstance(error_type, dict)
        result = dict(result_status, **error_type)

        return result
