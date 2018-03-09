"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #first remove all spaces
        string = s.strip()
        #check for empty string
        if not string:
            return 0
        
        if len(string) == 1:
            return 1
        count = 0
        #iterate the string in reverse order
        for char in string[::-1]:
            if char == ' ':  #break the loop if we have reached a space character               
                break
            count+=1       
        return count
    
    """
    this is the easy solution
    Split the stripped string and return length of last word
    """
    def lengthOfLastWord1(self,s):
        array = s.strip().split()
        if not array:
            return 0
        
        return len(array[-1])