# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        if bottomLeft.x == topRight.x and topRight.y == bottomLeft.y:
            return 1
        
        midx = (topRight.x + bottomLeft.x) // 2
        midy = (topRight.y + bottomLeft.y) // 2
        
        return self.countShips(sea, Point(midx, midy), bottomLeft) + self.countShips(sea, Point(topRight.x, midy), Point(midx+1, bottomLeft.y)) + self.countShips(sea, Point(midx, topRight.y), Point(bottomLeft.x, midy+1)) + self.countShips(sea, topRight, Point(midx+1, midy+1)) 
        