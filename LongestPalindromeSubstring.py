"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
 

Example:

Input: "cbbd"

Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxlength = 0
        self.startIndex = -1
        
        for i in range(len(s)):
            self._extendPalindrome(s, i, i) #check for odd length palindromes
            self._extendPalindrome(s, i, i+1) #check for even length palindromes
        
        return s[self.startIndex: self.startIndex+self.maxlength]
                
        
        
    def _extendPalindrome(self, s, left, right):
        while (left >= 0 and right < len(s)) and s[left] == s[right]:
            left-=1
            right+=1
        length = right-left-1 #since left/right are one step backward/forward of actual palindrome substring
        #if new palindrome length is maximum then update its start index and length
        if length > self.maxlength:
            self.maxlength = length
            self.startIndex = left+1