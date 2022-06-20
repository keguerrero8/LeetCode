class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        maxUnits = 0
        boxTypes.sort(key = lambda x: x[1])
        
        for i in reversed(range(len(boxTypes))):
            if truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                maxUnits += boxTypes[i][0]*boxTypes[i][1]
            else:
                maxUnits += boxTypes[i][1]*truckSize
                break
                
        return maxUnits
        