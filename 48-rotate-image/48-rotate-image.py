class Solution(object):
    def rotate(self, matrix):
        L = 0
        R = len(matrix) - 1
        top = 0
        bottom = len(matrix) - 1
        
        while L <= R or top <= bottom:
            for i in range(R-L):
                temp = matrix[top][L+i]
                matrix[top][L+i] = matrix[bottom-i][L]
                matrix[bottom-i][L] = matrix[bottom][R-i]
                matrix[bottom][R-i] = matrix[top+i][R]
                matrix[top+i][R] = temp
            L += 1
            R -= 1
            top += 1
            bottom -= 1
            
        return matrix
        