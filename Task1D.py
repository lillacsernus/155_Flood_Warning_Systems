from numpy import size
from floodsystem.stationdata import build_station_list
import floodsystem.geo

def run():

    stations = build_station_list()
    z = sorted(floodsystem.geo.rivers_with_station(stations))
    print("There are" + "  " + str(len(z)) + "  " + "rivers with at least one monitoring station.")
    print("The first 10 rivers in the list are:" .format(z[:10]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()


def run():

    stations = build_station_list()
    u = floodsystem.geo.stations_by_river(stations)
    a = sorted(u['River Aire'])
    b = sorted(u['River Cam'])
    c = sorted(u['River Thames'])
    print(a)
    print(b)
    print(c)
    
    
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()




