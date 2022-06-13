class Solution(object):
    def gameOfLife(self, board):
        #live = 1, dead = 0
        #if < 2 neighbors are alive, live cell dies from 1 to 0
        #if 2-3 neighbors are alive, live cell stays alive
        #if > 3 neighbors are alive, live cell dies from 1 to 0
        #if 3 neighbors are alive, dead cell lives from 0 to 1
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                liveNeighbors = self.getNeighbors(board, row, col)
                if board[row][col] == 1:
                    if liveNeighbors < 2 or liveNeighbors > 3:
                        board[row][col] = -1
                else:
                    if liveNeighbors == 3:
                        board[row][col] = 2
                        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
                    
        return board
    
    
    def getNeighbors(self, board, row, col):
        liveNeighbors = 0
        
        #up
        if row - 1 >= 0 and abs(board[row - 1][col]) == 1:
            liveNeighbors += 1
        #down
        if row + 1 < len(board) and abs(board[row + 1][col]) == 1:
            liveNeighbors += 1
        #left   
        if col - 1 >= 0 and abs(board[row][col-1]) == 1:
            liveNeighbors += 1
        #right   
        if col + 1 < len(board[0]) and abs(board[row][col+1]) == 1:
            liveNeighbors += 1

        #up, left
        if row - 1 >= 0 and col - 1 >= 0 and abs(board[row - 1][col-1]) == 1:
            liveNeighbors += 1
        #up, right
        if row - 1 >= 0 and col + 1 < len(board[0]) and abs(board[row - 1][col + 1]) == 1:
            liveNeighbors += 1
        #down, left   
        if row + 1 < len(board) and col - 1 >= 0 and abs(board[row + 1][col - 1]) == 1:
            liveNeighbors += 1
        #down, right   
        if row + 1 < len(board) and col + 1 < len(board[0]) and abs(board[row+1][col+1]) == 1:
            liveNeighbors += 1
            
        return liveNeighbors