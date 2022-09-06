# Question: https://leetcode.com/problems/binary-tree-pruning/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def containsOne(node):
            if not node:
                return False
            
            left = containsOne(node.left)
            right = containsOne(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val or left or right
        
        if containsOne(root):
            return root
        else:
            None
            
# Verdict:
# Runtime: 37 ms, faster than 84.08% of Python3 online submissions for Binary Tree Pruning.
# Memory Usage: 13.8 MB, less than 68.92% of Python3 online submissions for Binary Tree Pruning.
