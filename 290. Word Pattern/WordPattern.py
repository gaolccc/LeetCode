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