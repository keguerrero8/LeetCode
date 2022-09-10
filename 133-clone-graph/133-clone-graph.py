"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None
        
        cloneMap = {}
        
        def dfs(node):            
            if node.val in cloneMap:
                return cloneMap[node.val]
            
            cloneMap[node.val] = Node(node.val)
            clone = cloneMap[node.val]

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)
    
        
        