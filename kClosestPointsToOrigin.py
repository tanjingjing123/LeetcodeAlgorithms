import math
import heapq


def kClosest(points, K):
    maxHeap = []
    answer = []
    distance = []
    for point in points:
        distance.append([point[0] ** 2 + point[1] ** 2, point])
    for i in range(K):
        # -1 is multiplied to convert minHeap to maxHeap
        heapq.heappush(maxHeap, [-1 * distance[i][0], distance[i][1]])
    for i in range(K, len(points)):
        max_distance = -1 * (maxHeap)[0][0]
        if distance[i][0] < max_distance:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, [-1 * distance[i][0], distance[i][1]])

    for i in range(len(maxHeap)):
        answer.append(maxHeap[i][1])
    return answer

points = [[3,3],[5,-1],[-2,4],[4,3],[3,2],[5,2]]
K = 3
print(kClosest(points, K))