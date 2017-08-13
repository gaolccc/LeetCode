'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """      
        if len(pattern) != len(str.split(' ')) or len(set(pattern)) != len(set(str.split(' '))):
            return False
        else:
            dict = {}
            for k, v in enumerate(pattern):
                if v not in dict.keys():
                    dict[v] = str.split(' ')[k]
    
            theStr = []
            for item in pattern:
                theStr.append(dict[item])
    
            return True if theStr == str.split(' ') else False
            
'''
Other's solution:
1.
def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

2. 
def wordPattern(self, pattern, str):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return f(pattern) == f(str.split())

3.
def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

'''
