##  @file deque.py
#   @title DequeCircleModule
#   @author Susan Fayez
#   @date 2/15/2017

##  @brief importing from libraries needed
from circleADT import *

##  @brief A class for a deque abstract object
#   @details This class represents a deque by storing it in a list s
class Deq:

    ##  @brief declaring constants and state variables
    MAX_SIZE = 20

    s = []

    ##  @brief Constructor for the deque 
    #   @details Initializes the deque before any other access program is called 
    @staticmethod
    def init():
        Deq.s = []
        
    ##  @brief Adds an element to the back of the deque
    #   @details raises an error if user attempts to push an element onto the 
    #   deque when it is full
    @staticmethod
    def pushBack(c):
        if (len(Deq.s) >= Deq.MAX_SIZE):
            raise Full("Maxium size exceeded")
        
        Deq.s.append(c)
        
    ##  @brief Adds an element to the front of the deque
    #   @details raises an error if user attempts to push an element onto the 
    #   deque when it is full
    @staticmethod
    def pushFront(c):
        if (len(Deq.s) >= Deq.MAX_SIZE):
            raise Full("Maxium size exceeded")
        
        Deq.s.insert(0, c)
        
    ##  @brief Deletes an element from the back of the deque
    #   @details raises an error if user attempts to pop an element from the 
    #   deque when it is empty
    @staticmethod
    def popBack():
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")
        
        del Deq.s[len(Deq.s) - 1]
        
    ##  @brief Deletes an element from the front of the deque
    #   @details raises an error if user attempts to pop an element from the 
    #   deque when it is empty
    @staticmethod
    def popFront():
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")
        
        del Deq.s[0]
        
    ##  @brief Retrieves an element from the back of the deque
    #   @details raises an error if user attempts to retrieve an element from the 
    #   deque when it is empty
    @staticmethod
    def back():
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")
        
        return Deq.s[len(Deq.s) - 1]

    ##  @brief Retrieves an element from the front of the deque
    #   @details raises an error if user attempts to retrieve an element from the 
    #   deque when it is empty
    @staticmethod
    def front():
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")
        
        return Deq.s[0]
    
    ##  @brief Retrieves the size of the deque
    @staticmethod
    def size():
        return len(Deq.s)
        
    ##  @brief Determines whether or not the circles in the dueque intersect
    #   @details Raises an error if user attempts to call this access program
    #   when the deque is empty. If not, compares each element in the deque to one
    #   another. Returns false if any elements intersect one another. Returns true 
    #   if no circles in the set intersect.
    @staticmethod
    def disjoint():
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")

        for i in range(len(Deq.s)):
            for j in range(len(Deq.s)):
                if (Deq.s[i].intersect(Deq.s[j]) and i != j):
                    return False
        return True

    ##  @brief Calculates the sum of the gravitational forces between the circles in 
    #   the deque and the first circle in the x direction
    #   @details Raises an error if user attempts to call this access program
    #   when the deque is empty. If not, implements __Fx() to calculate the sum of the
    #   gravitational forces in the x direction
    @staticmethod
    def sumFx(f):
        if(len(Deq.s) == 0):
            raise Empty("No elements in the deque")

        ##  @brief Local function returns the x-component of a force between two circles
        #   @param F The force between the two circles
        #   @param ci The first circle, type CircleT
        #   @param cj The second circle, type CircleT
        def xcomp(F, ci, cj):
            return F * ((ci.cen().xcrd() - cj.cen().xcrd()) / ci.connection(cj).len())

        ##  @brief Local function returns the x-component of a force between two circles
        #   @details Implements __xcomp to find the x component of the force by calling 
        #   the force method from circleADT.py for the force and entering the circles
        #   as the other two parameters
        #   @param f The lambda function needed by force() to calculate the gravitational
        #   force
        #   @param ci The first circle 
        #   @param cj The second circle
        def Fx(f, ci, cj):
            return xcomp(ci.force(f)(cj), ci, cj)
        
        sum = 0;
        for i in range(len(Deq.s)):
            if (i != 0):
                sum += Fx(f, Deq.s[i], Deq.s[0])
        return sum

##  @brief Class defines the deque full exception
class Full(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

##  @brief Class defines the deque empty exception
class Empty(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
