class Solution(object):
    def candyCrush(self, board):
        isStable = False
        
        while not isStable:
            isStable = True
            #check rows
            for i in range(len(board)):
                for j in range(len(board[0]) - 2):
                    if board[i][j] == 0:
                        continue
                    if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                        val = -1*abs(board[i][j])
                        board[i][j] = val
                        board[i][j+1] = val
                        board[i][j+2] = val
                        isStable = False
            #check cols     
            for j in range(len(board[0])):
                for i in range(len(board) - 2):
                    if board[i][j] == 0:
                        continue
                    if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                        val = -1*abs(board[i][j])
                        board[i][j] = val
                        board[i+1][j] = val
                        board[i+2][j] = val
                        isStable = False
                
                
            for j in range(len(board[0])):
                emptySpace = 0
                for i in reversed(range(len(board))):
                    if board[i][j] < 0:
                        emptySpace += 1
                        board[i][j] = 0
                    elif board[i][j] > 0:
                        if emptySpace > 0:
                            board[i+emptySpace][j] = board[i][j]
                            board[i][j] = 0
                    else:
                        emptySpace += 1
                        
        return board
                    