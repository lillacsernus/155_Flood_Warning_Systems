# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .station import MonitoringStation
import floodsystem.utils  # noqa

from datetime import datetime, timedelta

from haversine import haversine



def stations_by_distance(stations, p):
    """This function returns a list of (station, distance) tuples 
    where distance is the distance from coordinate p"""
    distances = []
    for n in stations:
        distance = haversine(n.coord, p)
        tuple = (n.name, distance)
        distances.append(tuple)
        distances_list = floodsystem.utils.sorted_by_key(distances, 1)
    return distances_list

def stations_within_radius(stations, centre, r):
    """This function returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate x."""
    list_stations = []
    for n in stations:
        radius = haversine(n.coord, centre)
        if radius <= r:
            list_stations.append(n.name)
    list_stations.sort()
    return list_stations

def rivers_with_station(stations):
    """This function, given a list of station objects, returns a container 
    (list/tuple/set) with the names of the rivers with a monitoring station. """
    x = set()
    for n in stations:
        x.add(n.river)
    return x

def stations_by_river(stations):
    """This function returns a Python dict (dictionary) that maps river 
    names (the key) to a list of station objects on a given river."""
    y = {}
    for n in stations:
        if n.river not in y:
            y[n.river] = [n.name]
        else: y[n.river].append(n.name)
    return y
    
def rivers_by_station_number(stations,N):
    """This function returns a list of rivers with stations above a set threshold N"""
    hi = {}
    for n in range(len(stations)):
        if stations[n].river not in hi:
            hi.update({stations[n].river : 1})
        else:
            hi[stations[n].river] = hi[stations[n].river] + 1
    hello = list(hi.items())
    hello.sort(key = lambda x: x[1], reverse = True)
    y = hello[:N]
    g = hello[N:]
    for i in range(len(g)):
        if g[i][1] == y[N-1][1]:
            y.append(g[i])
        else:
            pass
    return y


