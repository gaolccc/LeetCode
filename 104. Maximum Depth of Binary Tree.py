'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return max(self.getDepth(root))
    
    def getDepth(self, root):
        if not root:
            return 0
        else:
            return [1 + path for kid in (root.left, root.right) if kid for path in self.getDepth(kid)] or [1]        
            
'''

StefanPochmann's solution:

def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
    
'''
