class Solution(object):
    def maxProfit(self, prices):
        minCost, maxPro = 10000000, 0
        for price in prices:
            minCost = min(price, minCost)
            maxPro = max(maxPro, price-minCost)
        return maxPro