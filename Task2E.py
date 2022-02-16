from floodsystem.stationdata import build_station_list
import floodsystem.plot
import floodsystem.flood
import floodsystem.datafetcher
import matplotlib.pyplot as plt
from datetime import timedelta, datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
import matplotlib.pyplot as plt



def run():
    stations = build_station_list()
    update_water_levels(stations)
    y = floodsystem.flood.stations_highest_rel_level(stations, N=5)
    print(y)
    
    dt = 10
    
    station_list = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in stations:
            if n.name == station_name:
                station_list.append(n)
    
    
    for s in range(len(station_list)-1):
        dates, levels = fetch_measure_levels(station_list[s].measure_id, dt=timedelta(days=dt))
        floodsystem.plot.plot_water_levels(station_list[s], dates, levels)
        
    

        
    
     
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()