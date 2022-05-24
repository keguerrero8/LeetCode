"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node, clonedHash = None):
        if node is None:
            return None
        if clonedHash == None:
            clonedHash = {}
            
        if node.val in clonedHash:
            return clonedHash[node.val]
        
        clone = Node(node.val)
        clonedHash[node.val] = clone
        
        for neighbor in node.neighbors:
            cloneNeighbor = self.cloneGraph(neighbor, clonedHash)
            clone.neighbors.append(cloneNeighbor)
            
        return clone
        