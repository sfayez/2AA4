##  @file circleADT.py
#   @title circleADT
#   @author Susan Fayez
#   @date 2/14/2017

##  @brief importing from libraries needed
from lineADT import *

##  @brief A class for a circle ADT
#   @details This class represents a circle with a point for the center and 
#   a number for the radius
class CircleT():
    
    ##  @brief Constructor for CircleT
    #   @details Constructor accepts a point for the centre of the circle and 
    #   a number for the radius. Throws an exception if zero is entered, takes the
    #   absolute value of the radius and prints a warning if a negative radius is 
    #   entered.
    #   @param cin The center of the radius of type PointT
    #   @param rin The numeric value of the radius
    def __init__(self, cin, rin):
        t = type(rin)
        if(rin == 0):
            print "Radius cannot be zero."
            self.c = None
            self.r = None
        if(isinstance(cin, PointT) and (t == int or t == long or t == float) and rin != 0):
            self.c = cin
            self.r = abs(rin)
            if(rin < 0):
                print("Radius can't be negative. Absolute value of input taken.")
        else:
            print "Invalid type entered."
            self.c = None
            self.r = None
    
    ##  @brief Private method that returns a lambda function that calculates the 
    #   gravitational constant divided by the input squared
    #   @details Not implemented in this class, but here to show what the lambda
    #   function for force should look like
    def __f(self):
        return lambda r: (6.672e-11) / (r ** 2)
    
    ##  @brief Getter method for the center point of the circle 
    #   @return The center point of the circle, type PointT
    def cen(self):
        return self.c

    ##  @brief Getter method for the radius of the circle 
    #   @return The radius of the circle
    def rad(self):
        return self.r

    ##  @brief Calculates the area of the circle.
    #   @return The area of the circle
    def area(self):
        return math.pi * self.r ** 2
    
    ##  @brief Determines whether or not the circle intersects with a given circle
    #   @details Function accepts an instance of CircleT and determines whether 
    #   or not the circles intersect by checking if the distance between the centers
    #   of the circles is greater than the sum of the radii.
    #   @param circleTwo An instance of CircleT
    #   @return a boolean value on whether or not the circles intersect
    def intersect(self, ci):
        
        ##  @brief Checks whether a given point is inside a given circle 
        #   @details Uses dist() from pointADT.py to check whether the distance from the
        #   given point to the center of the given circle is less than the radius of the
        #   circle. If it is, the method returns True, if not it returns False. Not 
        #   implemented in this class, but can be used to check intersection of circles
        #   @param p instance of PointT
        #   @param c instance of CircleT
        #   @return Boolean depending on whether the point is in the circle
        def insideCircle(p, c):
            if (p.dist(c.cen()) <= c.rad()):
                return True
            else:
                return False
        if (self.c.dist(ci.cen()) <= (self.r + ci.rad())):
            return True
        else:
            return False

    ##  @brief Creates a line connecting the centers of the circle and an input circle 
    #   @return A line connnecting the centers of the circles, type LineT
    def connection(self, ci):
        return LineT(self.c, ci.cen())

    ##  @brief Calculates the force of gravity between two circles
    #   @details Accepts a lambda function and multiplies the result of 
    #   entering the distance between the two circles in the lambda function 
    #   by the areas of the circles .
    #   @param f lambda function that calculates the gravitational constant divided 
    #   by the input squared
    #   @return The force of gravity between the two circles
    def force(self, f):
        return lambda x: self.area() * x.area() * f(self.connection(x).len())
        
