# Question: https://leetcode.com/problems/construct-string-from-binary-tree/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        ans = ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if left or right:
            ans += "(%s)" % left
        if right:
            ans += "(%s)" % right
        return str(root.val) + ans
      
# Verdict:
# Runtime: 112 ms, faster than 17.89% of Python3 online submissions for Construct String from Binary Tree.
# Memory Usage: 16.6 MB, less than 10.34% of Python3 online submissions for Construct String from Binary Tree.
