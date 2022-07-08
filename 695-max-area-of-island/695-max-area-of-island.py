class Solution(object):
    def maxAreaOfIsland(self, grid):
        maxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = self.bfs(grid, row, col)
                    maxArea = max(maxArea, area)
                    
        return maxArea
        
        
    def bfs(self, grid, row, col):
        area = 1
        
        q = [[row, col]]
        grid[row][col] = 2
        
        while q:
            r, c = q.pop(0)
            
            if c - 1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                q.append([r, c-1])
                area += 1
                
            if c+1 < len(grid[0]) and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                q.append([r,c+1])
                area += 1
                
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                q.append([r-1, c])
                area += 1
            
            if r+1 < len(grid) and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                q.append([r+1, c])
                area += 1
                
        return area