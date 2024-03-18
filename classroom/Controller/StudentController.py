from Model.Service.StudentService import StudentService
from Utils.APIStatus import APIStatus


class StudentController:

    def __init__(self):
        self.service = StudentService()
        self.api_status = APIStatus()

    def get_student_detail(self, sid):

        service_result = self.service.student_detail_service(sid)

        if service_result["data"] is None:
            result = self.api_status.construct_error_data(self.api_status.get_data_failed)
            return result
        else:
            ok_msg = service_result["data"]
            result = self.api_status.construct_ok_data(ok_msg)
            return result
