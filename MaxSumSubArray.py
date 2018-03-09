"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        At every index keep track of max sum till now
            - it will be either number[i] or number[i] + maxTillNow 
        Also store maximum of all maxTillNow values
        return maxTillNow value as result
        """
        maxSum = nums[0]
        maxTillNow = nums[0]
        for i in range(1, len(nums)):
            #maximum sum till now will be either (this number), or (max sum till now + this number)
            maxTillNow = max(nums[i], maxTillNow + nums[i])
            maxSum = max(maxTillNow, maxSum)
 
        return maxSum