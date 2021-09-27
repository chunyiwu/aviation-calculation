# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:00:58 2021

@author: Chun-Yi Wu
"""

from AvCalc import *

wp1 = Waypoint('START',0,0)
wp2 = Waypoint('END',-10,10)

[headGC, distGC] = getGreatCircleHeadingDistance(wp1, wp2)
[headR, distR] = getRhumbLineHeadingDistance(wp1, wp2)

fp = FlightPlan()
fp.addWaypoint(wp1)
fp.addWaypoint(wp2)

fp.plotFlightPlan()