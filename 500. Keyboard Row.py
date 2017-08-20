'''
https://leetcode.com/problems/keyboard-row/description/

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

American keyboard
----------------
QWERTYUIOP
ASDFGHJKL
ZXCVBNM
----------------

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rlt = []
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        
        for word in words:
            for row in rows:
                if all(map(lambda x: x in row, word.lower())):
                    rlt.append(word)
        
        return rlt
        
'''
StefanPochmann's solution:

def findWords(self, words):
    return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
'''
