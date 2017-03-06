##  @file pointADT.py
#   @title pointADT
#   @author Susan Fayez
#   @date 2/14/2017

##  @brief importing from libraries needed
import math

##  @brief A class for a point ADT
#   @details This class represents a point with x and y coordinates   
class PointT():
    
    ##  @brief Constructor for PointT
    #   @details Only allows numeric types for x and y. If anything 
    #   else entered, a warning is printed
    #   @param x The x-coordinate of the point
    #   @param y The y-coordinate of the point
    def __init__(self, x, y):
        t1 = type(x)
        t2 = type(y)
        if((t1 == int or  t1 == long or t1 == float) and (t2 == int or t2 == long or t2 == float)):
            self.xc = x
            self.yc = y
        else:
            self.xc = None
            self.yc = None
            print "Invalid type entered."
        

    ##  @brief Getter method for the x-coordinate
    #   @return The x-coordinate of the point
    def xcrd(self):
        return self.xc

    ##  @brief Getter method for the y-coordinate
    #   @return The y-coordinate of the point
    def ycrd(self):
        return self.yc

    ##  @brief Calculates the distance between two points
    #   @param p The other point we want to find the distance from
    #   @return The distance between the two points
    def dist(self, p):
        return math.sqrt((self.xc - p.xcrd())**2 + (self.yc - p.ycrd())**2)

    ##  @brief Rotates the point about the origin
    #   @param angle The angle the point is rotated by in radians
    def rot(self, angle):
        self.xc = (math.cos(angle) - math.sin(angle)) * self.xc
        self.yc= (math.cos(angle) + math.sin(angle)) * self.yc


    