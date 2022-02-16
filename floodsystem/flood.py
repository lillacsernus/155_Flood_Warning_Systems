from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels
from pickle import TUPLE1
from floodsystem.station import MonitoringStation
from haversine import haversine

stations = build_station_list()
update_water_levels(stations)

def stations_level_over_threshold(stations, tol):
    z = []
    for n in range(len(stations)):
        x = stations[n].typical_range_consistent()
        if x == True:
            y = stations[n].relative_water_level()
            if y == None:
                pass
            elif y > tol:
                Tuple2 = (stations[n].name, stations[n].relative_water_level())
                z.append(Tuple2)
    h = sorted_by_key(z,1)
    h.reverse()
    return h

def stations_highest_rel_level(stations, N):
    AllStations = stations_level_over_threshold(stations, 0)
    return AllStations[:N]
