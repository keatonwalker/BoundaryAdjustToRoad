'''
Created on Oct 18, 2013

@author: kwalker
'''
import os
from GeometryAdjuster import *
from CheckRoad import *

class GeometryAdjusterTest(object):
    
    inputRoad = None
    inputBoundary = None
    tempDatabasePath = None
   
    def __init__(self):
        self.inputRoad = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "Roads")
        self.checkRoadInputRoad = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "CheckRoadAdjustPointsTestRoad")
        self.inputBoundary = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "Boundary")
        self.tempDatabasePath = "C:\Users\kwalker\Documents\Aptana Studio 3 Workspace\BoundaryToRoadAdjustments\GeometryAdjustments\data\TempBoundaryToRoadAdjustments.gdb"

        
    def runAdjustmentRoadFinderTest(self):
        adjustmentroadfindertester = AdjustmentRoadFinder(self.inputRoad, self.tempDatabasePath)
        adjustmentroadfindertester.getRoadsToCheck(self.inputBoundary, 30.48, "CheckedRoads")
        
    def runCheckRoadAdjustPointsTest(self):
        startPoint = arcpy.Point(459835.1, 4192564.56)
        endPoint = arcpy.Point(460357.8, 4192102.6)
        checkroadtester1 = CheckRoad(startPoint, endPoint, self.checkRoadInputRoad)
        for point in checkroadtester1.getAdjustPoints():
            print point
            
    def runCheckRoadRoadPointsTest(self):
        checkroadtester2 = CheckRoad(2, 3, self.checkRoadInputRoad)
        for point in checkroadtester2._roadPoints:
            print point
            
    def runCheckRoad_getStartAndEndPoint(self):
        startPoint = arcpy.Point(459835.1, 4192564.56)
        endPoint = arcpy.Point(460357.8, 4192102.6)
        checkroadtester2 = CheckRoad(startPoint, endPoint, self.checkRoadInputRoad)
        startAndEndPnts = checkroadtester2._getRoadStartAndEndPoint()
        print "start: {}, {}\nend: {}, {}".format(startAndEndPnts[0].X, startAndEndPnts[0].Y, startAndEndPnts[1].X, startAndEndPnts[1].Y)
        
test1 = GeometryAdjusterTest()

# test1.runAdjustmentRoadFinderTest()
# test1.runCheckRoadRoadPointsTest()
test1.runCheckRoadAdjustPointsTest()
# test1.runCheckRoad_getStartAndEndPoint()


