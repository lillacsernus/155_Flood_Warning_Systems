from floodsystem.stationdata import build_station_list
import floodsystem.plot
import floodsystem.flood
import floodsystem.datafetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    y = floodsystem.flood.stations_highest_rel_level(stations, N=5)
    print(y)

    for station in y:
        dt = 10
        x = floodsystem.plot.plot_water_levels(station, dates, times)
        return x
    
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()