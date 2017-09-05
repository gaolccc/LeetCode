'''
https://leetcode.com/problems/pascals-triangle/description/

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
		if numRows < 1:
			return []
		elif numRows == 1:
			return [[1]]
		else:
			psc = [[1], [1, 1]]
			for i in xrange(2, numRows):
				temp = [1]
				for j in xrange(1, i):
					val = psc[i-1][j-1]+psc[i-1][j]
					temp.append(val)
				temp.append(1)
				psc.append(temp)
			return psc

'''
Other's solution:
1. 
def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1]+[0], [0]+res[-1]))]
    return res[:numRows]

(
explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1 
 )
 
 2.
def generate(self, numRows):
    resultset = [[1] * (i + 1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            resultset[i][j] = resultset[i - 1][j - 1] + resultset[i - 1][j]
    return resultset
'''
