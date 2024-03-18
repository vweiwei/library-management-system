from Model.Service.AccountService import AccountService
from Utils.APIStatus import APIStatus


class AccountController:

    def __init__(self):
        self.service = AccountService()
        self.api_status = APIStatus()

    def student_login(self, username, passwd):
        if username is None or passwd is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.student_login_service(username, passwd)
        if service_result["data"] is None:
            ok_msg = {"login_status": 0, "login_msg": service_result["msg"], "data": service_result["data"]}
            result = self.api_status.construct_ok_data(ok_msg)
            return result
        else:
            print(service_result)
            ok_msg = {"login_status": 1, "login_msg": service_result["msg"], "data": service_result["data"]}
            result = self.api_status.construct_ok_data(ok_msg)
            return result

    def admin_login(self, username, passwd):
        if username is None or passwd is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result

        service_result = self.service.admin_login_service(username, passwd)
        if service_result["data"] is None:
            ok_msg = {"login_status": 0, "login_msg": service_result["msg"], "data": service_result["data"]}
            result = self.api_status.construct_ok_data(ok_msg)
            return result
        else:
            ok_msg = {"login_status": 1, "login_msg": service_result["msg"], "data": service_result["data"]}
            result = self.api_status.construct_ok_data(ok_msg)
            return result

    def sign_up(self, username, passwd, name, email):
        if username is None or passwd is None or name is None or email is None:
            result = self.api_status.construct_error_data(self.api_status.param_null)
            return result
        else:
            service_result = self.service.sign_up_service(username, passwd, name, email)
            ok_msg = {"sign_up_status":  service_result["status"], "sign_up_msg": service_result["msg"]}
            result = self.api_status.construct_ok_data(ok_msg)
            return result


