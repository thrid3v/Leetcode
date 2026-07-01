class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxprof = 0
        while r <= len(prices) - 1:
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxprof = max(maxprof, diff)
            else:
                l = r
            r += 1
        return maxprof
        