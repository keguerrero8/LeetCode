# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        
        q = [[root, 0]]
        levelHash = {}
        
        while q:
            
            node, level = q.pop(0)
            
            if node.left:
                q.append([node.left, level + 1])
                
            if node.right:
                q.append([node.right, level + 1])
            
            if level not in levelHash:
                levelHash[level] = [node.val]
            else:
                levelHash[level].append(node.val)
                
        minLevel = float("inf")
        maxLevel = float("-inf")
        for key in levelHash.keys():
            maxLevel = max(maxLevel, key)
            minLevel = min(minLevel, key)
            
        res = []
        for i in range(minLevel, maxLevel + 1):
            res.append(levelHash[i])
            
        return res
            