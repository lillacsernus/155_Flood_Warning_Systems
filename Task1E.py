from floodsystem.stationdata import build_station_list
import floodsystem.geo
from floodsystem.utils import sorted_by_key
def run():
    stations=build_station_list()
    z=floodsystem.geo.rivers_by_station_number(stations,9)
    print (z)
def test_rivers_by_number():
    z = dict(z)
    assert z['Thames']== 55

    




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
   