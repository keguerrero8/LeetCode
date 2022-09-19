class Solution(object):
    def spiralOrder(self, matrix):
        L, R = 0, len(matrix[0]) - 1
        T, B = 0, len(matrix) - 1
        res = []
        while L <= R and T <= B:
            
            i = L
            while i <= R:
                res.append(matrix[T][i])
                i += 1
                
            i = T + 1
            while i <= B:
                res.append(matrix[i][R])
                i += 1
                
            i = R - 1
            while i >= L:
                if T == B:
                    break
                res.append(matrix[B][i])
                i -= 1
                
            i = B - 1
            while i > T:
                if L == R:
                    break
                res.append(matrix[i][L])
                i -= 1
                
            L += 1
            R -= 1
            T += 1
            B -= 1
            
        return res
                
                