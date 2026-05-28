class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## dynamic programming, wally came along
        minBuy = prices[0]
        maxP = 0

        for sell in prices:
            maxP = max(
                sell - (minBuy := min(minBuy,sell)), maxP
            )
        return maxP