class Solution(object):
    def allPathsSourceTarget(self, graph):
        res = []
        path = []
        def dfs(node, path):
            if node == len(graph) - 1:
                path.append(node)
                res.append(path + [])
                path.pop()
                return
            
            path.append(node)
            
            for neighbor in graph[node]:
                dfs(neighbor, path)
                
            path.pop()
            
        dfs(0, path)  
        return res

                
            
        