# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root, start = self.reconstructBstHelper(preorder, 0, len(preorder) - 1, float("-inf"), float("inf"))
        return root


    def reconstructBstHelper(self, preOrderTraversalValues, start, end, lowerBound, upperBound):     
        if start > end or preOrderTraversalValues[start] >= upperBound or preOrderTraversalValues[start] < lowerBound:
            return (None, start)

        root = TreeNode(preOrderTraversalValues[start])
        root.left, start = self.reconstructBstHelper(preOrderTraversalValues, start + 1, end, lowerBound, root.val)
        root.right, start = self.reconstructBstHelper(preOrderTraversalValues, start, end, root.val, upperBound)

        return (root, start)
        