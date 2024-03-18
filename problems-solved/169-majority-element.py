from typing import List

def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[int(len(nums) / 2)]