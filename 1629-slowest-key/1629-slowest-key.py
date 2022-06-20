class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        longestDuration = releaseTimes[0]
        largestKey = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            currentDuration = releaseTimes[i] - releaseTimes[i-1]
            if currentDuration > longestDuration:
                longestDuration = currentDuration
                largestKey = keysPressed[i]
            elif currentDuration == longestDuration:
                largestKey = max(keysPressed[i], largestKey)
                
        return largestKey
        