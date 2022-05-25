class Solution(object):
    def setZeroes(self, matrix):
        firstRowZero = False
        firstColZero = False
        
        #check first row
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                firstRowZero = True
                
        #check first column
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstColZero = True
        
        #set first col and row to 0 if current row, col is 0
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
                    
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
                    
        if firstRowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
                
        if firstColZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
        
        return matrix