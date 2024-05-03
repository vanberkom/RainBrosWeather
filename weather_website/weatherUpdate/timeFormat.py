def timeFormatter(time):
    time1 = time + 1
    time2 = time + 2
    time3 = time + 3
    time4 = time + 4
    if time1 >= 24:
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
    elif time2 >= 24:
        time1 = 23
        time2 = 0
        time3 = 1
        time4 = 2
    elif time3 >= 24:
        time1 = 22
        time2 = 23
        time3 = 0
        time4 = 1
    elif time4 >= 24:
        time1 = 21
        time2 = 22
        time3 = 23
        time4 = 0
    return str(time), str(time1), str(time2), str(time3), str(time4)

