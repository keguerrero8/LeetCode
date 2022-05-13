class Solution(object):
    def spiralOrder(self, matrix):
        l = 0
        r = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        result = []
        
        while l <= r and top <= bottom:
            i = l
            while i <= r:
                result.append(matrix[top][i])
                i += 1
                
            i = top + 1
            while i < bottom:
                result.append(matrix[i][r])
                i += 1
                
            i = r
            while i >= l:
                if bottom == top:
                    break
                result.append(matrix[bottom][i])
                i -= 1
                
            i = bottom - 1
            while i > top:
                if l == r:
                    break
                result.append(matrix[i][l])
                i -= 1
                
            l += 1
            r -= 1
            top += 1
            bottom -= 1
            
        return result