"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        """
        Merge both the arrays in a third list
            merge only till mid element is reached
        if combined length of two arrays is even 
            then return average of last 2 elements
        else
            return last element
        """
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        #get index of median element
        #for odd length, it will be last element
        #for even length it will be avg of last 2 elements
        midElem = totalLen//2 + 1        
        
        #create a new array to store merged array
        mergedArray = []
        i,j = 0,0
        for k in range(midElem): #get elements till midElement of merged array         
            if i < len1 and j < len2:
                mergedArray.append(min(nums1[i],nums2[j]))
                if nums1[i] < nums2[j]:
                    i+=1
                else:
                    j+=1                
            elif i < len1:
                mergedArray.append(nums1[i])
                i+=1
            elif j < len2:
                mergedArray.append(nums2[j])
                j+=1

        print(mergedArray)
        if totalLen%2 == 0: #even length dataset
            median = (mergedArray[-1] + mergedArray[-2])/2
        else:
            median = mergedArray[-1]
        
        return median
        