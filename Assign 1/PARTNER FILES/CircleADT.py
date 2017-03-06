## @file CircleADT.py
#  @title CircleADT
#  @author Jenny Feng Chen
#  @date 1/27/2017

import math

## @brief This class represents a circle
#  @details This class represents a circle as (x,y,r) which (x,y) is the
#  coordinate of the center of the circle and r as the radius.
class CircleT(object):

    ## @brief Constructor for CircleT
    #  @details Constructor accepts three parameters for the x and y coordinate and radius
    #  where the radius is greater than 0. Assuming that the user will enter r > 0
    #  @param x is a real number for the x-coordinate.
    #  @param y is a real number for the y-coordinate.
    #  @param r is a real number for the radius.
    def __init__(self,x,y,r):
        if (r > 0):
            self.x = float(x)
            self.y = float(y)
            self.r = float(r)
        else:
            print "Radius should be greater than 0"

    ## @brief Returns the x-coordinate of the center of the circle.
    #  @return the x-coordinate of the center of the circle.
    def xcoord(self):
        return self.x

    ## @brief Returns the y-coordinate of the center of the circle.
    #  @return the y-coordinate of the center of the circle.
    def ycoord(self):
        return self.y

    ## @brief Returns the radius of the circle.
    #  @return the radius of the circle.
    def radius(self):
        return self.r

    ## @brief Returns the area of the circle.
    #  @return the area of the circle.
    def area(self):
        return pow(self.r,2)* math.pi

    ## @brief Returns the circumference of the circle.
    #  @return the circumference of the circle.
    def circumference(self):
        return 2*math.pi*self.r

    ## @brief This method determines whether the circle is inside a box
    #  @details This method takes the x coordinate of the left side of a box,
    #  the y coordinate of the top of the box, the width of the box and
    #  the height of the box.
    #  Assuming that a circle inside the box which any side of the box
    #  is tangent to the circle is also considered as inside the box
    #  @param x0 is a real number of the x coordinate of the left side of the box.
    #  @param y0 is a real number of the y coordinate of the top of the box.
    #  @param w is a real number for the width of the box.
    #  @param h is a real number for the height of the box.
    #  @return True or False by determine whether the circle is inside the box.
    def insideBox(self,x0,y0,w,h):
        x0 = float(x0)
        y0 = float(y0)
        w = float(w)
        h = float(h)
        if self.y+self.r > y0:
            return False
        if self.y-self.r < y0-h:
            return False
        if self.x+self.r > x0+w:
            return False
        if self.x-self.r < x0:
            return False
        return True

    ## @brief This method determines whether two circles intersect.
    #  @details This method takes a second instance of CircleT c as input
    #  and returns true if the circles intersect and otherwise false.
    #  Assuming that one circle tangent to another circle is also an intersection
    #  @param c is an instance of CircleT object.
    #  @return True or False by determine whether two circles intersect.
    def intersect(self,c):
        intersect = (self.x-c.x)**2 + (self.y-c.y)**2 <= (self.r + c.r)**2
        return intersect
    
    ## @brief This method sets a new radius of the circle.
    #  @details This method sets a new radius of the circle. Assuming that input k can only be positive real number
    #  @param k is a positive real number for the new radius of the circle.
    def scale(self,k):
        self.r = self.r * float(abs(k))

    ## @brief This method translate the center of the circle.
    #  @param dx is a real number for the translation of x-coordinate of the center of the circle.
    #  @param dy is a real number for the translation of y-coordinate of the center of the circle.
    def translate(self,dx,dy):
        self.x = self.x + float(dx)
        self.y = self.y + float(dy)

## @brief Example of class usage
if __name__== '__main__':
    circle = CircleT(-2,3,5)
    print circle.xcoord()
