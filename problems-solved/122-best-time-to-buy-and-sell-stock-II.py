from typing import List
def maxProfit(self, prices: List[int]) -> int:
    minValue = prices[0]
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > minValue:
            profit += prices[i] - minValue
        minValue = prices[i]
    
    if profit <= 0:
        return 0
    return profit