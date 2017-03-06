##  @file testCircles.py
#   @title testCircles
#   @author SusanFayez
#   @date 1/27/2017

##  @brief Importing from files and libraries needed
from Statistics import *
import numpy as np

##  @brief Initiating instances of CircleT and a list of CircleT to use for testing
#   @details Chose variety of numbers to show both negative and positive ints and floats run properly
#   One case of inputting type str to test robustness
testCircleOne = CircleT(1, 5, 20.7)
testCircleTwo = CircleT(0.1, 0.5, 1)
testCircleThree = CircleT(0, -2.658, 3)
testCircleFour = CircleT(-20, -4, 10.2)
testCircleFive = CircleT(-18.28, 0, 1)
circleList = [testCircleOne, testCircleTwo, testCircleThree, testCircleFour, testCircleFive]

##  @brief Function to test getXCoord()
#   @details One simple test case used, already tested for str inputs.
#   Prints whether test passed or failed
def xTest():
    getXTestOne = testCircleOne.xcoord()
    if(getXTestOne == 1):
        print("getXTestOne passed!")
    else:
        print("getXTestOne failed!")

##  @brief Function to test getYCoord()
#   @details One simple test case used, already tested for str inputs
#   Prints whether test passed or failed
def yTest():
    getYTestTwo = testCircleTwo.ycoord()
    if(getYTestTwo == 0.5):
        print("getYTestTwo passed!")
    else:
        print("getYTestTwo failed!")

##  @brief Function to test getRadius()
#   @details One simple test case used, already tested for str inputs
#   Prints whether test passed or failed
def radTest():
    getRadiusTestThree = testCircleThree.radius()
    if(getRadiusTestThree == 3):
        print("getRadiusTestThree passed!")
    else:
        print("getRadiusTestThree failed!")

##  @brief Function to test area()
#   @details One simple test case and a test case of 0 radius used
#   Prints whether test passed or failed
def areaTest():
    areaTestFour = testCircleFour.area()
    if(areaTestFour == (math.pi * 10.2 ** 2)):
        print("areaTestFour passed!")
    else:
        print("areaTestFour failed!")

    areaTestFive = testCircleFive.area()
    if(areaTestFive == (math.pi * 1 ** 2)):
        print("areaTestFive passed!")
    else:
        print("areaTestFive failed!")

##  @brief Function to test circumference()
#   @details One simple test case and a test case of 0 radius used
#   Prints whether test passed or failed
def circTest():
    circumferenceTestOne = testCircleOne.circumference()
    if(circumferenceTestOne == (math.pi * 20.7 * 2)):
        print("circumferenceTestOne passed!")
    else:
        print("circumferenceTestOne failed!")

    circumferenceTestFive= testCircleFive.circumference()
    if(circumferenceTestFive == (math.pi * 1 * 2)):
        print("circumferenceTestFive passed!")
    else:
        print("circumferenceTestFive failed!")

##  @brief Function to test insideBox()
#   @details A test case that should return true, a test case that should return false used
#   Also included a zero radius circle with x and y coordinates inside the box to make sure it returns false
#   Prints whether test passed or failed
def boxTest():
    boxTestTwo = testCircleTwo.insideBox(-2, 2, 6, 6)
    if(boxTestTwo == True):
        print("boxTestTwo passed!")
    else:
        print("boxTestTwo failed!")

    boxTestThree = testCircleThree.insideBox(3, 4, 1, 2)
    if(boxTestThree == False):
        print("boxTestThree passed!")
    else:
        print("boxTestThree failed!")

##  @brief Function to test intersect()
#   @details A test case that should return true, a test case that should return false used
#   Also included a zero radius circle with x and y coordinates inside the other circle to make sure it returns false
#   Prints whether test passed or failed
def intersectTest():
    intersectOneTwoTest = testCircleOne.intersect(testCircleTwo)
    if(intersectOneTwoTest == True):
        print("intersectOneTwoTest passed!")
    else:
        print("intersectOneTwoTest failed!")

    intersectThreeFourTest = testCircleThree.intersect(testCircleFour)
    if(intersectThreeFourTest == False):
        print("intersectOneThreeFourTest passed!")
    else:
        print("intersectThreeFourTest failed!")

##  @brief Function to test scale()
#   @details Test cases scaled with both positive and negative numbers to make sure both yield a positive radius
#   Also included a zero radius circle to make sure scaling still results in a zero radius
#   Prints whether test passed or failed
def scaleTest():
    testCircleOne.scale(10) 
    if(testCircleOne.radius() == 207.0):
        print("scaleTestOne passed!")
    else:
        print("scaleTestOne failed!")

    testCircleTwo.scale(-10)
    if(testCircleTwo.radius() == 10):
        print("scaleTestTwo passed!")
    else:
        print("scaleTestTwo failed!")

    testCircleFive.scale(10)
    if(testCircleFive.radius() == 10):
        print("scaleTestFive passed!")
    else:
        print("scaleTestFive failed!")

##  @brief Function to test tanslate()
#   @details Test cases moved in both positive and negative directions
#   Also included a zero radius circle to make sure it can still be moved
#   Prints whether test passed or failed
def transTest():
    testCircleThree.translate(5, 5.5)
    if(testCircleThree.xcoord() == 5 and testCircleThree.ycoord() == 2.842):
        print("translasteTestThree passed!")
    else:
        print("translateTestThree failed!")

    testCircleFour.translate(-2.7, -16)
    if(testCircleFour.xcoord() == -22.7 and testCircleFour.ycoord() == -20):
        print("translasteTestFour passed!")
    else:
        print("translateTestFour failed!")

    testCircleFive.translate(0, -0.8)
    if(testCircleFive.xcoord() == -18.28 and testCircleFive.ycoord() == -0.8):
        print("translasteTestFive passed!")
    else:
        print("translateTestFive failed!")

##  @brief Function to test average()
#   @details Test case of list of all previous CircleT testers
#   Prints whether test passed or failed
def avgTest():
    averageCL = average(circleList)
    if(averageCL == (207 + 10 + 3 + 10.2 + 10) / 5.0):
        print("averageTest passed!")
    else:
        print("averageTest failed!")

##  @brief Function to test stdDev()
#   @details Test case of list of all previous CircleT testers
#   Prints whether test passed or failed
def stdDevTest():
    stdDevCL = stdDev(circleList)
    radArr = np.array([207, 10, 3, 10.2, 10])
    if(int(stdDevCL) == int(radArr.std())):
        print("stdDevTest passed!")
    else:
        print("stdDevTest failed!")

##  @brief Function to test rank()
#   @details Test case of list of all previous CircleT testers
#   Prints whether test passed or failed
def rankTest():
    rankCL = rank(circleList)
    if(rankCL == [1, 3, 5, 2, 4]):
        print("rankTest passed!")
    else:
        print("rankTest failed!")

##  @brief Running all the test cases
xTest()
yTest()
radTest()
areaTest()
circTest()
boxTest()
intersectTest()
scaleTest()
transTest()
avgTest()
stdDevTest()
rankTest()
