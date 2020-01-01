def canAssignNewMeeting(meetings, new):
    for meeting in meetings:
        if (meeting[0] <= new[0] and meeting[1] > new[0]) or (meeting[0] < new[1] and meeting[1] >= new[1]):
            return False
        continue

    return True

meetings = [[1300,1500],[930,1200],[830,845]]
new = [820, 830]
print(canAssignNewMeeting(meetings, new))