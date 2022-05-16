# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        traversal = []
        stack = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            traversal.append(current.val)
            current = current.right
                
                    
        return traversal
        
        
        
        
        # def inorderTraversal(self, root, traverse = None):
        #         if traverse == None:
        #             traverse = []

        #         if root is None:
        #             return

        #         self.inorderTraversal(root.left, traverse)
        #         traverse.append(root.val)
        #         self.inorderTraversal(root.right, traverse)

        #         return traverse
    