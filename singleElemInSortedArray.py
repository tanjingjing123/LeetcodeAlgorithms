def singleNonDuplicate(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if mid % 2:
            if nums[mid] == nums[mid-1]:
                low = mid + 1
            elif nums[mid] == nums[mid+1]:
                high = mid - 1
            else:
                return nums[low]
        else:
            if nums[mid] == nums[mid+1]:
                low = mid
            elif nums[mid] == nums[mid-1]:
                high = mid
            else:
                return nums[mid]
    return nums[low]

def singleNonDuplicate2(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        leftFlag = False
        if nums[mid] == nums[mid - 1]:
            leftFlag = True
        elif nums[mid] != nums[mid + 1]:
            return nums[mid]

    return nums[low]




nums = [1,8,8]
print(singleNonDuplicate(nums))