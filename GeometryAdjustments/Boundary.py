'''
Created on Nov 29, 2013

@author: kwalker
'''
import arcpy, math

class Boundary(object):
    
    _adjustPoints = None
    _boundaryGeometry = None
    _boundaryPoints = None
    
    def __init__(self, adjustPoints, boundaryGeometry):
        self._adjustPoints = adjustPoints
        self._boundaryGeometry = boundaryGeometry
        self._boundaryPoints = self._getBoundaryArray()
        
    def _getBoundaryArray(self):
        return self._boundaryGeometry.getPart(0)
    
    def _findStartAndEndIndex(self):
        '''Finds the closest boundary points to the start and end road points. 
        Booleans replaceStart and replaceEnd determine whether the start and end boundary points should 
        be replaced with the start and end road points based on their proximity to each other.
        Returns a list containing: start index, end index, replaceStart?, replaceEnd?'''
        startIndex = None
        endIndex = None
        startDist = None
        endDist = None
        replaceStart = False
        replaceEnd = False
        startAdjustPoint = self._adjustPoints[0]
        endAdjustPoint = self._adjustPoints[self._adjustPoints.count - 1]
        bufferDistance = 1
        i = 0
        
        for point in self._boundaryPoints:
            tempStartDist = self._distanceFormula(point.X, point.Y, startAdjustPoint.X, startAdjustPoint.Y)
            tempEndDist = self._distanceFormula(point.X, point.Y, endAdjustPoint.X, endAdjustPoint.Y)
            
            if i == 0:
                startDist = tempStartDist
                startIndex = i
                endDist = tempEndDist
                endIndex = i
            else:
                if tempStartDist < startDist:
                    startDist = tempStartDist
                    startIndex = i

                if tempEndDist < endDist:
                    endDist = tempEndDist
                    endIndex = i
                    
            i += 1
            
        if startDist < bufferDistance:
            replaceStart = True
        if endDist < bufferDistance:
            replaceEnd = True
            
        return [startIndex, endIndex, replaceStart, replaceEnd]
    
    def _replaceBoundaryPoints(self):
        '''Replaces points in _boundaryPoints with _adjustPoints.'''
        startEndIndices = self._findStartAndEndIndex() 
        insertIndex = startEndIndices[0] + 1
        
        # Replace start point
        if startEndIndices[2]:
            self._boundaryPoints.replace(startEndIndices[0], self._adjustPoints[0])
        # Replace end point
        if startEndIndices[3]:
            self._boundaryPoints.replace(startEndIndices[1], self._adjustPoints[self._adjustPoints.count - 1])  
            
        for point in self._adjustPoints:
            self._boundaryPoints.insert(insertIndex, point)
            insertIndex += 1
    
    def getUpdatedBoundary(self):
        '''Returns updated boundary as a geometry object.'''
        pass
    
    def _distanceFormula(self, x1 , y1, x2, y2):
        d = math.sqrt((math.pow((x2 - x1),2) + math.pow((y2 - y1),2)))
        return d
    