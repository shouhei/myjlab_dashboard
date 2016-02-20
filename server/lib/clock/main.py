import time
from .timetable import TimeTable

if __name__ == "__main__":
    now = time.localtime()
    for row in TimeTable.list():
        if row.is_near_start(now):
            message = ""
        else if row.is_near_end(now):
            message = ""
    if message :
        
