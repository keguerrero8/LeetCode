class Solution(object):
    def insert(self, intervals, newInterval):
        mergedInterval = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                mergedInterval.append(newInterval)
                mergedInterval = mergedInterval + intervals[i:]
                return mergedInterval
            elif newInterval[0] <= intervals[i][1]:
                mergedInterval.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
                j = i+1
                while j < len(intervals) and intervals[j][0] <= mergedInterval[-1][1]:
                    mergedInterval[-1] = [min(mergedInterval[-1][0], intervals[j][0]), max(mergedInterval[-1][1], intervals[j][1])]
                    j += 1
                if j == len(intervals):
                    return mergedInterval
                else:
                    mergedInterval = mergedInterval + intervals[j:]
                    return mergedInterval 
            else:
                mergedInterval.append(intervals[i])
                
        mergedInterval.append(newInterval)
                
        return mergedInterval
            
            
        