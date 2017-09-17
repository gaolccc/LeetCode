'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curString, longestString = '', ''
        for item in s:
            if item not in curString:
                curString += item
            else:
                if len(curString) > len(longestString):
                    longestString = curString
                idx = curString.index(item)
                curString = curString[idx+1:]+item
        return max(len(longestString), len(curString))
        
        
