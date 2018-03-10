"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and 
ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. 
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31-1  
        INT_MIN = -2**31
        str = str.strip()
        if not str:
            return 0

        #determine sign of the number
        sign = -1 if str[0] == '-' else 1
        plussign = True if str[0] == '+' else False
        
        #remove the sign of number
        if (sign == -1 or plussign) and len(str) > 1:
            str = str[1:]
            
        num = 0
        for i in range(len(str)): #compute the number till non-digit character is found
            char = str[i]
            digit = ord(char) - 48
            if digit < 0 or digit > 9:
                break
            #now check if integer will overflow in next calculation
            if num > INT_MAX//10 or (num == INT_MAX//10 and digit > INT_MAX%10):
                return INT_MAX if sign > 0 else INT_MIN
            
            num = num*10 + digit
        
        return sign*num
