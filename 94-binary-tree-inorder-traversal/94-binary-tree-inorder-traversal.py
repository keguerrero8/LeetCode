# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        inOrder = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            node = stack.pop()
            inOrder.append(node.val)
            current = node.right
            
        return inOrder
        