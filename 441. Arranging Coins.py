'''
https://leetcode.com/problems/arranging-coins/description/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

class Solution(object):
	def arrangeCoins(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		import math
		return int(math.floor(math.sqrt(2*n+0.25)-0.5))
    
'''
Other solution:
1. 
def arrangeCoins(self, n):
	"""
	:type n: int
	:rtype: int
	"""
	i = 1
	while n >= i:
		n -= i
		i += 1
	return i - 1

2.
def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((1+8*n)**0.5 - 1) / 2
'''
