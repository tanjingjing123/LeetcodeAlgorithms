import bisect


def minTicketscOST(days, costs):
    D = [0] * (days[-1] + 1)
    for i in range(len(days)):
        day = days[i]
        D[day] = D[day-1] + costs[0]
        for cost, length in zip(costs, [1,7,30]):
            if day - length >= 0:
                D[day] = min(D[day - length] + cost, D[day])
            else:
                D[day] = min(D[day], cost)

        if i + 1 < len(days):
            next_day = days[i+1]
            for i in range(day+1, next_day):
                D[i] = D[day]
    return D[-1]



days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(minTicketscOST(days, costs))