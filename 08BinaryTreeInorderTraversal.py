# Question: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Solutiom:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return arr
      
# Verdict:
# Runtime: 58 ms, faster than 22.23% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 13.9 MB, less than 13.48% of Python3 online submissions for Binary Tree Inorder Traversal.
