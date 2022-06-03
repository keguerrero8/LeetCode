class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals) == 1:
            return 1
        
        startingTimes = []
        endTimes = []
        
        for interval in intervals:
            startingTimes.append(interval[0])
            endTimes.append(interval[1])
            
        startingTimes.sort()
        endTimes.sort()
        
        i = j = 0
        
        maxRooms = 1
        currentRooms = 0
        while i < len(startingTimes):
            if startingTimes[i] < endTimes[j]:
                currentRooms += 1
                i += 1
            else:
                currentRooms -= 1
                j += 1
            maxRooms = max(maxRooms, currentRooms)  
                
        return maxRooms
            
        