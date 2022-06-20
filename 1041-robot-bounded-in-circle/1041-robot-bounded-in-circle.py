class Solution(object):
    def isRobotBounded(self, instructions):
        current = [0,0]
        dirX, dirY = 0, 1
        for i in range(4):
            for inst in instructions:
                if inst == "G":
                    current[0] += dirX
                    current[1] += dirY
                elif inst == "L":
                    dirX, dirY = -1*dirY, dirX 
                else:
                    dirX, dirY = dirY, -1*dirX
                    
            if current == [0,0]:
                return True
            
        return False