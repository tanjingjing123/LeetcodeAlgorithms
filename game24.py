class solution:
    def judgePoint24(self, nums):
        if len(nums) == 1:
            return round(nums[0], 4) == 24
        nums_len = len(nums)
        for left in range(nums_len - 1):
            for right in range(left + 1, nums_len):
                remain = nums[:left] + nums[left+1:right] + nums[right+1:]
                left_val, right_val = nums[left], nums[right]
                if self.judgePoint24(remain+[left_val+right_val]):
                    return True
                if self.judgePoint24(remain+[left_val - right_val]):
                    return True
                if self.judgePoint24(remain+[left_val * right_val]):
                    return True
                if right_val and self.judgePoint24(remain+[left_val/right_val]):
                    return True
                if self.judgePoint24(remain + [right_val - left_val]):
                    return True
                if left_val and self.judgePoint24(remain+[right_val/left_val]):
                    return True
        return False

nums = [ 2, 0, 4, 2, 1]
mywork = solution()
print(mywork.judgePoint24(nums))