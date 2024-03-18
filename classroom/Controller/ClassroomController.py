from Model.Service.ClassroomService import ClassroomService
from Utils.APIStatus import APIStatus


class ClassroomController:

    def __init__(self):
        self.service = ClassroomService()
        self.api_status = APIStatus()

    def get_classroom_overview(self):

        service_result = self.service.classroom_overview_service()

        if service_result["data"] is None:
            # ok_msg = []
            # result = self.api_status.construct_ok_data(ok_msg)
            # return result
            result = self.api_status.construct_error_data(self.api_status.get_data_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result

    def get_classroom_detail(self, classroom_id):

        service_result = self.service.classroom_detail_service(classroom_id)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.get_data_failed)
            return result

        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            result["start_time"] = service_result["start_time"]
            result["end_time"] = service_result["end_time"]
            return result

    def modify_time(self, cid, start_time, end_time):
        if cid is None or start_time is None or end_time is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.change_time_service(cid, start_time, end_time)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.change_time_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result




