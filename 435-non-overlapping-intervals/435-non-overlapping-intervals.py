class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[0])
        minErase = 0
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                minErase += 1
                end = min(end, intervals[i][1])
            else:
                end = intervals[i][1]
                
        return minErase
        