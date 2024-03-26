class Solution:
    def trailingZeroes(self, n: int) -> int:
        numOfTwo = 0
        numOfFive = 0
        for i in range(2, n + 1):
            currNum = i
            while currNum % 2 == 0 and currNum is not 0:
                numOfTwo += 1
                currNum = currNum // 2
            while currNum % 5 == 0 and currNum is not 0:
                numOfFive += 1
                currNum = currNum // 5

        
            

        return min(numOfTwo, numOfFive)