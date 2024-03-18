class Classroom:
    def __init__(self, idx, name, start_time, end_time):

        self.idx = idx
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def construct_dict(self):
        return {"id": str(self.idx), "name": self.name, "start_time": self.start_time, "end_time": self.end_time}


