'''
Created on Nov 27, 2013

@author: kwalker
'''
import unittest, os, arcpy
from CheckRoad import *



class Test(unittest.TestCase):

    _inputRoad = None
    _checkRoadInputRoad = None
    _inputBoundary = None
    _tempDatabasePath = None
    _rdXyResolution = 0.0
    
    @classmethod
    def setUpClass(self):
        print "Class setup"
        self._inputRoad = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "Roads")
        self._checkRoadInputRoad = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "CheckRoadAdjustPointsTestRoad")
        self._inputBoundary = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "Boundary")
        self._tempDatabasePath = "C:\Users\kwalker\Documents\Aptana Studio 3 Workspace\BoundaryToRoadAdjustments\GeometryAdjustments\data\TempBoundaryToRoadAdjustments.gdb"
        
        roadSpatialRef = arcpy.Describe(self._checkRoadInputRoad).spatialReference
        self._rdXyResolution = roadSpatialRef.XYResolution



    def tearDown(self):
        pass


    def testName(self):
        print self._rdXyResolution
        startPoint = arcpy.Point(459835.1, 4192564.56)
        endPoint = arcpy.Point(460357.8, 4192102.6)
        checkroadtester1 = CheckRoad(startPoint, endPoint, self._checkRoadInputRoad)
        adjustPointList = checkroadtester1.getAdjustPoints()
        self.assertTrue(abs(startPoint.X - adjustPointList[0].X) < .001, "start point X compare")
#         for point in checkroadtester1.getAdjustPoints():
#             print point
    def testName1(self):
        print self._rdXyResolution
        startPoint = arcpy.Point(459835.1, 4192564.56)
        endPoint = arcpy.Point(460357.8, 4192102.6)
        checkroadtester1 = CheckRoad(startPoint, endPoint, self._checkRoadInputRoad)
        adjustPointList = checkroadtester1.getAdjustPoints()
        self.assertTrue(abs(startPoint.X - adjustPointList[0].X) == 9, "start point X compare")
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['--verbose', 'Test']
    unittest.main()