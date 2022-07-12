# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parentHash = {}
        self.findParents(parentHash, root, None)
        distanceP = self.findDistanceToRoot(p, 0, parentHash)
        distanceQ = self.findDistanceToRoot(q, 0, parentHash)
        
        if distanceP > distanceQ:
            delta = distanceP - distanceQ
            newP = self.moveDistance(p, delta, parentHash)
            return self.lowestAncestor(newP, q, parentHash)
        elif distanceQ > distanceP:
            delta = distanceQ - distanceP
            newQ = self.moveDistance(q, delta, parentHash)
            return self.lowestAncestor(newQ, p, parentHash)
        else:
            return self.lowestAncestor(q, p, parentHash)
            
    def findParents(self, parentHash, root, parent):
        if root is None:
            return 
        parentHash[root.val] = parent
        self.findParents(parentHash, root.left, root)
        self.findParents(parentHash, root.right, root)
        
    def findDistanceToRoot(self, node, distance, parentHash):
        if parentHash[node.val] is None:
            return distance
        
        return self.findDistanceToRoot(parentHash[node.val], distance + 1, parentHash)
        
    def moveDistance(self, node, distance, parentHash):
        curD = 0
        curNode = node
        while curD != distance:
            curNode = parentHash[curNode.val]
            curD += 1
            
        return curNode
    
    def lowestAncestor(self, q, p, parentHash):
        if p.val == q.val:
            return p
        
        return self.lowestAncestor(parentHash[q.val], parentHash[p.val], parentHash)
        
        

        
        
        