
def maxArea(height):
    left = 0
    right = len(height) - 1
    max_val = 0
    n = len(height)
    while left < right:
        area = min(height[left], height[right]) * (n - 1)
        max_val = max(max_val, area)
        if height[left] <= height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
        n -= 1
    return max_val

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
