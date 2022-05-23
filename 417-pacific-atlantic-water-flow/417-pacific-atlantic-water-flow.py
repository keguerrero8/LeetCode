class Solution(object):
    def pacificAtlantic(self, heights):
        pac = set()
        atl = set()
        
        for col in range(len(heights[0])):
            self.dFS(0, col, pac, heights, heights[0][col])
            self.dFS(len(heights)-1, col, atl, heights, heights[len(heights)-1][col])
            
        for row in range(len(heights)):
            self.dFS(row, 0, pac, heights, heights[row][0])
            self.dFS(row, len(heights[0])-1, atl, heights, heights[row][len(heights[0])-1])
            
        result = []
        
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pac and (row, col) in atl:
                    result.append([row, col])
        return result          
    
    def dFS(self, row, col, ocean, heights, prev):
        if  row < 0 or col < 0 or row == len(heights) or col == len(heights[0]) or heights[row][col] < prev or (row, col) in ocean:
            return
        ocean.add((row, col))
        self.dFS(row+1, col, ocean, heights, heights[row][col])
        self.dFS(row-1, col, ocean, heights, heights[row][col])
        self.dFS(row, col+1, ocean, heights, heights[row][col])
        self.dFS(row, col-1, ocean, heights, heights[row][col])
        
    
        