class Solution(object):
    def countComponents(self, n, edges):
        if n == 1:
            return 1
            
        edgesHash = {}
        visited = set()
        numOfConnectedComponents = 0
        
        for edge in edges:
            if edge[0] not in edgesHash:
                edgesHash[edge[0]] = [edge[1]]
            else:
                edgesHash[edge[0]].append(edge[1])
                
            if edge[1] not in edgesHash:
                edgesHash[edge[1]] = [edge[0]]
            else:
                edgesHash[edge[1]].append(edge[0])
                
        for node in range(n):
            if node in visited:
                continue
            self.dFS(edgesHash, visited, node)
            numOfConnectedComponents += 1
        
        return numOfConnectedComponents
    
    
    
    def dFS(self, edgesHash, visited, node):
        if node in visited:
            return 
        
        visited.add(node)
        
        if node not in edgesHash:
            return
        
        for neighbor in edgesHash[node]:
            self.dFS(edgesHash, visited, neighbor)
            
        return 