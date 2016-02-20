import time

class TimeTableCell:
    def __init__(self, start, end):
        self.__start = time.strptime(start, "%H:%M")
        self.__end = time.strptime(end, "%H:%M")

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def is_near_start(self, now):
        diff_hour = self.__start.tm_hour - now.tm_hour
        diff_min = (diff_hour * 60) - (self.__start.tm_min - now.tm_min)
        return 0 < diff_min < 5

    def is_near_end(self, now):
        diff_hour = self.__end.tm_hour - now.tm_hour
        diff_min = (diff_hour * 60) - (self.__end.tm_min - now.tm_min)
        return 0 < diff_min < 5


class TimeTable:
    __list_ = [
        TimeTableCell("9:00", "10:30"),
        TimeTableCell("11:00", "12:30"),
        TimeTableCell("13:25", "14:55"),
        TimeTableCell("15:10", "16:40"),
        TimeTableCell("16:55", "18:25")
    ]

    @classmethod
    def list(cls):
        return cls.__list
