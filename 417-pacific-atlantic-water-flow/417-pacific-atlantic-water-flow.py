class Solution(object):
    def pacificAtlantic(self, heights):        
        pac = set()
        atl = set()
        
        #iterate through first row and last row
        for col in range(len(heights[0])):
            self.bfs(heights, 0, col, pac)
            self.bfs(heights, len(heights) - 1, col, atl)
            
        #iterate through first col and last col
        for row in range(len(heights)):
            self.bfs(heights, row, 0, pac)
            self.bfs(heights, row, len(heights[0]) - 1, atl)
        
        res = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in atl and (row, col) in pac:
                    res.append([row, col])        
        return res
    
    
    def bfs(self, heights, row, col, ocean):
        if (row, col) not in ocean:
            ocean.add((row, col))
            
        q = [[row, col]]
        
        while q:
            r, c = q.pop(0)
            
            #check left
            if c - 1 >= 0 and (r, c - 1) not in ocean and heights[r][c-1] >= heights[r][c]:
                ocean.add((r, c-1))
                q.append([r, c-1])
                
            #check right
            if c + 1 < len(heights[0]) and (r, c + 1) not in ocean and heights[r][c+1] >= heights[r][c]:
                ocean.add((r, c+1))
                q.append([r, c+1])
                
            #check up
            if r - 1 >= 0 and (r - 1, c) not in ocean and heights[r-1][c] >= heights[r][c]:
                ocean.add((r-1, c))
                q.append([r-1, c])
                
            #check down
            if r + 1 < len(heights) and (r + 1, c) not in ocean and heights[r+1][c] >= heights[r][c]:
                ocean.add((r+1, c))
                q.append([r+1, c])