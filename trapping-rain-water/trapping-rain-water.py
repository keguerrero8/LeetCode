class Solution(object):
    def trap(self, heights):
        if len(heights) == 0:
            return 0

        l, r = 0, len(heights) - 1
        leftMax = [heights[l], l]
        rightMax = [heights[r], r]
        totalArea = 0

        while l < r:

            if heights[l] > leftMax[0]:
                leftMax = [heights[l], l]
            if heights[r] > rightMax[0]:
                rightMax = [heights[r], r]

            if l != leftMax[1]:
                area = min(leftMax[0], rightMax[0]) - heights[l]
            elif r != rightMax[1]:
                area = min(leftMax[0], rightMax[0]) - heights[r]
            else:
                area = 0

            totalArea += area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return totalArea