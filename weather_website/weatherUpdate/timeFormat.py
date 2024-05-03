def timeFormatter(time):
    time1 = ''
    time2 = ''
    time3 = ''
    time4 = ''
    if (time + 1) == 24:
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
    elif (time + 2) == 24:
        time1 = 23
        time2 = 0
        time3 = 1
        time4 = 2
    elif (time + 3) == 24:
        time1 = 22
        time2 = 23
        time3 = 0
        time4 = 1
    elif (time + 4) == 24:
        time1 = 21
        time2 = 22
        time3 = 23
        time4 = 0
    elif (time + 2) == 24:
        time1 = 20
        time2 = 21
        time3 = 22
        time4 = 23
    return time, time1, time2, time3, time4
