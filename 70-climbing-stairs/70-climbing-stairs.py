class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        ways = [0]*(n+1)
        ways[0], ways[1] = 1, 1
        
        for step in range(2, len(ways)):
            ways[step] = ways[step-1] + ways[step-2]
        
        return ways[-1]