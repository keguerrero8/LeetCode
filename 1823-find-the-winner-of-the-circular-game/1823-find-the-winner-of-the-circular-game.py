class Solution(object):
    def findTheWinner(self, n, k):
        q = [i+1 for i in range(n)]
        
        while len(q) > 1:
            for j in range(k-1):
                q.append(q.pop(0))
            q.pop(0)
        return q[0]
        