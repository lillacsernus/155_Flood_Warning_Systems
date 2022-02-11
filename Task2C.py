from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_highest_rel_level(stations, 8)
    for n in range(len(x)):
        print("{}, {}".format(x[n][0], x[n][1]))