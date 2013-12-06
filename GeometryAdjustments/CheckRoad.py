'''
Created on Oct 25, 2013

@author: kwalker
'''
import arcpy, math

class CheckRoad(object):
    
    _usrStartPnt = None
    _usrEndPnt = None
    _inputRoad = None
    _roadPoints = None
    adjustPoints = None
    
    def __init__(self, userStart, userEnd, userInputRoad):
        self._usrStartPnt = userStart
        self._usrEndPnt = userEnd
        self._inputRoad = userInputRoad
        self._roadPoints = self.getRoadPoints()
        self.adjustPoints = arcpy.Array()
        self._addAdjustPoints()
        
    def _distanceFormula(self, x1 , y1, x2, y2):
        d = math.sqrt((math.pow((x2 - x1),2) + math.pow((y2 - y1),2)))
        return d
    
    def _getRoadStartAndEndIndex(self):
        '''Takes the user-selected start and end points, finds the closest road points 
        to those start and end points, and returns their array indices in the form of a list.'''
        bufferDistance = 1
        
        rdStartPnt = None
        minstartDist = None
        startPntIndex = -1
        foundZeroDistStartPnt = False
        
        rdEndPnt = None
        minEndDist = None
        endPntIndex = -1
        foundZeroDistEndPnt = False
        
        i = 0;
        for point in self._roadPoints:
            startDist = self._distanceFormula(self._usrStartPnt.X, self._usrStartPnt.Y, point.X, point.Y)
            endDist = self._distanceFormula(self._usrEndPnt.X, self._usrEndPnt.Y, point.X, point.Y)
            
            #small rounding decimals make this useless right now
            if foundZeroDistStartPnt and foundZeroDistEndPnt:
                break
            
            #Select the point closest to the start point that is within the buffer
            if foundZeroDistStartPnt:
                foundZeroDistStartPnt = True
            elif minstartDist == None:
                rdStartPnt = point
                minstartDist = startDist
                startPntIndex = i              
            elif startDist <= 0.009:
                rdStartPnt = point
                minstartDist = startDist
                startPntIndex = i
                foundZeroDistStartPnt = True                                          
            elif startDist <= bufferDistance and startDist < minstartDist:
                rdStartPnt = point
                minstartDist = startDist
                startPntIndex = i
            
            #Select the point closest to the end point that is within the buffer
            if foundZeroDistEndPnt:
                foundZeroDistEndPnt = True
            elif minEndDist == None:
                rdEndPnt = point
                minEndDist = endDist
                endPntIndex = i              
            elif endDist <= 0.009:
                rdEndPnt = point
                minEndDist = endDist
                endPntIndex = i 
                foundZeroDistEndPnt = True                                          
            elif endDist <= bufferDistance and endDist < minEndDist:
                rdEndPnt = point
                minEndDist = endDist
                endPntIndex = i
            
            i += 1
            #print i                    
        
        if startPntIndex > endPntIndex:
            # switch points
            temp = rdStartPnt
            rdStartPnt = rdEndPnt
            rdEndPnt = temp
            # switch indexes
            temp2 = startPntIndex
            startPntIndex = endPntIndex
            endPntIndex = temp2
            
        return [startPntIndex, endPntIndex]
    
    def _addAdjustPoints(self):
        '''Adds the road points between and including the start and 
        end point to the adjustPoints array.'''
        roadStartEnd = self._getRoadStartAndEndIndex()
        tempArray = range(roadStartEnd[0], roadStartEnd[1] + 1)
        for index in tempArray:
            self.adjustPoints.add(self._roadPoints[index])
        
    def getAdjustPoints(self):
        return self.adjustPoints
    
    def getRoadPoints(self):
        '''Returns an arcpy.Array of road points.'''
        # self._roadPoints = []
        with arcpy.da.SearchCursor(self._inputRoad, "SHAPE@") as Cursor:
            for row in Cursor:
                return row[0].getPart(0)
            