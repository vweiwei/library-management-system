class Preserve:
    def __init__(self, idx, stu_id, seat_id, start_time, end_time):

        self.idx = idx
        self.stu_id = stu_id
        self.seat_id = seat_id
        self.start_time = start_time
        self.end_time = end_time
        self.is_check_in = False

    def construct_dict(self):
        return {"id": self.idx, "start_time": self.start_time, "end_time": self.end_time}