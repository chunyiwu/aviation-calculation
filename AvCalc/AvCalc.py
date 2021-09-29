import numpy as np
import matplotlib.pyplot as plt

"""Constants/parameters"""
REarth = 3443.92    # Earth radius in nautical mile
deg = np.pi / 180   # degrees to radians
rad = 180 / np.pi   # radians to degrees


"""Class definitions"""
class FlightPlan:
    """
    FlightPlan
    
    Contains a flight plan, with a list of waypoints
    """
    
    wps = []
    
    """ constructor """    
    def __init__(self, wps=[]):
        self.wps = wps
        
        
    """ waypoint edits"""
    def addWaypoint(self, wp):
        self.wps.append(wp)
        
        
        
    """ plotting """
    def plotFlightPlan(self):
        lons = []
        lats = []
        
        for wp in self.wps:
            lons.append(wp.lon)
            lats.append(wp.lat)            
            
        plt.plot(lons,lats,'k.-')
        plt.xlabel('Longitude [deg]')
        plt.ylabel('Latitude [deg]')
        plt.axis('equal')


class Waypoint:
    """
    Waypoint
    
    Contains the name and location of a waypoint
    """
    
    name = "WPNT"   # name 
    lat = 0         # latitude in degrees
    lon = 0         # longitude in degress
    
    """ constructor """    
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon 


""" Aviation calculations """
def getGreatCircleHeadingDistance(wp1, wp2):
    """
    getGreatCircleHeadingDistance
    
    Calculate the heading and distance between two way points using the 
    great circle.
    
    Inputs:
        wp1 - first waypoint
        wp2 - second waypoint
    
    Outputs:
        head - the true heading between the two points
        dist - the distance between the two points
        
    Reference:
        https://www.movable-type.co.uk/scripts/latlong.html
        
    """
    
    lat1 = wp1.lat * deg
    lon1 = wp1.lon * deg
    lat2 = wp2.lat * deg
    lon2 = wp2.lon * deg
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = np.sin(dlat/2)*np.sin(dlat/2) + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)*np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a));
    dist = REarth * c
    
    y = np.sin(dlon) * np.cos(lat2)
    x = np.cos(lat1)*np.sin(lat2) - -np.sin(lat1)*np.cos(lat2)*np.cos(dlon)
    q = np.arctan2(y, x)
    
    head = q * rad
    head = np.mod(head, 360)
    
    return head, dist

def getRhumbLineHeadingDistance(wp1, wp2):
    """
    getRhumbLineHeadingDistance
    
    Calculate the heading and distance between two way points using the 
    Rhumb Line.
    
    Rhumb line provides a constant bearing along the path.
    
    Inputs:
        wp1 - first waypoint
        wp2 - second waypoint
    
    Outputs:
        head - the true heading between the two points
        dist - the distance between the two points
        
    Reference:
        https://www.movable-type.co.uk/scripts/latlong.html
        
    """    
    
    lat1 = wp1.lat * deg
    lon1 = wp1.lon * deg
    lat2 = wp2.lat * deg
    lon2 = wp2.lon * deg
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    dphi = np.log(np.tan(np.pi/4+lat2/2)/np.tan(np.pi/4+lat1/2))
    if np.abs(dphi) > 1e-12:
        q = dlat / dphi
    else:
        q = np.cos(lat1)
        
    if np.abs(dlon) > np.pi:
        if dlon > 0:
            dlon = -(2*np.pi-dlon)
        else:
            dlon = 2*np.pi+dlon
    
    dist = np.sqrt(dlat*dlat+q*q*dlon*dlon) * REarth
    
    head = np.arctan2(dlon, dlat) * rad
    head = np.mod(head, 360)
    
    return head, dist
    
    
    
""" Auxillary functions """

    