def maxScore(cardPoints, k):
    leftsum = 0
    rightsum = 0
    left = k - 1
    maximum = 0
    right = len(cardPoints) - 1

    for i in range(0, k):
        leftsum = leftsum + cardPoints[i]
    maximum = leftsum
    while left >= 0:
        leftsum = leftsum - cardPoints[left]
        rightsum = rightsum + cardPoints[right]
        left = left - 1
        right = right - 1
        maximum = max(maximum, leftsum + rightsum)

    return maximum


cardPoints = [2,2,3,4,7,5,5,7,1]
k = 3
print(maxScore(cardPoints, k))