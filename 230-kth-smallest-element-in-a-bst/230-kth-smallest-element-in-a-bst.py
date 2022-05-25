# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        treeInfo = TreeInfo()
        self.findKthSmallestHelper(root, k, treeInfo)
        return treeInfo.kTree.val  
        

    def findKthSmallestHelper(self, tree, k, treeInfo):
        if tree is None or treeInfo.kTree is not None:
            return

        self.findKthSmallestHelper(tree.left, k, treeInfo)

        treeInfo.kVal += 1
        if treeInfo.kVal == k:
            treeInfo.kTree = tree
            return

        self.findKthSmallestHelper(tree.right, k, treeInfo)

        return treeInfo.kTree


class TreeInfo:
    def __init__(self, kTree = None, kVal = 0):
        self.kVal = kVal
        self.kTree = kTree
        