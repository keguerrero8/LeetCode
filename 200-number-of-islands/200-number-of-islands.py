class Solution(object):
    def numIslands(self, grid):
        res = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid[row][col] = "2"
                    self.dfs(row, col, grid)
                    res += 1
                    
        return res
    
    def dfs(self, r, c, grid):

        neighbors = self.getNeighbors(r, c, grid)
        
        for nei in neighbors:
            self.dfs(nei[0], nei[1], grid)
            

    
    def getNeighbors(self, r, c, grid):
        neighbors = []
        
        if c - 1 >= 0 and grid[r][c-1] == "1":
            grid[r][c-1] = "2"
            neighbors.append([r, c-1])
            
        if c + 1 < len(grid[0]) and grid[r][c+1] == "1":
            grid[r][c+1] = "2"
            neighbors.append([r, c+1])
            
        if r - 1 >= 0 and grid[r-1][c] == "1":
            grid[r-1][c] = "2"
            neighbors.append([r-1, c])
            
        if r + 1 < len(grid) and grid[r+1][c] == "1":
            grid[r+1][c] = "2"
            neighbors.append([r+1, c])
            
        return neighbors