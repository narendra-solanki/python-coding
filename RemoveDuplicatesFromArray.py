"""
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        If this element is equal to next element then skip the element
        else copy this element in the array (maintain a new index counter for copied elements)
        This solution can be seen as if we are copying unique elements in a new array but
        actually we are copying elements in same array
        """
        
        if not nums:
            return 0
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]: #values are not equal, it means element is not duplicate
                nums[k] = nums[i] #copy the element
                k+=1
        #copy the last element in the array
        nums[k] = nums[-1]
        
        #now return the length of new array
        return k+1