'''
Created on Nov 27, 2013

@author: kwalker
'''
import unittest, os, arcpy
from CheckRoad import *
from Boundary import *

class Test_CheckRoad(unittest.TestCase):

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
        actualXDist = abs(startPoint.X - adjustPointList[0].X)
        actualYDist = abs(startPoint.Y - adjustPointList[0].Y)
        self.assertTrue(abs(startPoint.X - adjustPointList[0].X) < self._rdXyResolution, "start point X compare")
        

class Test_CheckRoad2(unittest.TestCase):

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
    
    def testStuff(self):
        #print self._rdXyResolution
        startPoint = arcpy.Point(459835.1, 4192564.56)
        endPoint = arcpy.Point(460357.8, 4192102.6)
        checkroadtester1 = CheckRoad(startPoint, endPoint, self._checkRoadInputRoad)
        adjustPointList = checkroadtester1.getAdjustPoints()
        actualXDist = abs(startPoint.X - adjustPointList[0].X)
        actualYDist = abs(startPoint.Y - adjustPointList[0].Y)
        self.assertTrue(abs(startPoint.X - adjustPointList[0].X) < self._rdXyResolution, "start point X compare")        
          
        
class Test_Boundary(unittest.TestCase):
    _adjustPoints = {"InsideBoundary" : arcpy.Array()}#, arcpy.Point(464369.54, 4198802.18),
                                #arcpy.Point(464365.09, 4197705.4), arcpy.Point(464367.32, 4197182.6))}
#     _expectedBndReplacedPoints = {"InsideBoundary" : arcpy.Array(arcpy.Point(464387.510, 4199741.310), arcpy.Point(464387.420, 4199721.210),
#                                 arcpy.Point(464378.840, 4198132.960), arcpy.Point(464378.750, 4198112.860),
#                                 arcpy.Point(464380.780, 4197328.900))}
    _inputBoundary = None
    _tempDatabasePath = None
    _rdXyResolution = 0.0
       
    @classmethod
    def setUpClass(self):
        print "Class setup"
        self._inputBoundary = os.path.join(os.path.dirname(__file__), "data", "BoundaryToRoadAdjust.gdb", "Boundary")
        self._tempDatabasePath = r"C:\Users\kwalker\Documents\Aptana Studio 3 Workspace\BoundaryToRoadAdjustments\GeometryAdjustments\data\TempBoundaryToRoadAdjustments.gdb"
           
        roadSpatialRef = arcpy.Describe(self._inputBoundary).spatialReference
        self._rdXyResolution = roadSpatialRef.XYResolution
  
    def tearDown(self):
        pass
  
    def testName(self):
        boundaryGeometries = []
        with arcpy.da.SearchCursor(self._inputBoundary, "SHAPE@") as Cursor:
            for row in Cursor:
                boundaryGeometries.append(row[0])
                
        self._adjustPoints["InsideBoundary"].add(arcpy.Point(464373.99, 4199785.49))
        self._adjustPoints["InsideBoundary"].add(arcpy.Point(464367.32, 4197182.6)) 
           
        testBoundary = Boundary(self._adjustPoints["InsideBoundary"], boundaryGeometries[0])
        actualBndStartAndEnd = testBoundary._findStartAndEndIndex()
        actualStartIndex = actualBndStartAndEnd[0]
        actualEndIndex= actualBndStartAndEnd[1]
        print actualStartIndex
        print actualEndIndex
           
        self.assertTrue(actualStartIndex == 9 and actualEndIndex == 13, "Compare index to data")

        
       
if __name__ == "__main__":
    #import sys;sys.argv = ['--verbose', 'Test_CheckRoad']
    unittest.main()