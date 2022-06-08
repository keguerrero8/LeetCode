# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    def isSameTree(self, candidate, subRoot):
        if candidate is None and subRoot is None:
            return True
        elif candidate is None or subRoot is None:
            return False
        
        if candidate.val != subRoot.val:
            return False
        
        return self.isSameTree(candidate.left, subRoot.left) and self.isSameTree(candidate.right, subRoot.right)
        