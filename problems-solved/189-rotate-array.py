from typing import List
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    lastElem = []
    for i in range(len(nums) - k, len(nums)):
        lastElem.append(nums[i])

    lastIndex = len(nums) - 1
    for i in range(lastIndex, 0, -1):
        nums[i] = nums[i - k]

    for i in range(0, len(lastElem)):
        nums[i] = lastElem[i]