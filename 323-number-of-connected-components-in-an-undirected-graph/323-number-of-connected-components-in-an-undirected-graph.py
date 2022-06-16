class Solution(object):
    def countComponents(self, n, edges):
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        #find function will find root parent of the node, and also perform path compression
        def find(node):
            res = node
            
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
                
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
            
        return res