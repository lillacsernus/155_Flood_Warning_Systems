from floodsystem.analysis import polyfit, get_gradient
from datetime import datetime, timedelta
import matplotlib
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels

def test_poyfit():
    dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
    levels = [0, 1, 8, 27, 64, 125, 216]
    a, x0 = polyfit(dates, levels, p=3)
    assert round(a[0]) == 0
    assert round(a[1]) == 0
    assert round(a[2]) == 0
    assert round(a[3]) == 1

def test_get_gradient():
    dates = dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
    dates_num = matplotlib.dates.date2num(dates)
    levels = [0, 2, 4, 6, 8, 10, 12]
    g = get_gradient(dates_num, levels, p=1)
    print(g)
    assert round(g) == 2
test_get_gradient()

def test_stations_level_over_threshold():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-1, 1)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_id_1 = "test-s-id1"
    m_id_1 = "test-m-id 1"
    label_1 = "some other station"
    coord_1 = (-2.0, 1.0)
    trange_1 = (-1, 1)
    river_1 = "River Y"
    town_1 = "My Other Town"
    s_1 = MonitoringStation(s_id_1, m_id_1, label_1, coord_1, trange_1, river_1, town_1)
    s.latest_level = 0
    s_1.latest_level = 0
    stations = [s, s_1]
    x = stations_level_over_threshold(stations, 0)
    print(x)
    assert len(x) == 2

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_highest_rel_level(stations, 5)
    assert len(x) == 5


