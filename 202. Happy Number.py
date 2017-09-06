'''
https://leetcode.com/problems/happy-number/description/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

1. 
class Solution(object):
	def isHappy(self, n):
		sums = []
		if n <= 0:
			return False
		else:
			while n != 1:
				n = self.getSum(n)
				if n in sums:
					return False
				else:
					sums.append(n)
			return True

	def getSum(self, n):
		lst = []
		while n // 10 >= 1:
			lst.append(n % 10)
			n = n // 10
		lst.append(n)
		
		from functools import reduce
		return reduce(lambda x, y: x + y, [i**2 for i in lst])
    
2.
class Solution(object):
	def isHappy(self, n):
		sums = []
		while n != 1:
			n = sum([int(i)**2 for i in str(n)])
			if n in sums:
				return False
			else:
				sums.append(n)
		return True
    
