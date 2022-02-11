from floodsystem.stationdata import build_station_list
import floodsystem.geo 
from floodsystem.utils import sorted_by_key

def run():
    stations=build_station_list()
    z=floodsystem.geo.rivers_by_station_number(stations,9)
<<<<<<< HEAD
    print(z)
=======
    print (z)
>>>>>>> 099056c5dea404370d71646df8421ff69bb5e65e
    print(len(z))


    




if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
   