# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q = [[root, 0]]
        depthHash = {}
        
        while q:
            node, depth = q.pop(0)
            
            if depth in depthHash:
                depthHash[depth].append(node.val)
            else:
                depthHash[depth] = [node.val]
                
            if node.left:
                q.append([node.left, depth + 1])
            if node.right:
                q.append([node.right, depth + 1])
                
        maxDepth = float("-inf")
        for key in depthHash.keys():
            maxDepth = max(key, maxDepth)
            
        res = []
        zigZagDirection = True
        for depth in range(maxDepth + 1):
            depthRes = []
            if zigZagDirection:
                for val in depthHash[depth]:
                    depthRes.append(val)
            else:
                for i in reversed(range(len(depthHash[depth]))):
                    depthRes.append(depthHash[depth][i])
            res.append(depthRes)
            zigZagDirection = False if zigZagDirection else True
            
        return res
                    
            
            
            
        