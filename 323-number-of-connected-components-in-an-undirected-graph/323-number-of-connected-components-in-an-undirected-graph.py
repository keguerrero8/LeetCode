class Solution(object):
    def countComponents(self, n, edges):
        if n == 1: return 1
        visited = set()
        visiting = set()
        edgesHash = { i:[] for i in range(n) }
        for edge in edges:
            edgesHash[edge[0]].append(edge[1])
            edgesHash[edge[1]].append(edge[0])
            
        components = 0   
        for node in range(n):
            if node in visited:
                continue
            self.dfs(node, edgesHash, visited, visiting, -1)
            components += 1
            
        return components
    
    def dfs(self, node, edgesHash, visited, visiting, prevNode):
        if node in visited or node in visiting:
            return
        
        visiting.add(node)
        
        for neighbor in edgesHash[node]:
            if neighbor == prevNode:
                continue
            self.dfs(neighbor, edgesHash, visited, visiting, node)
            
        visited.add(node)
        visiting.remove(node)
        
        return