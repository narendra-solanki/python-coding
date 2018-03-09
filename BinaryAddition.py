"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #first make length of both binary strings same by appending zeroes
        while len(a) != len(b):
            if len(a) < len(b):
                a = "0"+ a
            elif len(b) < len(a):
                b = "0"+ b
        output = ""
        carry = 0
        for i in range(len(a)-1,-1,-1):
            #implement full adder logic
            result = int(a[i]) ^ int(b[i]) ^ carry #lsb after addition 
            carry = (int(a[i]) & int(b[i])) | (int(b[i]) & carry) | (carry & int(a[i])) #output carry
            output+=str(result)
        #if there is an output carry after adding MSBs
        if carry:
            output+="1"
            
        #return reversed string                                                      
        return output[::-1]