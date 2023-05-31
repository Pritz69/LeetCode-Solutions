class UndergroundSystem:

    def __init__(self):
        self.travel = {}
        self.travelt = {}

    def checkIn(self, id: int, startstationName: str, t: int) -> None:
        self.travel[id] = (startstationName,t)

    def checkOut(self, id: int, endstationName: str, t: int) -> None:
        start,time = self.travel[id]
        route = (start,endstationName)
        if route not in self.travelt :
            self.travelt[route] = [0,0]
        self.travelt[route][0] += t-time
        self.travelt[route][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,count = self.travelt[(startStation,endStation)]
        return time/count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
