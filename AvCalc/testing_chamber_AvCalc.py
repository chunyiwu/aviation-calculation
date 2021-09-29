from AvCalc import *

wp1 = Waypoint('START',0,0)
wp2 = Waypoint('END',-10,10)

[headGC, distGC] = getGreatCircleHeadingDistance(wp1, wp2)
[headR, distR] = getRhumbLineHeadingDistance(wp1, wp2)

fp = FlightPlan()
fp.addWaypoint(wp1)
fp.addWaypoint(wp2)

fp.plotFlightPlan()


map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')