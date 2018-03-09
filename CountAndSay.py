"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #base case
        if(n == 1):
            return "1"

        #initial string marked with $ at the end, $ will ensure traversal of full string
        inputString = "1$"
        for i in range (2, n+1): #generate string for each step till n
            nextString = ""
            count = 1 #initial count is 1, since we are on next character, hence the character is counted already
            for j in range(1, len(inputString)): #run loop from 2nd character
                if inputString[j-1] != inputString[j]: #if this char and previous char do not match
                    nextString+= str(count) + str(inputString[j-1]) #then append the count of previous characters
                    count = 1 #reset the counter for next unique character
                else:
                    count+=1 #chars are same so increase the counter
            inputString = nextString + "$" #create string for next step            
            
        return nextString