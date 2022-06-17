class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        matrix = [[] for i in range(numRows)]
        counter = 1
        isZigDown = True
        
        for char in s:
            matrix[counter-1].append(char)
            
            if isZigDown:
                if counter == numRows:
                    isZigDown = False
                    counter -= 1
                else:
                    counter += 1
            else:
                if counter == 1:
                    isZigDown = True
                    counter += 1
                else:
                    counter -= 1
                    
        zigZagConversion = []           
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                zigZagConversion.append(matrix[row][col])
        
        return "".join(zigZagConversion)
        
        