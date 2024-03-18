from Model.DAO.StudentDAO import StudentDAO


class StudentService:

    def __init__(self):
        self.stu_dao = StudentDAO()

    def student_detail_service(self, stu_idx):
        student = self.stu_dao.select_one_student_by_id(stu_idx)
        if student is None:
            return {"msg": "按id获取学生信息失败", "data": None}

        return {"msg": "ok", "data": student.construct_dict()}


