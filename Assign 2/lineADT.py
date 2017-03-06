##  @file lineADT.py
#   @title lineADT
#   @author Susan Fayez
#   @date 2/14/2017

##  @brief importing from libraries needed
from pointADT import *

##  @brief A class for a line ADT
#   @details This class represents a line with two points (type PointT)
class LineT():
    
    ##  @brief Constructor for LineT
    #   @param p1 The beginning point of the line 
    #   @param p2 The end point of the line
    def __init__(self, p1, p2):
        if(isinstance(p1, PointT) and isinstance(p2, PointT)):
            self.b = p1
            self.e = p2
        else:
            print "Invaild type entered."
            self.b = None
            self.e = None

    ##  @brief Private method that calculates the average of two numbers
    #   @param x1 The first number
    #   @param x2 The second number
    #   @return The average of the two numbers
    

    ##  @brief Getter method for the beginning point of the line 
    #   @return The beginning point of the line
    def beg(self):
        return self.b

    ##  @brief Getter mothod for the end point of the line 
    #   @return The end point of the line
    def end(self):
        return self.e

    ##  @brief Returns the length of the line 
    #   @details uses dist() from pointADT.py to calculate the distance between the
    #   end point and the beginning point.
    #   @return the length of the line
    def len(self):
        return self.b.dist(self.e)

    ##  @brief returns the midpoint of the line 
    #   @details Implements __avg() to find the mid x-coordinate and mid y-coordinate
    #   and uses them to create a a new point to return
    #   @return The midpoint of the line, type PointT
    def mdpt(self):
        def __avg(x1, x2):
            return (x1 + x2) / 2.0
        x = __avg(self.b.xcrd(), self.e.xcrd())
        y = __avg(self.b.ycrd(), self.e.ycrd())
        return PointT(x, y)

    ##  @brief rotates the line about the origin
    #   @details Implements rot() from pointADT.py to rotate the beginning point and
    #   the end point.
    #   @param angle The angle by which to rotate the line, in radians
    def rot(self, angle):
        self.b.rot(angle)
        self.e.rot(angle)
