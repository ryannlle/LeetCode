class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if low < prices[i]:
                profit += prices[i] - low
            low = prices[i]

        return profit