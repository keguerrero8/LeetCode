# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        def buildTreeHelper(preorder, inOrderHash, preStart, preEnd, inorder, inStart, inEnd):
            if preStart > preEnd:
                return None
            
            idxInorder = inOrderHash[preorder[preStart]]
            root = TreeNode(preorder[preStart])
            left = idxInorder - inStart
            
            root.left = buildTreeHelper(preorder, inOrderHash, preStart+1, preStart+left, inorder, inStart, idxInorder)
            root.right = buildTreeHelper(preorder, inOrderHash, preStart+1+left, preEnd, inorder, idxInorder+1, inEnd)
            
            return root
        
        inOrderHash = {}
        for i in range(len(inorder)):
            inOrderHash[inorder[i]] = i
                    
        return buildTreeHelper(preorder, inOrderHash, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    