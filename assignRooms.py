import collections


def canAssign(meetings, rooms):
    roomMeetingMap = collections.defaultdict(list)

    for meeting, mValue in meetings.items():
        for room, rValue in rooms.items():
            if rValue["size"] >= mValue["size"]:
                roomMeetingMap[room].append([meeting, mValue["start"], mValue["end"]])

    resultMap = {}
    roomList = []

    for room in rooms:
        roomList.append(room)
        # roomMeetingMap[room].sort(key=lambda x:x[1])

    def dfs(roomIndex, meetingIndex, lastEnd):
        if len(resultMap) == len(meetings):
            return True
        if roomIndex == len(roomList):
            return False
        curRoom = roomList[roomIndex]
        meetingList = roomMeetingMap[curRoom]
        if meetingIndex == len(meetingList):
            return dfs(roomIndex + 1, 0, -1)

        for i in range(meetingIndex, len(meetingList)):
            if meetingList[i][0] in resultMap or meetingList[i][1] < lastEnd:
                continue
            resultMap[meetingList[i][0]] = curRoom
            if dfs(roomIndex, i + 1, meetingList[i][2]):
                return True
            del resultMap[meetingList[i][0]]

        return False

    if not dfs(0, 0, -1):
        print("Impossible!")
    else:
        print(resultMap)


meetings = {"Manager 1:1": {"size": 2, "start": 900, "end": 1030},
            "Budget": {"size": 4, "start": 900, "end": 1000},
            # "Forecasting": {"size": 8, "start": 900, "end": 1100},
            "SVP 1:1": {"size": 2, "start": 1000, "end": 1030},
            "UX Testing": {"size": 4, "start": 1015, "end": 1130}}
rooms = {"Phone Booth": {"size": 2},
         "War Room": {"size": 6},
         "Conference Room": {"size": 12}}

canAssign(meetings, rooms)
