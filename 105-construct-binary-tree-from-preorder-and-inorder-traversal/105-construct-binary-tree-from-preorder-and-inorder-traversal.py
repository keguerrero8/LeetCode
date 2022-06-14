# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        inOrderHash = { inorder[i] : i for i in range(len(inorder))}
        return self.buildTreeHelper(preorder, inorder, inOrderHash, 0, len(preorder) - 1, 0, len(inorder) - 1)
    
    
    def buildTreeHelper(self, preorder, inorder, inOrderHash, startPre, endPre, startIn, endIn):
        if startPre > endPre:
            return None
        
        root = TreeNode(preorder[startPre])
        inOrderIdx = inOrderHash[preorder[startPre]]
        leftTreeLength = inOrderIdx - startIn 
        
        root.left = self.buildTreeHelper(preorder, inorder, inOrderHash, startPre + 1, startPre + leftTreeLength, startIn, inOrderIdx - 1)
        root.right = self.buildTreeHelper(preorder, inorder, inOrderHash, startPre + 1 + leftTreeLength, endPre, inOrderIdx+1, endIn)
        
        return root
        