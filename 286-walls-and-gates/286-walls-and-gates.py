class Solution(object):
    def wallsAndGates(self, rooms):
        q1 = []
        INF = 2147483647
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    q1.append([row, col, 0])
                            
        while q1:
            r, c, distance = q1.pop(0)

            if c - 1 >= 0 and rooms[r][c-1] == INF:
                q1.append([r, c-1, distance + 1])
                rooms[r][c-1] = distance + 1

            if c + 1 < len(rooms[0]) and rooms[r][c+1] == INF:
                q1.append([r, c+1, distance+1])
                rooms[r][c+1] = distance + 1

            if r - 1 >= 0 and rooms[r-1][c] == INF:
                q1.append([r-1, c, distance+1])
                rooms[r-1][c] = distance + 1

            if r + 1 < len(rooms) and rooms[r+1][c] == INF:
                q1.append([r+1, c, distance+1])
                rooms[r+1][c] = distance + 1
                
        return rooms
                    
                
        