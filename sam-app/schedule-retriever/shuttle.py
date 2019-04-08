import datetime
import numpy as np

def get_shuttle_schedule():
    today = datetime.datetime.now()

    year = today.year
    month = today.month
    date = today.day
    np.set_printoptions(threshold=np.inf)
    data = np.zeros((77, 18), dtype = 'datetime64[s]')
    start = datetime.datetime(year, month, date, 6, 30)
    increments = [0, 5, 5, 2, 2, 1, 5, 1, 1, 8, 5, 2, 1, 2, 1, 2, 2, 3]
    inc = True

    def next_row(start):
        nonlocal inc
        if start < datetime.datetime(year, month, date, 7, 19):
            return start + datetime.timedelta(minutes = 25)
        elif start > datetime.datetime(year, month, date, 21, 54):
            if start < datetime.datetime(year, month, date, 22, 19):
                return start + datetime.timedelta(minutes = 25)
            else:
                return start + datetime.timedelta(minutes=50)
        elif inc:
            inc = False
            return start + datetime.timedelta(minutes = 12)
        elif not inc:
            inc = True
            return start + datetime.timedelta(minutes = 13)
        else:
            raise Exception('this time is not being handled yet')

    for i in range(77):
        t = start
        for j, increment in enumerate(increments):
            if start.hour == 0 and start.minute == 50 and j == 9:
                break
            t = (t + datetime.timedelta(minutes = increment))
            data[i, j] = datetime.datetime(year, month, date, t.hour, t.minute)
        start = next_row(start)
    return data

