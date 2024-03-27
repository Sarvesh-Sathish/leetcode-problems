class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True

        if len(s) > len(t):
            return False
        pointer = 0
        for i in range(0, len(t)):
            if t[i] == s[pointer]:
                pointer += 1

            if pointer == len(s):
                return True

        return False