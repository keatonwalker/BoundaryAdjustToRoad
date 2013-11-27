'''
Created on Oct 11, 2013

@author: kwalker
'''
import arcpy
import os

class AdjustmentRoadFinder (object):
    
    _inputRoads = None
    _tempGDB = None
    
    def __init__(self, inputRoads, tempGDB):
        self._inputRoads = inputRoads
        self._tempGDB = tempGDB
        
    def getRoadsToCheck(self, boundary, searchDistance, outputFeatureName):
        roadsToCheck = os.path.join(self._tempGDB, outputFeatureName)
        roadLayer = "road_layer"
        
        if arcpy.Exists(roadLayer):
            arcpy.Delete_management(roadLayer)
        
        arcpy.MakeFeatureLayer_management(self._inputRoads, roadLayer)
        arcpy.SelectLayerByLocation_management(roadLayer, 'WITHIN_A_DISTANCE', boundary, searchDistance)
        arcpy.CopyFeatures_management(roadLayer, roadsToCheck)
        
        print int(arcpy.GetCount_management(roadLayer).getOutput(0))
        return roadsToCheck