##  @file CircleADT.py
#   @title CircleADT
#   @author Susan Fayez
#   @date 1/27/2017

##  @brief importing from libraries needed
import math

##  @brief A class for a circle ADT
#   @details This class represents a circle with x and y coordinates as well as a radius   
class CircleT():

    ##  @brief Constructor for CircleT
    #   @details Constructor accepts three parameters for the x-coordinate, the y-coordinate, and the radius.
    #   If any of the parameters entered are strings, an error message is printed and no circle is initiated.
    #   If the radius entered is negative, a warning is printed and the absolute value of the input is taken. If the radius is 0, a warning is printed.
    #   @param x The x-coordinate
    #   @param y The y-coordinate
    #   @param r The radius
    def __init__(self, x, y, r):
        if (type(x) == str or type(y) == str or type(r) == str):
            print("Invalid input. No circle initiated.")
        else:
            self.x = x
            self.y = y
            self.r = abs(r)
            if(r < 0):
                print("Radius can't be negative. Absolute value of input taken.")
            if(r == 0):
                print("WARNING: Setting radius to 0 means the circle does not exist.")
            
    ##  @brief Returns the x-coordinateor the circle.
    #   @return Numeric value of the x-coordinate.
    def getXCoord(self):
        return self.x

    ##  @brief Returns the y-coordinate of the circle.
    #   @return Numeric value of the y-coordinate.
    def getYCoord(self):
        return self.y

    ##  @brief Returns the radius of the circle.
    #   @return Numeric value of the radius.
    def getRadius(self):
        return self.r

    ##  @brief Calculates the area of the circle.
    #   @return The area of the circle
    def area(self):
        return math.pi * (self.r ** 2)
    
    ##  @brief Calculates the circumference of the circle.
    #   @return The circumference of the circle
    def circumference(self):
        return 2 * math.pi * self.r
    
    ##  @brief Determines whether or not circle is in specified box
    #   @details Function accepts x and y coordinates of top left corner of a box as well as width and height of the box
    #   and determines whether or not it contains the circle
    #   @param x0 The x-coordinate of the top left corner of the box
    #   @param y0 The y-coordinate of the top left corner of the box
    #   @param w The width of the box
    #   @param h the height of the box
    #   @return a boolean value on whether the circle is in the box
    def insideBox(self, x0, y0, w, h):
        if (self.r == 0):
            return False
        if (self.x - self.r) >= x0 and (self.y + self.r) <= y0 and (self.x + self.r) <= (x0 + w) and (self.y - self.r) >= (y0 - h):
            return True
        else:
            return False

    ##  @brief Determines whether or not the circle intersects with a given circle
    #   @details Function accepts an instance of CircleT and determines whether or not the circles intersect
    #   @param circleTwo An instance of CircleT
    #   @return a boolean value on whether or not the circles intersect
    def intersect(self, circleTwo):
        if (self.r == 0 or circleTwo.getRadius() == 0):
            return False
        if math.sqrt((circleTwo.getXCoord() - self.x)**2 + (circleTwo.getYCoord()-self.y)**2) <= (self.r + circleTwo.getRadius()):
            return True
        else:
            return False

    ##  @brief Scales the radius of the circle
    #   @details Function accepts some value k and multiplies the radius by it
    #   @param k The factor by which we scale the radius of the circle
    def scale(self, k):
        if(k < 0):
            print("Cannot scale by negative number. Scaled by absolute value.")
        self.r = self.r * abs(k)

    ##  @brief Moves the circle
    #   @details Function accepts numbers dx and dy and moves the circle by dx in the x direction and dy in the y direction
    #   @param dx The amount to move in the x direction
    #   @param dy The amount to move in the y direction
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

