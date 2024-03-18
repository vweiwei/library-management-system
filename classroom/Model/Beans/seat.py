class Seat:
    def __init__(self, idx, name, is_special, classroom):
        self.idx = idx
        self.name = name
        self.is_special = is_special
        self.classroom = classroom
        self.preserve_list = []

    def construct_dict(self):
        return {"id": str(self.idx),
                "name": self.name,
                "is_special": self.is_special,
                "classroom": str(self.classroom),
                "pre_list": self.preserve_list}
