class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeatingIndex = -1
        usedLetters = []
        usedLettersIndex = []
        subString = ""
        maxSubString = ""
        for i in range(0, len(s)):
            if s[i:i+1] in usedLetters:
                repeatingIndex = usedLettersIndex[usedLetters.index(s[i:i+1])]
                anotherIndex = usedLettersIndex.index(repeatingIndex)
                subString = subString[anotherIndex + 1 :] + s[i:i+1]
                usedLettersIndex = usedLettersIndex[anotherIndex + 1:] 
                usedLettersIndex.append(i)
                usedLetters = usedLetters[anotherIndex + 1:]
                usedLetters.append(s[i : i + 1])
                
            else:
                subString += s[i:i+1]
                usedLetters.append(s[i:i+1])
                usedLettersIndex.append(i)
            if len(subString) > len(maxSubString) :
                maxSubString = subString
            

        return len(maxSubString)