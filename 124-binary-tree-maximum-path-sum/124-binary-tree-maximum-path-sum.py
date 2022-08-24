# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, tree):
        def maxPathSumHelper(tree):
            if tree is None:
                return (0, float("-inf"))

            LS, LF = maxPathSumHelper(tree.left)
            RS, RF = maxPathSumHelper(tree.right)

            singleBranchMax = max(tree.val, tree.val + max(LS, RS))
            fullTreeMax = max(singleBranchMax, tree.val + LS + RS)
            finalTreeMax = max(fullTreeMax, LF, RF)

            return (singleBranchMax, finalTreeMax)
        branchMax, fullTreeMax = maxPathSumHelper(tree)
        return max(branchMax, fullTreeMax)

        