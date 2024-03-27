class Solution:
    def reverseWords(self, s: str) -> str:
        words = ""
        initialSpaces = True
        currWord = ""
        for i in range(0, len(s)):
            if s[i] == ' ' and initialSpaces:
                continue
            
            if s[i] == ' ' and currWord != "":
                words = ' ' + words
                words = currWord + words
                currWord = ""
                

            if s[i] != ' ':
                initialSpaces = False
                currWord += s[i]

        if currWord != "":
            words = " " + words
            words = currWord + words 

        if words[len(words) - 1] == ' ':
            return words[0:len(words) - 1]
        return words
                




    