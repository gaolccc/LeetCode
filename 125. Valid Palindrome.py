'''
https://leetcode.com/problems/valid-palindrome/description/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''
# beats 90.68% of python submissions

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = re.findall('[0-9a-z]*', s.lower())
        s = ''.join(s)
        return s == s[::-1]

'''
Other's solution:

class Solution:
    def isPalindrome(self, s):
        newS= [i.lower() for i in s if i.isalnum()]
        return newS == newS[::-1]
'''
