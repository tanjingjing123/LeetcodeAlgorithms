import heapq
def findKthLargest(nums, k):
    l = 0
    r = len(nums) - 1
    def place_at_correct(in_pos, l, r):
        pivot = nums[in_pos]
        nums[in_pos], nums[l] = nums[l], nums[in_pos]
        border, first_pos = l, l
        l = l + 1
        while l <= r:
            if nums[l] <= pivot:
                border += 1
                nums[border], nums[l] = nums[l], nums[border]
            l += 1
        nums[first_pos], nums[border] = nums[border], nums[first_pos]
        return border

    while True:
        in_pos = (l + r) // 2
        correct_pos = place_at_correct(in_pos, l, r)
        if correct_pos == len(nums) - k:
            return nums[correct_pos]
        elif correct_pos > len(nums) - k:
            r = correct_pos - 1
        else:
            l = correct_pos + 1


nums = [3,2,3,6,2,7,5,5,1]
k = 4
print(findKthLargest(nums, k))