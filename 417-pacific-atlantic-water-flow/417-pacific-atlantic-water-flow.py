class Solution(object):
    def pacificAtlantic(self, heights):
        #create a pac set and an atlantic set
        #iterate through first row and first col and perform bfs to mark coordinates that can be reached by pac
            #during iteration, if coordinate is already in ocean, skip and move to next
        #iterate through last row and last col and perform bfs to mark coordinates for atl
        #iterate through heights matrix again, and if coordinates are in both sets, add them to output array
        pac = set()
        atl = set()
        
        #perform bfs on first row and last row
        for col in range(len(heights[0])):
            if (0, col) not in pac:
                pac.add((0, col))
            self.breadthFirstSearch(pac, 0, col, heights)
            if (len(heights)-1, col) not in atl:
                atl.add((len(heights)-1, col))
            self.breadthFirstSearch(atl, len(heights)-1, col, heights)
            
        #perform bfs on first col and last col
        for row in range(len(heights)):
            if (row, 0) not in pac:
                pac.add((row, 0))
            self.breadthFirstSearch(pac, row, 0, heights)
            if (row, len(heights[0])-1) not in atl:
                atl.add((row, len(heights[0])-1))
            self.breadthFirstSearch(atl, row, len(heights[0])-1, heights)
        
        result = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (row, col) in pac and (row, col) in atl:
                    result.append([row, col])
                    
        return result
    
    
    def breadthFirstSearch(self, ocean, row, col, heights):
        
        q = [[row, col]]
        
        while q:
            cRow, cCol = q.pop(0)
                
            #check left
            if cCol - 1 >= 0 and heights[cRow][cCol] <= heights[cRow][cCol-1] and (cRow, cCol - 1) not in ocean:
                    q.append([cRow, cCol - 1])
                    ocean.add((cRow, cCol-1))

            #check right
            if cCol + 1 < len(heights[0]) and heights[cRow][cCol] <= heights[cRow][cCol+1] and (cRow, cCol + 1) not in ocean:
                    q.append([cRow, cCol + 1])
                    ocean.add((cRow, cCol+1))

                    
            #check up
            if cRow - 1 >= 0 and heights[cRow][cCol] <= heights[cRow-1][cCol] and (cRow-1, cCol) not in ocean:
                    q.append([cRow-1, cCol])
                    ocean.add((cRow-1, cCol))

            
            #check down
            if cRow + 1 < len(heights) and heights[cRow][cCol] <= heights[cRow+1][cCol] and (cRow+1, cCol) not in ocean:
                    q.append([cRow+1, cCol])
                    ocean.add((cRow+1, cCol))

        