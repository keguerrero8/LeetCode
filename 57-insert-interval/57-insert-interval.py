class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        res.append(newInterval)
        return res