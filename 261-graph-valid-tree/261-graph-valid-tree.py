class Solution(object):
#     def validTree(self, n, edges):
#         if n == 1:
#             return True
#         edgesHash = {}
#         visiting = set()
#         visited = set()
        
#         for edge in edges:
#             if edge[0] not in edgesHash:
#                 edgesHash[edge[0]] = [edge[1]]
#             else:
#                 edgesHash[edge[0]].append(edge[1])
                
#             if edge[1] not in edgesHash:
#                 edgesHash[edge[1]] = [edge[0]]
#             else:
#                 edgesHash[edge[1]].append(edge[0])
            
#         return self.dfs(0, edgesHash, visiting, visited, -1) and len(visited) == n
    
    
#     def dfs(self, node, edgesHash, visiting, visited, prevNode):
#         if node in visiting or node not in edgesHash:
#             return False
        
#         visiting.add(node)
        
#         if node in visited:
#             visiting.remove(node)
#             return True
        
#         for neighbor in edgesHash[node]:
#             if neighbor == prevNode:
#                 continue
#             isValidTree = self.dfs(neighbor, edgesHash, visiting, visited, node)
#             if not isValidTree:
#                 return False
            
#         visiting.remove(node)
#         visited.add(node)
#         return True
    def validTree(self, n, edges):
        if n == 1:
            return True
        edgesHash = {}
        visited = set()
        
        for edge in edges:
            if edge[0] not in edgesHash:
                edgesHash[edge[0]] = [edge[1]]
            else:
                edgesHash[edge[0]].append(edge[1])
                
            if edge[1] not in edgesHash:
                edgesHash[edge[1]] = [edge[0]]
            else:
                edgesHash[edge[1]].append(edge[0])
            
        return self.dfs(0, edgesHash, visited, -1) and len(visited) == n
    
    
    def dfs(self, node, edgesHash, visited, prevNode):
        if node in visited or node not in edgesHash:
            return False
        
        visited.add(node)
        
        for neighbor in edgesHash[node]:
            if neighbor == prevNode:
                continue
            isValidTree = self.dfs(neighbor, edgesHash, visited, node)
            if not isValidTree:
                return False
            
        return True

    