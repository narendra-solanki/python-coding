"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
        generate each row one by one
        first and last element in each row will be 1
        store only last generated row in triangle
        each column value will be sum of nearest elements from previous row (column j-1 and column j)

        """
        triangle = [1] #for 0th index
        for row_num in range(1, rowIndex+1): #start from 1st index
            row = [None for _ in range(row_num+1)] #generate k+1 elements in k(th) index
            row[0],row[-1] = 1,1 #first and last elements will always be 1

            for j in range(1, len(row)-1): #generate all elements between first and last element
                row[j] = triangle[j-1] + triangle[j]

            triangle = row
        return triangle
