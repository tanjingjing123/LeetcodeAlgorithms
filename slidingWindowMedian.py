import bisect
def medianSlidingWindow(nums, k):
    res = []
    window = sorted(nums[:k][:])
    for i in range(k, len(nums) + 1):
        if k % 2:
            res.append(window[len(window)//2])
        else:
            res.append((window[len(window)//2 - 1] + window[len(window)//2])/2)
        if i < len(nums):
            window.remove(nums[i-k])
            bisect.insort(window, nums[i])

nums = [1,3,-1,6,2,5,4,-1,6,-2,4,3]
print(medianSlidingWindow(nums, k=4))