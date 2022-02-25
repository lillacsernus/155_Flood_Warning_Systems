from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import plot_water_level_with_fit, polyfit
from floodsystem.flood import stations_highest_rel_level
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import plot_water_level_with_fit
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations_list = []
    for station in stations:
        if station.name not in inconsistent_stations:
            stations_list.append(station)
        else:
            pass
    y = stations_highest_rel_level(stations_list, N=7)
    
    
    station_list_two = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in stations_list:
            if n.name == station_name:
                station_list_two.append(n)
    
    for n in range(len(station_list_two)-1):
        dt = 2
        dates, levels = fetch_measure_levels(station_list_two[n].measure_id, timedelta(days=dt))
        if len(dates) != 0 and np.size(levels) != 0:
            polyfit(dates, levels, p=4)
        
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()




def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations_list = []
    for station in stations:
        if station.name not in inconsistent_stations:
            stations_list.append(station)
        else:
            pass
    y = stations_highest_rel_level(stations_list, N=7)
    
    print(y)
    

    station_list_two = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in stations_list:
            if n.name == station_name:
                station_list_two.append(n)
    

    for n in range(len(station_list_two)-1):
        dt = 10
        dates, levels = fetch_measure_levels(station_list_two[n].measure_id, dt=timedelta(days=dt))
        stations_list = []
        if len(dates) != 0 and np.size(levels) != 0:
            plot_water_level_with_fit(station_list_two[n], dates, levels, p=4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()