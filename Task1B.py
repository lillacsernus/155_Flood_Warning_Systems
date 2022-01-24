

from floodsystem.stationdata import build_station_list
import floodsystem.geo
from floodsystem.utils import sorted_by_key
p = (52.2053, 0.1218)

def run():
    stations = build_station_list()
    

    x = floodsystem.geo.stations_by_distance(stations, p)

    print(x[:10])
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()









