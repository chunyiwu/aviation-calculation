# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 21:06:06 2021

@author: Chun-Yi Wu
"""

import numpy as np

REarth = 3443.92        # Earth radius in nautical mile
deg = np.pi / 180   # degrees to radians
rad = 180 / np.pi   # radians to degrees

class Waypoint:
    """
    Waypoint: contains the name and location of a waypoint
    """
    
    name = "WPNT"   # name 
    lat = 0         # latitude in degrees
    lon = 0         # longitude in degress
    
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon 



def getHeadingAndDistance(wp1, wp2):
    lat1 = wp1.lat * deg
    lon1 = wp1.lon * deg
    lat2 = wp2.lat * deg
    lon2 = wp2.lon * deg
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat/2)*np.sin(dlat/2) + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)*np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a));
    d = REarth * c
    
    y = np.sin(dlon) * np.cos(lat2)
    x = np.cos(lat1)*np.sin(lat2) - -np.sin(lat1)*np.cos(lat2)*np.cos(dlon)
    q = np.arctan2(y, x)
    
    h = np.mod(-(q*rad - 90), 360)
    
    return h, d


wp1 = Waypoint('START',0,0)
wp2 = Waypoint('END',-1,1)

[head, dist] = getHeadingAndDistance(wp1, wp2)