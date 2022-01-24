# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .station import MonitoringStation
import floodsystem.utils  # noqa

from haversine import haversine



def stations_by_distance(stations, p):
    """This function returns a list of (station, distance) tuples 
    where distance is the distance from coordinate p"""
    distances = []
    for n in range(len(stations)):
        distance = haversine(stations[n].coord, p)
        tuple = (stations[n].name, distance)
        distances.append(tuple)
        distances_list = floodsystem.utils.sorted_by_key(distances, 1)
    return distances_list

def stations_within_radius(stations, centre, r):
    """This function returns a list of all stations (type MonitoringStation) 
    within radius r of a geographic coordinate x."""
    list_stations = []
    for n in range(len(stations)):
        radius = haversine(stations[n].coord, centre)
        if radius <= r:
            list_stations.append(stations[n].name)
            list_stations.sort()
    return list_stations