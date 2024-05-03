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
    formatted_dates = []
    for i, day in enumerate(ordered_days):
        date_offset = datetime.timedelta(days=i)
        current_date = today + date_offset
        formatted_date = current_date.strftime("%A, %B %d")
        formatted_dates.append(f"{formatted_date}")
    return formatted_dates
