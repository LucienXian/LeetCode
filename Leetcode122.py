class Solution(object):
    def maxProfit(self, prices):
        return sum(max(0, prices[i+1]-prices[i]) for i in range(len(prices)-1))