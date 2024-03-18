class Account:
    def __init__(self, idx, username, passwd):
        self.id = idx
        self.username = username
        self.passwd = passwd


class StudentAccount(Account):
    def __init__(self, idx, username, passwd, uid):
        super(StudentAccount, self).__init__(idx, username, passwd)
        self.uid = uid


class AdminAccount(Account):
    def __init__(self, idx, username, passwd):
        super(AdminAccount, self).__init__(idx, username, passwd)
