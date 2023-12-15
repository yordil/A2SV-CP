class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  
        self.trip_history = {}  

    def checkIn(self, traveler_id: int, start_station: str, check_in_time: int) -> None:
        self.check_ins[traveler_id] = (start_station, check_in_time)
#         tuple of values for......

    def checkOut(self, traveler_id: int, end_station: str, check_out_time: int) -> None:
        start_station, check_in_time = self.check_ins.pop(traveler_id)
        key = (start_station, end_station)
        total_time, total_trips = self.trip_history.get(key, (0, 0))
        self.trip_history[key] = (total_time + (check_out_time - check_in_time), total_trips + 1)

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        key = (start_station, end_station)
        total_time, total_trips = self.trip_history.get(key, (0, 0))
        return total_time / total_trips if total_trips != 0 else 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)