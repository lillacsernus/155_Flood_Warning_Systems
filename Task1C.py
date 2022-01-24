from floodsystem.stationdata import build_station_list
import floodsystem.geo

centre = (52.2053, 0.1218)

def run():
    stations = build_station_list()
    

    y = floodsystem.geo.stations_within_radius(stations, centre, 10)

    print(y)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()