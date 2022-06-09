# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return self.isBalancedHelper(root, 0)[0]

    def isBalancedHelper(self, root, depth):
        if root is None:
            return (True, depth)

        isBalanceLeft, leftDepth = self.isBalancedHelper(root.left, depth + 1)
        isBalanceRight, rightDepth = self.isBalancedHelper(root.right, depth + 1)

        if not isBalanceLeft or not isBalanceRight:
            return (False, None)

        if abs(leftDepth - rightDepth) > 1:
            return (False, None)

        return (True, max(leftDepth, rightDepth))
        