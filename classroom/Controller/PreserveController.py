from Utils.APIStatus import APIStatus
from Model.Service.PreserveService import PreserveService


class PreserveController:

    def __init__(self):
        self.service = PreserveService()
        self.api_status = APIStatus()

    def preserve(self, stu_id, seat_id, start_time, end_time):
        if stu_id is None or seat_id is None or start_time is None or end_time is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.preserve_service(stu_id, seat_id, start_time, end_time)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.preserve_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result

    def check_in(self, pid):
        if pid is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.check_in_service(pid)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.check_in_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result

    def cancel_preserve(self, pid):
        if pid is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.cancel_preserve_service(pid)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.preserve_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result
