class Solution(object):
    #Time : 3 x 81 = O(1)
    #Space : 3 x 81 = O(1)
    def isValidSudoku(self, board):
        sudokuMap = { str(i): False for i in range(1, 10) }
        
        #check all rows for validation
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] not in sudokuMap:
                    continue
                if not sudokuMap[board[row][col]]:
                    sudokuMap[board[row][col]] = True
                else:
                    return False
            sudokuMap = { str(i): False for i in range(1, 10) }
        # isValid = self.sudokuCheck(board, 0, 10, sudokuMap)
            
        
        #check all columns for validation
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] not in sudokuMap:
                    continue
                if not sudokuMap[board[row][col]]:
                    sudokuMap[board[row][col]] = True
                else:
                    return False
            sudokuMap = { str(i): False for i in range(1, 10) }
            
            
        #check all each grid for validation -> first check is rows 0-2 and cols 0-2, second check is rows 3-5 and cols 3-5
        rowStart, rowEnd = 0, 3
        colStart, colEnd = 0, 3
        colIteration = rowIteration = 0
        
        while rowIteration <= 2:
            colStart, colEnd = 0, 3
            while colIteration <= 2:
                for row in range(rowStart, rowEnd):
                    for col in range(colStart, colEnd):
                        if board[row][col] not in sudokuMap:
                            continue
                        if not sudokuMap[board[row][col]]:
                            sudokuMap[board[row][col]] = True
                        else:
                            return False
                sudokuMap = { str(i): False for i in range(1, 10) }
                colIteration += 1
                colStart += 3
                colEnd += 3
                
            colIteration = 0
            rowIteration += 1
            rowStart += 3
            rowEnd += 3
            
        return True
    
    
        
        
        
        
        
        
        
                    
                    
                
        
        