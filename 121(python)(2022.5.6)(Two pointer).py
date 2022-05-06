class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Two pointer
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentprofit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentprofit, max_profit)
            else:
                left = right
            right += 1
            
        return max_profit
