#!/usr/bin/python3

import datetime

def print_working_days(date1, date2):
    # a = date 1
    a = datetime.date.fromisoformat(date1)
    # b = date 2
    b = datetime.date.fromisoformat(date2)
    delta = datetime.timedelta(days = 1)
    while a < b:
        if a.weekday() < 5:
            print(a.isoformat())
        a = a + delta

print('Dni pracujące:')
print_working_days('2022-02-03', '2022-02-15')
