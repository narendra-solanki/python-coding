"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #if all bits are zero than reverse is the same number
        if not n:
            return n

        result = 0
        #get LSB from the input number one by one and append at the end in result
        for i in range(32):
            #make space for next bit at last position
            result = result<<1
            #if last bit in n is 1 then append it to result else leave it 0
            if n&1 == 1:
                result+=1
            #remove LSB from the result
            n = n>>1
        return result
