# Question: https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        levels = []
        stack = [root]
        
        while root and stack:
            temp = []
            for node in stack:
                temp.append(node.val)
            levels.append(temp)
            
            temp = []
            for node in stack:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            stack = temp
        
        ans = []
        for arr in levels:
            ans.append(sum(arr)/len(arr))
        return ans
      
# Verdict:
# cRuntime: 108 ms, faster than 11.93% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.6 MB, less than 46.07% of Python3 online submissions for Average of Levels in Binary Tree.
