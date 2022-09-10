# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Solution:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not n: return 0
        if k >= n // 2:
            return sum(i - j    for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        k = min(k, len(prices)//2)
        dp = [0]*len(prices)
        for x in range(k):
            val = 0
            for i in range(1, len(prices)):
                val = max(dp[i], val+prices[i]-prices[i-1])
                dp[i] = max(dp[i-1], val)
        return dp[-1]
        
# Verdict:
# Runtime: 194 ms, faster than 57.01% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 13.9 MB, less than 95.05% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
