from typing import List

def canJump(self, nums: List[int]) -> bool:
    currPos = 0
    val = nums[currPos]
    while currPos < len(nums) - 1:
        currPos += 1
        val -= 1
        if val < 0:
            return False
        
        if nums[currPos] > val:
            val = nums[currPos]

    return val >= 0
