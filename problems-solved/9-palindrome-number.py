class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        j = len(strX) - 1
        for i in range(0, len(strX)):
            if strX[i] != strX[j]:
                return False
            j -= 1

        return True