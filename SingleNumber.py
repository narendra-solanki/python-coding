"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Make exclusive or of all the numbers
        all duplicate pairs will cancel each other
        """
        result = nums[0]
        for num in nums[1:]:
            result=result^num
        return result
