class Solution(object):
    def solve(self, board):
        for col in range(len(board[0])):
            if board[0][col] == "O":
                self.bfs(0, col, board)
            if board[len(board)-1][col] == "O":
                self.bfs(len(board)-1, col, board)
                
        for row in range(len(board)):
            if board[row][0] == "O":
                self.bfs(row, 0, board)
            if board[row][len(board[0])-1] == "O":
                self.bfs(row, len(board[0])-1, board)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "1":
                    board[row][col] = "O"
                    
        return board
    
    def bfs(self, row, col, board):
        board[row][col] = "1"
        q = [[row, col]]
        
        while q:
            r, c = q.pop(0)
            
            if c - 1 >= 0 and board[r][c-1] == "O":
                board[r][c-1] = "1"
                q.append([r, c-1])
            
            if c+1 < len(board[0]) and board[r][c+1] == "O":
                board[r][c+1] = "1"
                q.append([r,c+1])
                
            if r-1 >= 0 and board[r-1][c] == "O":
                board[r-1][c] = "1"
                q.append([r-1,c])
            
            if r+1 < len(board) and board[r+1][c] == "O":
                board[r+1][c] = "1"
                q.append([r+1,c])