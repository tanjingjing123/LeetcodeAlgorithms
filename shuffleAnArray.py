import random

import numpy as np
class solution:
    def __init__(self, nums):
        self.nums = nums



    def reset(self):
        return self.nums



    def shuffle(self):
        return random.sample(self.nums, len(self.nums))




nums = [1, 2, 2, 3, 3]
obj = solution(nums)
print(obj.shuffle())

