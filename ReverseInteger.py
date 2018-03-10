"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #compute MAX and MIN range for integer
        MAX = 2**31-1
        MIN = -2**31+1
        sign = -1 if x < 0 else 1        
        x = x*sign #make the number positive for calculation purpose
        rev = 0
        while x > 0:
            digit = x%10 #get last digit
            x = x//10 #remove last digit from next number            
            #now check if integer will overflow in next iteration
            if rev > MAX//10 or (rev == MAX//10 and digit > MAX%10):
                return 0            
            rev = rev*10 + digit #compute the reverse number at every step
        return rev *sign