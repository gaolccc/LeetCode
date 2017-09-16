'''
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, head = 0, ListNode(0)
        l = head
        while l1 and l2:
            sum = l1.val + l2.val + carry
            head.next = ListNode(sum % 10)
            carry = sum // 10
            head = head.next
            l1 = l1.next
            l2 = l2.next
            if not l1 and carry:
                l1 = ListNode(carry)
                carry = 0
            elif not l2 and carry:
                l2 = ListNode(carry)
                carry = 0
        if l1 or l2:
            head.next = l1 if l1 else l2
        l = l.next
        return l  
        
'''
Solutions from StefanPochmann:
1.
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))

2.
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first

3.
class Solution:
    def addTwoNumbers(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry /= 10
        return dummy.next
        
https://discuss.leetcode.com/topic/14575/python-for-the-win/2
'''
