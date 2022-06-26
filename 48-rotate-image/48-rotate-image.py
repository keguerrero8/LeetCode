class Solution(object):
    def rotate(self, matrix):
        L, R = 0, len(matrix) - 1
        T, B = 0, len(matrix) - 1
        
        while L < R:
            for i in range(R-L):
                temp = matrix[T][L+i]
                matrix[T][L+i] = matrix[B-i][L]
                matrix[B-i][L] = matrix[B][R-i]
                matrix[B][R-i] = matrix[T+i][R]
                matrix[T+i][R] = temp
            L += 1
            R -= 1
            T += 1
            B -= 1
            
        return matrix
        