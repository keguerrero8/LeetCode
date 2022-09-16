class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.averageTimes = {}

    def checkIn(self, id, stationName, t):
        #{id: [stationName, t]}
        if id not in self.averageTimes:
            self.checkins[id] = [stationName, t]
        self.checkins[id][0] = stationName
        self.checkins[id][1] = t

    def checkOut(self, id, stationName, t):
        startTime, startStation = self.checkins[id][1], self.checkins[id][0]
        if startStation not in self.averageTimes:
            self.averageTimes[startStation] = {stationName: [t - startTime, 1]}
        else:
            if stationName not in self.averageTimes[startStation]:
                self.averageTimes[startStation][stationName] = [t-startTime, 1]
            else:
                self.averageTimes[startStation][stationName][0] += (t - startTime)
                self.averageTimes[startStation][stationName][1] += 1 

    def getAverageTime(self, startStation, endStation):
        totalTime = self.averageTimes[startStation][endStation][0]
        count = self.averageTimes[startStation][endStation][1]
        return totalTime/count
        
# "checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","getAverageTime","checkIn","getAverageTime","getAverageTime","checkOut"]

# [[37043,"K2618O72",29],[37043,"U1DTINDT",39],["K2618O72","U1DTINDT"],[779975,"K2618O72",112],[779975,"CN3K6CYM",157],["K2618O72","U1DTINDT"],[706901,"K2618O72",221],["K2618O72","CN3K6CYM"],[18036,"K2618O72",258],["K2618O72","U1DTINDT"],["K2618O72","CN3K6CYM"],[18036,"U1DTINDT",293]]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)