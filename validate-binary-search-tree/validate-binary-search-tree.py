# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.validateBstHelper(root.left, float("-inf"), root.val) and self.validateBstHelper(root.right, root.val, float("inf"))


    def validateBstHelper(self, tree, leftBound, rightBound):
        if tree is None:
            return True

        if tree.val >= rightBound or tree.val <= leftBound: 
            return False

        return self.validateBstHelper(tree.left, leftBound, tree.val) and self.validateBstHelper(tree.right, tree.val, rightBound)
        