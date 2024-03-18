from Model.DAO.AccountDAO import AccountDAO
from Model.DAO.StudentDAO import StudentDAO


class AccountService:

    def __init__(self):
        self.acc_dao = AccountDAO()
        self.stu_dao = StudentDAO()

    def student_login_service(self, username, passwd):
        account = self.acc_dao.select_one_student_account_by_name(username)
        if account is None:
            return {"msg": "账号不存在", "data": None}
        else:
            if account.passwd == passwd:
                uid = account.uid
                student = self.stu_dao.select_one_student_by_id(uid)
                if student is None:
                    return {"msg": "登陆失败", "data": "账号与学生关联失败！"}
                else:
                    return {"msg": "登陆成功", "data": student.construct_dict()}
            else:
                return {"msg": "密码错误", "data": None}

    def admin_login_service(self, username, passwd):
        account = self.acc_dao.select_one_admin_account_by_name(username)
        if account is None:
            return {"msg": "账号不存在", "data": None}
        else:
            if account.passwd == passwd:
                return {"msg": "登陆成功", "data": 1}
            else:
                return {"msg": "密码错误", "data": None}

    def sign_up_service(self, username, passwd, name, email):
        status = self.acc_dao.create_one_student_account(username, passwd, name, email)
        if status:
            return {"status": 1, "msg": "注册成功！"}
        else:
            return {"status": 0, "msg": "注册失败！"}
