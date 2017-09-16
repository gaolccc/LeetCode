'''
https://leetcode.com/problems/add-strings/description/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = abs(len(num1) - len(num2))
        if len(num1) < len(num2):
            num1 = '0' * length + num1
        elif len(num1) > len(num2):
            num2 = '0' * length + num2
        carry, sum = 0, []
        for i in range(len(num1)):
            val = ord(num1[-1-i]) + ord(num2[-1-i]) - 2*ord('0') + carry
            sum.append(val % 10)
            carry = val // 10
        sum = ''.join(list(map(str, sum[::-1])))
        return '1' + sum if carry else sum
        
'''
Other's solution:

def addStrings(self, num1, num2):
    z = itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0')
    res, carry, zero2 = [], 0, 2*ord('0')
    for i in z:
        cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
        res.append(str(cur_sum % 10))
        carry = cur_sum // 10
    return ('1' if carry else '') + ''.join(res[::-1])

'''
