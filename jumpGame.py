def canJump(nums):
    if len(nums) == 1:
        return True
    idx_max = rest = nums[0]
    if rest <= 0:
        return False
    for idx, jumps in enumerate(nums[1:-1], start=1):
        idx_max = max(idx_max, idx + jumps)
        
nums = [2,3,1,1,4]
print(canJump(nums))