from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while (i + 1) < len(nums):
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)