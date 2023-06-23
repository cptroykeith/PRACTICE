class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] -prices[r]
                maxp = max(maxp, profit)
            else:
                l = r

            r += l

        return maxp