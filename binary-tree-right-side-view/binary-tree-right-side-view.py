# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        
        q = [[0, root]]
        res = []
        prevDepth = 0
        prevNode = root
        
        while True:
            depth, node = q.pop(0)
            
            if prevDepth != depth:
                res.append(prevNode.val)
                
            if node.left:
                q.append([depth+1, node.left])
            if node.right:
                q.append([depth+1, node.right])
                
            if not q:
                res.append(node.val)
                break
                
            prevDepth = depth
            prevNode = node
            
        return res

        
        
        