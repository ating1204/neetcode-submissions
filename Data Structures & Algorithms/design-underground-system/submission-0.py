class UndergroundSystem:

    def __init__(self):
        
        self.ids = {} #elem: id: [stationName, t]
        self.averages = {} #elem: (stationA, stationB) : [total time, number times]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.ids:
            return #invalid
        self.ids[id] = [stationName, t]


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.ids:
            return #invalid
        time =  t - self.ids[id][1]
        stationA = self.ids[id][0]
        
        self.averages.setdefault((stationA, stationName), [0,0])[0] += time
        self.averages.setdefault((stationA, stationName), [0,0])[1] += 1
    
        self.ids.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[(startStation, endStation)][0] /  self.averages[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)