"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        For each element
            subtract element from target to get diff
            check if diff value exist in next elements
        
        """
        result = [-1,-1]
        for i, num in enumerate(nums):
            diff = target - num
            result[0] = i
            for j in range(i+1, len(nums)):            
                if nums[j] == diff:
                    result[1] = j
                    return result
                    
        return result