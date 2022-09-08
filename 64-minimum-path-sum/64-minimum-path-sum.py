class Solution(object):
    def minPathSum(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                left = grid[row][col - 1] if col - 1 >= 0 else float("inf")
                up = grid[row - 1][col] if row - 1 >= 0 else float("inf")
                
                if up == float("inf") and left == float("inf"):
                    minPath = 0
                else:
                    minPath = min(left, up)
                
                grid[row][col] = grid[row][col] + minPath
                
        return grid[-1][-1]
    
#         pathSum = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
        
#         for row in range(len(pathSum)):
#             for col in range(len(pathSum[0])):
#                 left = pathSum[row][col - 1] if col - 1 >= 0 else float("inf")
#                 up = pathSum[row - 1][col] if row - 1 >= 0 else float("inf")
                
#                 if up == float("inf") and left == float("inf"):
#                     minPath = 0
#                 else:
#                     minPath = min(left, up)
                
#                 pathSum[row][col] = grid[row][col] + minPath
                
#         return pathSum[-1][-1]
        