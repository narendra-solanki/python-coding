"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """
        iterate List from the end
        make all the 9s to 0 till a number less tha 9 is found
        if number is less than 9 then add 1 and break the loop
        if loop has exited without any break, 
            it means there were all 9s in the number and overflow has occured
            so we will have to append a 1 at the start of the list
        """
        for i in range(len(digits)-1, -1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i]+=1
                break
        else:
            digits.insert(0,1)
        
        return digits