#!/usr/bin/env python3
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
            1. first sort the array, so that negative elements are near the start and positive near the end
            2. anchor each element and move two pointers, one from next element and another from last element
            3. Sum the 3 elements, if sum < 0, then move left pointer ahead, if sum > 0, then move right pointer backward
            4. If sum is zero,
                - append the triplet to result array
                - skip all elements which are duplicate to the left and right pointers so that we get only unique triplets
                - increase left index, decrease right index to compare next triplet


        """
        #first sort all the numbers
        nums.sort()
        result = []
        for i in range(len(nums)-2): #there should be atleast one triplet
            if i >= 1 and nums[i] == nums[i-1]: #skip all duplicate elements but the last
                continue

            left, right = i+1, len(nums)-1 #initialize next elements other than itself
            #run while loop for every element
            while left < right:
                sum = nums[i] + nums[left] + nums[right] #get the sum and check if its zero
                if sum > 0: #sum is greater it means we need to get rid of largest positive element
                    right-=1
                elif sum < 0: #sum is smaller it means we need to get rid of smallest negative element
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]]) #append the triplet
                    while (right > left) and nums[left] == nums[left+1]: #reach to the last duplicate element from left
                        left+=1
                    while (right > left) and nums[right] == nums[right-1]: #reach to the last duplicate element from right
                        right-=1
                    #move on to next pair of elements
                    left+=1
                    right-=1

        return result
