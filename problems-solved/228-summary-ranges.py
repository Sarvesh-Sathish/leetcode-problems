from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        retNums = []
        start = nums[0]
        interval = 1
        for i in range(1, len(nums)):
            if nums[i] == start + interval:
                interval += 1
                continue
            
            if interval == 1:
                retNums.append("" + str(start))
                start = nums[i]
            else:
                retNums.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
                interval = 1

        if interval == 1:
            retNums.append(str(start))
            return retNums
        elif len(nums) != len(retNums):
            retNums.append(str(start) + "->" + str(nums[len(nums) - 1]))

        return retNums