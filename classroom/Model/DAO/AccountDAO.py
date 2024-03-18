from Utils.Database import MongoConnection
from Model.Beans.account import StudentAccount, AdminAccount


class AccountDAO:

    def __init__(self):
        self.connection = MongoConnection()

    @staticmethod
    def construct_student_account_meta_data(meta_data):
        idx = meta_data["_id"]
        username = meta_data["username"]
        passwd = meta_data["passwd"]
        uid = meta_data["uid"]

        return StudentAccount(idx, username, passwd, uid)

    @staticmethod
    def construct_admin_account_meta_data(meta_data):
        idx = meta_data["_id"]
        username = meta_data["username"]
        passwd = meta_data["passwd"]

        return AdminAccount(idx, username, passwd)

    def select_one_student_account_by_name(self, username):
        try:
            account_meta = self.connection.db["s_account"].find_one({"username": username})
            if account_meta is None:
                return None
            else:
                account = self.construct_student_account_meta_data(account_meta)
                return account
        except Exception as e:
            print("Select student account failed !", e)
            return None

    def select_one_admin_account_by_name(self, username):
        try:
            account_meta = self.connection.db["a_account"].find_one({"username": username})
            print(account_meta)
            if account_meta is None:
                return None
            else:
                account = self.construct_admin_account_meta_data(account_meta)
                return account
        except Exception as e:
            print("Select admin account failed !", e)
            return None

    def create_one_student_account(self, username, passwd, name, email):
        try:
            account_data = {"username": username, "passwd": passwd}

            context_a = self.connection.db["s_account"].insert_one(account_data)
            a_id = context_a.inserted_id

            student_data = {"name": name, "email": email, "preserve": list(), "violate": 0}
            context_s = self.connection.db["student"].insert_one(student_data)
            uid = context_s.inserted_id

            context_s_u = self.connection.db["s_account"].update_one({"_id": a_id}, {"$set": {"uid": uid}})
            return True
        except Exception as e:
            print("Account insert failed !", e)
            return False
