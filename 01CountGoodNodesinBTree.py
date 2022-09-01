# Question: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root, maxx = -1000000):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 1 if root.val >= maxx else 0
        res += self.goodNodes(root.left, max(maxx, root.val))
        res += self.goodNodes(root.right, max(maxx, root.val))
        return res
      
# Verdict:
# Runtime: 639 ms, faster than 5.20% of Python online submissions for Count Good Nodes in Binary Tree.
# Memory Usage: 49.2 MB, less than 71.92% of Python online submissions for Count Good Nodes in Binary Tree.
