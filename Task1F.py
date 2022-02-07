from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
import floodsystem.geo
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_stations
def run():
    stations=build_station_list()
    z = inconsistent_typical_range_stations(stations)
    return z




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()