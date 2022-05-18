"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node, visited = None):
        if node is None:
            return None
        
        if visited == None:
            visited = {}
            
        if node.val in visited:
            return visited[node.val]
        
        visited[node.val] = Node(node.val)
        
        for neighbor in node.neighbors:
            cloneNeighbor = self.cloneGraph(neighbor, visited)
            visited[node.val].neighbors.append(cloneNeighbor)
            
        return visited[node.val]
        
        