class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals) == 1:
            return 1
        startTimes = [interval[0] for interval in intervals]
        endTimes = [interval[1] for interval in intervals]
        startTimes.sort()
        endTimes.sort()
        
        start, end = 0, 0
        rooms = 0
        maxRooms = 0
        
        while start < len(startTimes):
            if startTimes[start] < endTimes[end]:
                rooms += 1
                maxRooms = max(rooms, maxRooms)
                start += 1
            else:
                rooms -= 1
                end += 1
                
        return maxRooms