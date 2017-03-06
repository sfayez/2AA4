##  @file Statistics.py
#   @title Statistics
#   @author Susan Fayez
#   @date 1/27/2017

##  @brief importing from files and libraries needed
from numpy import *
import math
from CircleADT import *
import numpy as np

##  @brief Calculates the average of the radii for a list of circles
#   @details Function accepts a list of circles and uses numpy to the calculate the average of the radii
#   @param circleList A list of instances of CircleT
#   @return The numeric value of the average of the radii
def average(circleList):
    radArray = arange(len(circleList))
    for i in range(len(circleList)):
        radArray[i] = circleList[i].getRadius()
    average = radArray.mean()
    return average

##  @brief Calculates the standard deviation of the radii for a list of circles
#   @details Function accepts a list of circles and uses numpy to the calculate the standard deviation of the radii
#   @param circleList A list of instances of CircleT
#   @return The numeric value of the standard deviation of the radii
def stdDev(circleList):
    radArray = arange(len(circleList))
    for i in range(len(circleList)):
        radArray[i] = circleList[i].getRadius()
    stdDev = radArray.std()
    return stdDev
    
##  @brief Ranks the radii of the circles based on size
#   @details Function accpets a list of circles and returns a list with each number corresponding to the rank of the radius of each circle in their original order.
#   @param circleList A list of instances of CircleT
#   @return A list of each circle's rank
def rank(circleList):
    radArray = []
    for i in range(len(circleList)):
        radArray.append(circleList[i].getRadius())
    compare = sorted(radArray)
    compare.reverse()
    rank = []
    for i in range (len(radArray)):
        for j in range (len(compare)):
            if (radArray[i] == compare[j]):
                rank.append(j + 1)
    return rank
    
    
