from typing import List

def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    minValue = prices[0]
    profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        if prices[i] < minValue:
            minValue = prices[i]
        elif prices[i] - minValue > profit:
            profit = prices[i] - minValue

    if profit <= 0:
        return 0
    return profit