class Solution(object):
    def validTree(self, n, edges):
        hashEdges = {}
        visited = set()
        
        for edge in edges:
            if edge[0] not in hashEdges:
                hashEdges[edge[0]] = [edge[1]]
            else:
                hashEdges[edge[0]].append(edge[1])
                
            if edge[1] not in hashEdges:
                hashEdges[edge[1]] = [edge[0]]
            else:
                hashEdges[edge[1]].append(edge[0])
                
            
        return self.depthFirstSearch(0, hashEdges, visited, None) and len(visited) == n
    
    
    def depthFirstSearch(self, node, hashEdges, visited, prev):
        if node in visited:
            return False
        
        visited.add(node)
        
        if node not in hashEdges:
            visited.add(node)
            return True
        
        for neighbor in hashEdges[node]:
            if neighbor == prev:
                continue
            isValidTree = self.depthFirstSearch(neighbor, hashEdges, visited, node)
            if not isValidTree:
                return False
            
        visited.add(node)
        
        return True
            
        