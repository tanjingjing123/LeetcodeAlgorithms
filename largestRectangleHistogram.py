def largestRectangleArea(heights):
    stack = []
    maxA = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            pos = stack.pop()
            if stack:
                area = heights[pos] * (i - stack[-1] - 1)
                maxA = max(maxA, area)
            else:
                area = heights[pos] * (i - 0)
                maxA = max(maxA, area)
        stack.append(i)

    while stack:
        pos = stack.pop()
        if stack:
            area = heights[pos]*(len(heights) - stack[-1] - 1)
            maxA = max(maxA, area)
        else:
            area = heights[pos]*(len(heights) - 0)
            maxA = max(maxA, area)
    return maxA

heights = [2, 3, 4, 1, 5, 6, 8, 2, 4, 3]
print(largestRectangleArea(heights))