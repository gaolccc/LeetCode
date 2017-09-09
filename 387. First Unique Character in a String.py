'''
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        for i in range(len(s)):
            if s[i] not in chars:
                if s[i] not in s[i+1:]:
                    return i
                else:
                    chars.append(s[i])
            else:
                pass
        
        return -1
        
