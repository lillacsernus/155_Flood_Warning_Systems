from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.analysis
import floodsystem.flood
import floodsystem.datafetcher
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels


def run():
    station = build_station_list()
    update_water_levels(station)
    y = floodsystem.flood.stations_highest_rel_level(station, N=5)
    
    
    station_list = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in station:
            if n.name == station_name:
                station_list.append(n)
    
    for n in station_list:
        dt = 2
        dates, levels = fetch_measure_levels(n.measure_id, dt=timedelta(days=dt))
        x = floodsystem.analysis.polyfit(dates, levels, p=4)
        return x


def run():
    stations = build_station_list()
    update_water_levels(stations)
    y = floodsystem.flood.stations_highest_rel_level(stations, N=5)
    
    station_list = []
    for name in y:
        station_name = name[0]
    # Find station
        for n in stations:
            if n.name == station_name:
                station_list.append(n)
    

    for n in station_list:
        dt = 10
        dates, levels = fetch_measure_levels(n.measure_id, dt=timedelta(days=dt))
        x = plot_water_levels(n, dates, levels)
        return x
    
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()