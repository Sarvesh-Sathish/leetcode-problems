class Solution:
    def isHappy(self, n: int) -> bool:
        existingNumbers = []
        currNum = n
        while True:
            print(existingNumbers)
            if currNum == 1:
                break

            if currNum in existingNumbers:
                return False

            existingNumbers.append(currNum)
            currNum = self.digitSum(currNum)    
            

        return True

    def digitSum(self, n):
        sum = 0
        while n > 0:
            sum += int(pow(n % 10, 2))
            n = int(n/10)
        return sum