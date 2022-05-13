class Solution(object):
    def trap(self, height):
        L = [0 for i in range(len(height))]
        R = [0 for i in range(len(height))]
        
        for i in range(1, len(height)):
            L[i] = max(L[i-1], height[i-1])
            
        for i in reversed(range(len(height)-1)):
            R[i] = max(R[i+1], height[i+1])
            
        waterArea = 0
        
        for i in range(len(height)):
            minHeight = min(R[i], L[i])
            trappedWater = minHeight - height[i]
            waterArea += trappedWater if trappedWater > 0 else 0
            
        return waterArea