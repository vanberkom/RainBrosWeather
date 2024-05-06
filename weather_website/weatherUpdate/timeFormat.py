def timeFormatter(time):
    time1 = time + 1
    time2 = time + 2
    time3 = time + 3
    time4 = time + 4
    time5 = time + 5
    if time1 >= 24:
        time1 = 0
        time2 = 1
        time3 = 2
        time4 = 3
        time4 = 4
    elif time2 >= 24:
        time1 = 23
        time2 = 0
        time3 = 1
        time4 = 2
        time5 = 3
    elif time3 >= 24:
        time1 = 22
        time2 = 23
        time3 = 0
        time4 = 1
        time5 = 2
    elif time4 >= 24:
        time1 = 21
        time2 = 22
        time3 = 23
        time4 = 0
        time5 = 1
    elif time5 >= 24:
        time1 = 20
        time2 = 21
        time3 = 22
        time4 = 23
        time5 = 0
    return str(time), str(time1), str(time2), str(time3), str(time4)

