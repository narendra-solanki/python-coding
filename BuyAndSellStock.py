"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        loop through all the prices in array
        keep track of min value so far and maxprofit so far
        """
        if not prices:
            return 0
        minTillNow = prices[0]
        maxprofit = 0
        for price in prices[1:]:
            minTillNow = min(minTillNow, price) #get the minimum price till now
            maxprofit = max(maxprofit, price - minTillNow) #get max profit till now

        return maxprofit
