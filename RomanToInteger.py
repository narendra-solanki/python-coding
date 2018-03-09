class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #convert each roman numeral into its decimal equivalent
        romans = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        sum = 0
        
        """
        compare each roman numerals in pair
        if first character in pair is smaller, then subtract first number from final sum
        else add the number in final sum
        e.g. IV will be calculated as -1+5 = 4, in two iterations
        
        """
        for i in range(len(s)-1):
            if(romans[s[i]] < romans[s[i+1]]): #subtract first number from final sum
                sum = sum - romans[s[i]]
            else: #else just add the decimal equivalent in final sum
                sum = sum + romans[s[i]]
                
        return sum + romans[s[-1]]  #now add the last element     
        
        