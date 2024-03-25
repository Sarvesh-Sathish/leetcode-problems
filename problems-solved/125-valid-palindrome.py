class Solution:
    def isPalindrome(self, s: str) -> bool:
        # j = len(s) - 1
        # for i in range(0, int(len(s) / 2)):
        #     if s[i] >= 65
        #     if s[i] != s[j]:
        #         return False
        #     j -= 1

        # return True
        s = s.lower()
        listS = list(s)
        firstStr = ""
        secondStr = ""
        for i in range(0, len(s)):
            if listS[i].isalpha() or listS[i].isnumeric():
                firstStr += listS[i]
        for i in range(len(s) - 1, -1, -1):
            if listS[i].isalpha() or listS[i].isnumeric():
                secondStr += listS[i]
        
        print(firstStr, ' ', secondStr)
        return firstStr == secondStr