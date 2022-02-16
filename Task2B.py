from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from pickle import TUPLE1
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.utils import sorted_by_key
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
stations = build_station_list()
update_water_levels(stations)
def run():
    z = stations_level_over_threshold(stations, 0.8)
    for n in range(len(z)):
        print("{}, {}".format(z[n][0], z[n][1]))



if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()