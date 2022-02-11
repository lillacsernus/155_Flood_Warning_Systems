from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from haversine import haversine
stations = build_station_list()
update_water_levels(stations)

def test_stations_level_over_threshold():
    x = stations_level_over_threshold(stations, 0.8)
    assert len(x) > 0
    