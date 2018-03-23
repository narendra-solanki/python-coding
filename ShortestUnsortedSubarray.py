"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        From left find last element which breaks the ascending order of elements
            - keep track of max_element from left
            - if any element(which comes after max_element) is smaller than max_element then mark its index

        From right find last element which breaks the descending order of elements
            - keep track of min_element from right
            - if any element(which comes after min_element) is larger than min_element then mark its index
        """
        end = 0
        maxi = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < maxi:
                end = i
            else:
                maxi = max(maxi, nums[i])
        if end == 0: #if array is already sorted then return 0
            return 0

        start = 0
        mini = nums[-1]
        for j in reversed(range(len(nums)-1)):
            if nums[j] > mini:
                start = j
            else:
                mini = min(mini, nums[j])

        return end-start+1
