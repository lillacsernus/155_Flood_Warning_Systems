from floodsystem.geo import MonitoringStation
import floodsystem.geo
from floodsystem.stationdata import build_station_list



def test_stations_by_distance():
    stations = build_station_list()
    p =(52.2053, 0.1218)
    x = floodsystem.geo.stations_by_distance(stations, p)
    x = dict(x)
    assert x['Cambridge Jesus Lock'] == 0.840237595667494

   
def test_stations_within_radius():
    centre = (52.2053, 0.1218)
    stations = build_station_list()
    y = floodsystem.geo.stations_within_radius(stations, centre, 10)
    assert len(y) == 11


def test_rivers_with_station():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s_i = "test-s-id"
    m_i = "test-m-id"
    labe = "some station"
    coor = (-2.0, 4.0)
    trang = (-2.3, 3.4445)
    rive = "River X"
    tow = "My Town"
    d = MonitoringStation(s_i, m_i, labe, coor, trang, rive, tow)
    t = [s, d]
    x = floodsystem.geo.rivers_with_station(t)
    assert x == {'River X'}
   


def test_stations_by_river():
    stations = build_station_list()
    u = floodsystem.geo.stations_by_river(stations)
    a = len(u['River Cam'])
    assert a == 7


def test_rivers_by_station_number():
    stations = build_station_list()
    x = floodsystem.geo.rivers_by_station_number(stations,9)
    x = dict(x)
    assert x['River Thames'] == 55


