class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ""
        wordNotStarted = True
        for i in range(len(s) - 1, - 1, - 1):
            if s[i] is " " and not wordNotStarted:
                break
            if s[i] is not " ":
                wordNotStarted = False
                word += s[i]

        return len(word)