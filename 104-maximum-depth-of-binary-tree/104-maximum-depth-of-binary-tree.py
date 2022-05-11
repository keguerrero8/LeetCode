# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        def maxDepthHelper(root, depth):
            if root is None:
                return depth
            
            leftDepth = maxDepthHelper(root.left, depth + 1)
            rightDepth = maxDepthHelper(root.right, depth + 1)
            
            return max(leftDepth, rightDepth)
        
        return maxDepthHelper(root, 0)
        