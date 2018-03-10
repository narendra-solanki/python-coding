"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Start scanning from left and keep storing character vs its index
        If duplicate character found, then mark its index and store number of chars till now as max length, and keep scanning
        If next duplicate character found then calculate length from last duplicate character till now 
        and update max if length is greater than last length
        """
        if not s:
            return 0
        chardict = {}
        maxlength = 1
        newindex = 0 #start index of substring with 
        for i, char in enumerate(s, 0):               
            if char in chardict:                 
                newindex = max(newindex, chardict[char] + 1) #update newindex only if duplicate character is found after newindex  
            chardict[char] = i #put character vs key in dictionary
            maxlength = max(maxlength, i-newindex+1) #compute maxlength at each iteration
        
        return maxlength