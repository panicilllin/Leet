class UndergroundSystem:

    def __init__(self):
        self.in_station = {}
        self.station_map = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_station[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_info = self.in_station[id]
        station_pair = str(check_in_info[0] + '-' + stationName)
        time_cost = t - check_in_info[1]
        # del self.in_station[id]
        if not self.station_map.get(station_pair):
            self.station_map[station_pair] = [time_cost]
        else:
            self.station_map[station_pair].append(time_cost)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station_pair = str(startStation + '-' + endStation)
        if not self.station_map.get(station_pair):
            return -1
        else:
            station_times = self.station_map.get(station_pair)
            return (sum(station_times)+0.0)/len(station_times)




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

if __name__ == "__main__":
    struct = ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    inpt = [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

    a = UndergroundSystem()
    for i in range(1,len(struct)):
        if struct[i] == "checkIn":
            a.checkIn(inpt[i][0],inpt[i][1],inpt[i][2])
        elif struct[i] == "checkOut":
            a.checkOut(inpt[i][0],inpt[i][1],inpt[i][2])
        elif struct[i] == "getAverageTime":
            print(a.getAverageTime(inpt[i][0],inpt[i][1]))

