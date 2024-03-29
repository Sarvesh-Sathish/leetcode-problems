from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10

            if carry == 0:
                return digits
            
        if carry == 1:
            digits.insert(0, carry)
        return digits