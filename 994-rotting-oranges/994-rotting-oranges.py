class Solution(object):
    def orangesRotting(self, grid):
        q1, q2 = [], []
        minutes = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q1.append([row, col])
                    
        while True:  
            while q1:
                r, c = q1.pop(0)
                
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    q2.append([r, c-1])
                    grid[r][c-1] = 2
                    
                if c + 1 < len(grid[0]) and grid[r][c+1] == 1:
                    q2.append([r, c+1])
                    grid[r][c+1] = 2
                    
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    q2.append([r-1, c])
                    grid[r-1][c] = 2
                    
                if r + 1 < len(grid) and grid[r+1][c] == 1:
                    q2.append([r+1, c])
                    grid[r+1][c] = 2
            
            if not q2:
                break
            minutes += 1
            q1, q2 = q2, q1
            
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
                   
        return minutes
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        