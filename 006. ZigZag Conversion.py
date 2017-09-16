'''
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Zigzag:

/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/
that's the zigzag pattern the question asked!
'''

class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if s:
			rlt = [[] for i in range(numRows)]
			if numRows > 1:
				halfCircle = numRows - 1
				rlt[0].append(s[0])
				for i in range(1, len(s)):
					index = i % (2 * halfCircle)
					if 0 <= index <= halfCircle:
						rlt[index].append(s[i])
					else:
						rlt[2 * halfCircle - index].append(s[i])
				
				return ''.join(list(map(lambda x: ''.join(x), rlt)))
			else:
				return s
		else:
			return ''
      
'''
Other solution:

def convert(self, s, numRows):
    step = (numRows == 1) - 1  # 0 or -1  
    rows, idx = [''] * numRows, 0
    for c in s:
        rows[idx] += c
        if idx == 0 or idx == numRows-1: 
            step = -step  #change direction  
        idx += step
    return ''.join(rows)
 '''
 
