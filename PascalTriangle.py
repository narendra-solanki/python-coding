"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        """
        for numRows = 1, value is [1]
        first and last column of every row is 1
        Each value in remaining columns is sum of elements from previous row index [row-1][j-1] + [row-1][j]        
        """

        triangle = []

        for i in range(numRows): #generate each row
            row = [None for _ in range(i+1) ] #initialize a row with None values
            row[0], row[-1] = 1, 1 #first and last element will be always 1

            for j in range(1, len(row)-1): #start from 1st index till penultimate index
                row[j] = triangle[i-1][j-1] + triangle[i-1][j] #sum of nearest elements from previous row
            triangle.append(row)

        return triangle
