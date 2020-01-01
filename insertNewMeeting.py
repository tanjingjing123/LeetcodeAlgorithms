def canSchedual(meetings, start, end):
    for meeting in meetings:
        if (end > meeting[0] and end <=meeting[1]) or (start >= meeting[0] and start < meeting[1]) or (start <= meeting[0] and end >= meeting[1]):
            return False

    return True

meetings = [[1300, 1500], [930, 1200],[830, 845]]
start = 1200
end = 1300
print(canSchedual(meetings, start, end))