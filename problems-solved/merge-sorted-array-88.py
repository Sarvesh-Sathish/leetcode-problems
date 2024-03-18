from typing import List
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # Edge Case where each list has only one element
    if (m + n) == 1:
        if m == 1:
            return
        else:
            nums1.insert(0,nums2[0])
            nums1.pop()

    j = 0
    firstIsFull = False
    lastFirst = 0
    for i in range(len(nums1)):
        # Check if j is full
        if j == len(nums2):
            break

        # Check if i is full but j is not full
        if lastFirst == m:
            firstIsFull = True
            lastFirst = i
            break

        # Assumption both are not full
        if nums2[j] < nums1[i]:
            nums1.insert(i, nums2[j]) # Insert at index
            nums1.pop() # Remove lastValue
            i -= 1
            j += 1
        else:
            lastFirst += 1

    if firstIsFull:
        for k in range(lastFirst, len(nums1)):
            nums1[k] = nums2[j]
            j += 1


