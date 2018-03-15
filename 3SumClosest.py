"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
            1. First sort the array
            2. Anchor each element and create a triplet with next element and last element in the array
            3. if sum == target then we have found our sum
            4. adjust closest sum till now
            5. if sum < target, then we will compare with next larger element in the list from left
            6. if sum > target, then we will compare with next smaller element in the list from right

        """
        #length is not atleast 3 then, there is bad input
        length =  len(nums)
        if length < 3:
            return
        
        nums.sort() #first sort the array
        #initialize result with any arbitrary triplet
        result = nums[0] + nums[1] + nums[2];

        for i in range(length - 2):
            left, right = i+1, length-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right] #get sum of the triplet
                if sum == target:
                    return sum
                #update the closest sum
                if abs(sum-target) < abs(result-target):
                    result = sum

                if sum < target:
                    left+=1
                elif sum > target:
                    right-=1
        return result
