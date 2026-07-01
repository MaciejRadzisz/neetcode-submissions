class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []
        profit = 0
        for i in range(len(prices)):
            currentPrice = prices[i]
            arr.append(currentPrice)
            if currentPrice - min(arr) > profit:
                profit = currentPrice - min(arr)
        return profit