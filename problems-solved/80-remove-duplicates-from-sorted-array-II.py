from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
    i = 0

    while (i + 1) < len(nums):
        j = i + 1
        print(nums)
        while j < len(nums):
            if j > i + 1 and nums[j] == nums[i]:
                nums.pop(j)
            elif j > i + 1:
                break
            elif nums[j] == nums[i]:
                j += 1
                continue
            else:
                break
        i = j 
    return len(nums)