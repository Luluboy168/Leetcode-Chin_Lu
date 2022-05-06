class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #將每兩天相差的正值相加
        total = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                total += prices[i] - prices[i - 1]
        
        return total
