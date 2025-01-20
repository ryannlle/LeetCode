class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_diff = 0
        small = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < small:
                small = prices[i]
            if (prices[i] - small) > max_diff:
                max_diff = prices[i] - small


        return max_diff
