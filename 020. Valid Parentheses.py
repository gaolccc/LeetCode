'''
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets_dict = {'(': ')', '[': ']', '{': '}'}
        brackets_stack = ['']
        for i in s:
            if i in brackets_dict.keys():
                brackets_stack.append(brackets_dict[i])
            elif i != '' and i != brackets_stack.pop():
                return False
        return brackets_stack == ['']
        
        
