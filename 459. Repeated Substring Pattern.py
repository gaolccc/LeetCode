'''
https://leetcode.com/problems/repeated-substring-pattern/description/

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length > 1 and s == s[0] * length:
            return True
        else:
            for i in range(2, length // 2 + 1):
                if length % i == 0 and s == s[:length//i] * i:
                    return True
    
            return False
            
'''
Other's

def repeatedSubstringPattern(self, s):
    return s in (2 * s)[1:-1]
'''
