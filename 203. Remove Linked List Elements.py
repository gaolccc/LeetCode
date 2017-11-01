'''
https://leetcode.com/problems/remove-linked-list-elements/description/

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

'''
beats 95.56% of python submissions
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if head:
            node = head
            while head and head.next:
                if head.next.val == val:
                    head.next = head.next.next
                else:
                    head = head.next
            return node
        return head
        
