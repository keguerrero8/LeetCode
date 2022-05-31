# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        if root is None:
            return []
        verticalOrderTraversal = {}
        self.verticalOrderHelper(root, verticalOrderTraversal)
        
        minIdx = float("inf")
        maxIdx = float("-inf")
        for key in verticalOrderTraversal.keys():
            maxIdx = max(maxIdx, key)
            minIdx = min(minIdx, key)
        
        result = []
        for i in range(minIdx, maxIdx + 1):
            result.append(verticalOrderTraversal[i])
            
        return result 
        
    
    def verticalOrderHelper(self, root, verticalOrderTraversal):
        q = [[root, 0]]
        
        while q:
            currentNode, currentVerticalIdx = q.pop(0)
            
            if currentVerticalIdx not in verticalOrderTraversal:
                verticalOrderTraversal[currentVerticalIdx] = [currentNode.val]
            else:
                verticalOrderTraversal[currentVerticalIdx].append(currentNode.val)
                
            if currentNode.left:
                q.append([currentNode.left, currentVerticalIdx - 1])
            if currentNode.right:
                q.append([currentNode.right, currentVerticalIdx + 1])
        
            
        
            
        
        
        