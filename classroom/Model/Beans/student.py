
class Students:
    def __init__(self, idx, name, email, violate):
        self.idx = idx
        self.name = name
        self.email = email
        self.violate = violate
        self.preserve_list = []

    def construct_dict(self):
        return {"id": str(self.idx),
                "name": self.name,
                "email": self.email,
                "violate": self.violate,
                "pre_list": self.preserve_list}
