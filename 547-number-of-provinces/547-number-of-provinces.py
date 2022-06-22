class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0
        
        def dfs(city):
            visited.add(city)
            for neighbor in range(len(isConnected[city])):
                if neighbor not in visited and isConnected[city][neighbor] == 1 and city != neighbor:
                    dfs(neighbor)

            
        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                provinces += 1
                
        return provinces
            
            
            
            
#         provinces = len(isConnected)
#         parent = [i for i in range(provinces)]
#         rank = [1 for i in range(provinces)]
        
#         def find(n):
#             res = n
#             while res != parent[res]:
#                 parent[res] = parent[parent[res]]
#                 res = parent[res]
                
#             return res
                
        
#         def union(n1, n2):
#             p1, p2 = find(n1), find(n2)
#             if p1 == p2: return 0
            
#             if rank[p1] > rank[p2]:
#                 parent[p2] = p1
#                 rank[p1] += rank[p2]
#             else:
#                 parent[p1] = p2
#                 rank[p2] += p1
                
#             return 1
        
#         for i in range(len(isConnected)):
#             for j in range(len(isConnected[i])):
#                 if i != j and isConnected[i][j] == 1:
#                     provinces -= union(i, j)
        
                    
#         return provinces
    
        