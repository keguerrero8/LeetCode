class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda x: x[0])  
        mergeIntervals = [[intervals[0][0], intervals[0][1]]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= mergeIntervals[-1][1]:
                mergeIntervals[-1][1] = intervals[i][1] if intervals[i][1] > mergeIntervals[-1][1] else mergeIntervals[-1][1]
            else:
                mergeIntervals.append(intervals[i])
                
        return mergeIntervals
        