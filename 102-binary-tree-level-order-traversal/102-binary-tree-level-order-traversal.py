# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        def levelOrderHelper(node, levelHash, level):
            if node is None:
                return
            if level not in levelHash:
                levelHash[level] = [node.val]
            else:
                levelHash[level].append(node.val)
                
            levelOrderHelper(node.left, levelHash, level + 1)
            levelOrderHelper(node.right, levelHash, level + 1)
            
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        
        levelHash = {}
        levelOrderHelper(root, levelHash, 0)
        result = []
        maxLevel = float("-inf")
        for level in levelHash:
            if level > maxLevel:
                maxLevel = level
        
        for i in range(maxLevel + 1):
            result.append(levelHash[i])
            
        return result