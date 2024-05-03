# Used to find high and low temp for the day.
def high_low(temp1, temp2):
    if temp1 > temp2:
        return temp1,temp2
    else:
        return temp2, temp1

import datetime

def getDays():
    today = datetime.datetime.today()
    weekday = today.weekday()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ordered_days = days_of_week[weekday:] + days_of_week[:weekday]
    return ordered_days
