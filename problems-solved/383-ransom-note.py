class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(0, len(ransomNote)):
            print(ransomNote[i])
            if ransomNote[i] in magazine:
                remIndex = magazine.index(ransomNote[i])
                if len(ransomNote) == len(magazine) and len(ransomNote) ==1:
                    return True
                elif remIndex == len(magazine) - 1:
                    magazine = magazine[:len(magazine) - 1]
                else:
                    magazine = magazine[0:remIndex] + magazine[remIndex + 1:]
            else:
                return False

        return True