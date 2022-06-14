class Solution(object):
    def exist(self, board, word):        
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, 0, visited, word):
                        return True
        return False

    def dfs(self, board, row, col, startIdx, visited, word):
        if startIdx == len(word) - 1:
            return True
        
        visited.add((row, col))
        
        neighbors = self.getNeighbor(board, row, col, startIdx + 1, word, visited)
        
        if neighbors == []:
            visited.remove((row, col))
            return False
        
        for neighbor in neighbors:    
            if self.dfs(board, neighbor[0], neighbor[1], startIdx + 1, visited, word):
                return True
            
        visited.remove((row, col))
        return False
        
    def getNeighbor(self, board, row, col, i, word, visited):
        neighbor = []
        
        #left
        if col - 1 >= 0 and word[i] == board[row][col-1] and (row, col-1) not in visited:
            neighbor.append([row, col - 1]) 
        
        #right
        if col + 1 < len(board[0]) and word[i] == board[row][col+1] and (row, col+1) not in visited:
            neighbor.append([row, col + 1])
        
        #up
        if row - 1 >= 0 and word[i] == board[row-1][col] and (row-1, col) not in visited:
            neighbor.append([row-1, col])
        
        #down
        if row + 1 < len(board) and word[i] == board[row+1][col] and (row+1, col) not in visited:
            neighbor.append([row+1, col])
        
        return neighbor
                
        
        