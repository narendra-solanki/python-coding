"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        """
        we should compare needle with haystack substring only if enough characters are left
        for example haystack = "ABCEFG"
                    needle = "abcd"
        then we should only compare needle with substrings ABCEFG, BCEFG and CEFG
        rest all substrings are less than length of the needle
        """
        for i in range(len(haystack) - len(needle)+1): 
            for j in range(len(needle)): #compare the substring from ith index
                if ((i+j) >= len(haystack)) or (haystack[i+j] != needle[j]): 
                    break #substring starting from ith index did not match, so break the inner loop
            else: #we have matched whole string 
                return i
        
        return -1
                   