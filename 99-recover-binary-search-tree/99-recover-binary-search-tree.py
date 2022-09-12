# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-2147483648)
        
    def recoverTree(self, root):            
        self.inOrderTraversal(root)
        
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        
    
    def inOrderTraversal(self, root):
        if root is None: return
        self.inOrderTraversal(root.left)

        if self.first is None and self.prev.val > root.val:
            self.first = self.prev
            
        if self.first and self.prev.val > root.val:
            self.second = root
            
        self.prev = root

        self.inOrderTraversal(root.right)
    
        
        