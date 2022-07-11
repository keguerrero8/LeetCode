class Solution(object):
    def countComponents(self, n, edges):
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        
        def find(n):
            cur = n
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2: return 0
            
            if rank[p2] > rank[p1]:
                rank[p2] += rank[p1]
                parent[p1] = p2
            else:
                rank[p1] += rank[p2]
                parent[p2] = p1
                
            return 1
        
        components = n
        for node1, node2 in edges:
            components -= union(node1, node2)
            
        return components
                
        