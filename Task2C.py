from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations_list = []
    for station in stations:
        if station not in inconsistent_stations:
            stations_list.append(station)
        else:
            pass
    
    x = stations_highest_rel_level(stations_list, 8)
    for n in range(len(x)):
        print("{}, {}".format(x[n][0], x[n][1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()