NUM_SET = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
from tabulate import tabulate
from models import *

def pretty_print(users):
    headers = ['Name', 'Elo', 'Title', 'Last Active Date', 'Last Active Time']
    table = []

    for user in users:
        table.append([user.name, user.elo, user.title, user.last_active_date, user.last_active_time])

    print(tabulate(table, headers=headers))


def convert_sec_to_min(time):
    time_split = time.split('+')
    initial_sec = time_split[0]
    increment = time_split[1]
    if (time_split[0] == '180'):
        return '3 + ' + increment
    elif (time_split[0] == '60'):
        return '1 + ' + increment
    elif (time_split[0] == '30'):
        return '00:30 + ' + increment
    elif (time_split[0] == '15'):
        return '00:15 + ' + increment
    elif (time_split[0] == '300'):
        return '5 + ' + increment
    elif (time_split[0] == '600'):
        return '10 + ' +  increment
    else:
        return ''

def convertHHMM(time):
    hour, min, sec = time.split(":")
    return int(hour) * 60 * 60 + int(min) * 60 + int(sec)

def compareTime(date1, date2, time1, time2):
    if (date1 == date2):
        time1, time2 = convertHHMM(time1), convertHHMM(time2)
        if (time1 > time2):
            return False
        return True
    else:
        yy, mm, dd = date1.split(":")
        yy2, mm2, dd2 = date2.split(":")
        if int(yy) > int(yy2):
            return False
        if int(mm) > int(mm2):
            return False
        if int(dd) > int(dd2):
            return False
        return True