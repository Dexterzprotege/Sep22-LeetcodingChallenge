# Question: https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        stack = [root]
        
        while root and stack:
            ans.append([node.val for node in stack])
            temp = []
            
            for node in stack:
                if node.children:
                    temp.extend(node.children)
            
            stack = temp
        return ans
      
# Verdict:
# Runtime: 78 ms, faster than 55.87% of Python3 online submissions for N-ary Tree Level Order Traversal.
# Memory Usage: 16.1 MB, less than 50.08% of Python3 online submissions for N-ary Tree Level Order Traversal.
