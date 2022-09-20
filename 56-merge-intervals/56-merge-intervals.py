class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        mergedIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= mergedIntervals[-1][1]:
                mergedIntervals[-1][0] = min(mergedIntervals[-1][0], intervals[i][0])
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], intervals[i][1])
            else:
                mergedIntervals.append(intervals[i])
                
        return mergedIntervals
                
        