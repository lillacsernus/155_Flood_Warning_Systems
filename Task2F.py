from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import plot_water_level_with_fit, polyfit
import floodsystem.flood
import floodsystem.datafetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import plot_water_level_with_fit


def run():
    station = build_station_list()
    update_water_levels(station)
    y = floodsystem.flood.stations_highest_rel_level(station, N=7)
    z = y[2:]
    
    station_list = []
    for name in z:
        station_name = name[0]
    # Find station
        for n in station:
            if n.name == station_name:
                station_list.append(n)
    
    for n in range(len(station_list)):
        dt = 2
        dates, levels = fetch_measure_levels(station_list[n].measure_id, dt=timedelta(days=dt))
        polyfit(dates, levels, p=4)
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()

def run():
    stations = build_station_list()
    update_water_levels(stations)
    y = floodsystem.flood.stations_highest_rel_level(stations, N=7)
    z = y[2:]

    station_list = []
    for name in z:
        station_name = name[0]
    # Find station
        for n in stations:
            if n.name == station_name:
                station_list.append(n)
    

    for n in range(len(station_list)):
        dt = 10
        dates, levels = fetch_measure_levels(station_list[n].measure_id, dt=timedelta(days=dt))
        plot_water_level_with_fit(station_list[n], dates, levels, p=4)
        
    
    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()