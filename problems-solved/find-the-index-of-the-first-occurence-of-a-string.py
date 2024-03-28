class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for i in range(0, len(haystack) - len(needle) + 1):
            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                     break
                    
                if j == len(needle) - 1:
                    return i


        return -1