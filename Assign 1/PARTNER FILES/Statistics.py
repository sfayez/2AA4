## @file Statistics.py
#  @title Statistics
#  @author Jenny Feng Chen
#  @date 1/27/2017

import numpy as np
from CircleADT import*

## @brief This function calculates the average radius.
#  @details This function takes a list of instances of CircleT and calculates
#  the average radius of all of the circles in the list using numpy.
#  @param listOfCircle is a list of instances of CircleT.
#  @return the average of the radii
def average(listOfCircle):
    listR = []
    for i in listOfCircle:
        listR.append(i.radius())
    return np.average(np.array(listR))

## @brief This fucntion determines the standard deviation of the radii.
#  @details This function takes a list of instances of CircleT and determines
#  the standard deviation of the radii of all of the circles in the list using numpy.
#  @param listOfCircle is a list of instances of CircleT.
#  @return the standard deviation of the radii
def stdDev(listOfCircle):
    listR = []
    for i in range(len(listOfCircle)):
        listR.append(listOfCircle[i].radius())
    return np.std(np.array(listR))

## @brief This function returns a listed ranked by radius.
#  @details This function takes a list of instances of CircleT and return a listed ranked by radius
#  where a ranking list provides for each element in the list the position
#  it would hold if the list were sorted in descending order of radius.
#  This function is not using numpy.
#  Assuming that same value of radii will be ranked according to the order in the input list.
#  @param listOfCircle is a list of instances of CircleT.
#  @return the ranked list by the radii
def rank(listOfCircle):
    #exmaple:
    #listR = [7.0,6.0,9.0,6.0]
    #x = [9.0,7.0,6.0,6.0]
    #rankList = [2,3,1,4]
    listR = []
    for i in listOfCircle:
        listR.append(i.radius())
    x = sorted(listR, reverse = True)
    rankList = [0] * len(x)
    for i in range(len(x)):
        rankList[listR.index(x[i])] = i + 1
        listR[listR.index(x[i])] = -1
        x[i]=-1
    return rankList
    

