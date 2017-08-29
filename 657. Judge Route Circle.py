'''
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return True if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R') else False      
        
'''
Other's solution:
1.
def judgeCircle(self, moves):
    return not sum(map({'U': 1, 'D': -1, 'L': 1j, 'R': -1j}.get, moves))

2. 
def judgeCircle(self, moves):
    return not sum(1j**'RUL'.find(m) for m in moves)
    
3.
def judgeCircle(self, moves):
    return not sum(map(1j.__pow__, map('RUL'.find, moves)))
'''
