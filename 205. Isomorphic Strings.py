'''
https://leetcode.com/problems/isomorphic-strings/description/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return True if len(set(s)) == len(set(t)) == len(set(zip(s, t))) else False
        
'''
Other's solution
1. 
class Solution:
    def isIsomorphic(self, s, t):
        return all(map({}.setdefault, a, b) == list(b) for a, b in ((s, t), (t, s)))

2.
def isIsomorphic(self, s, t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]
    
3. 
def isIsomorphic(self, s, t):
    return map(s.find, s) == map(t.find, t)

4. 
def isIsomorphic(self, s, t):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return f(s) == f(t)
'''
