##  @file testCirclesDeque.py
#   @title testCirclesDeque
#   @author Susan Fayez
#   @date 2/18/2017

##  @brief importing from libraries needed
import unittest
from deque import *

##  @brief Class contains test cases for PointT
class PointTests(unittest.TestCase):

    ##  @brief Runs before test cases to initialize points
    def setUp(self):
        p1 = PointT(1, -5)
        p2 = PointT(4.76, -0.663)
        p3 = PointT(24L, 5L)
        p4 = PointT("hello", False)

        self.points = [p1, p2, p3, p4]

    ##  @brief Runs after test cases to remove points
    def tearDown(self):
        self.points = None
        
    ##  @brief Tests xcrd()
    def testXcrd(self):
        self.assertTrue(self.points[0].xcrd() == 1)
        self.assertTrue(self.points[1].xcrd() == 4.76)
        self.assertTrue(self.points[2].xcrd() == 24L)
        self.assertTrue(self.points[3].xcrd() == None)     
        
    ##  @brief Tests ycrd()
    def testYcrd(self):
        self.assertTrue(self.points[0].ycrd() == -5)
        self.assertTrue(self.points[1].ycrd() == -0.663)
        self.assertTrue(self.points[2].ycrd() == 5L)
        self.assertTrue(self.points[3].ycrd() == None)
          
    ##  @brief Tests dist()
    def testDist(self):
        self.assertAlmostEqual(self.points[0].dist(self.points[1]), 5.7399624563232114, None, None, 0.1)
        self.assertAlmostEqual(self.points[0].dist(self.points[2]), 25.079872407968907, None, None, 0.1)
        self.assertAlmostEqual(self.points[1].dist(self.points[2]), 20.056100543226247, None, None, 0.1)
   
    ##  @brief Tests rot()
    #   @details Rotates each point and checks whether the new x and y coordinates
    #   are the expected values
    def testRot(self):
        self.points[0].rot(3 * math.pi)
        self.points[1].rot(0)
        self.points[2].rot(-math.pi / 2.0)

        self.assertAlmostEqual(self.points[0].xcrd(), -1.0000000000000004, None, None, 0.1)
        self.assertTrue(self.points[1].xcrd() == 4.76)
        self.assertTrue(self.points[2].xcrd() == 24.0)
      
##  @brief Class contains tests for LineT
class LineTests(unittest.TestCase):
    
    ##  @brief Runs before test cases to initialize lines
    def setUp(self):
        p1 = PointT(1, -5)
        p2 = PointT(4.76, -0.663)
        p3 = PointT(24L, 5L)
        p4 = PointT(-27.4, 2L)
        p5 = PointT(54, 0.234)
        p6 = PointT(8.223, -8L)

        l1 = LineT(p1, p2)
        l2 = LineT(p3, p4)
        l3 = LineT(p5, p6)
        l4 = LineT("world", complex(8, 1))
        l5 = LineT(p1, p1)

        self.lines = [l1, l2, l3, l4, l5]

    ##  @brief Runs after test cases to remove lines
    def tearDown(self):
        self.lines = None
    
    ##  @brief Tests beg()
    #   @details Compares the x and y coordinates of the beginning point to the
    #   expected values
    def testBeg(self):
        self.assertTrue(self.lines[0].beg().xcrd() == 1 and self.lines[0].beg().ycrd() == -5)
        self.assertTrue(self.lines[1].beg().xcrd() == 24L and self.lines[1].beg().ycrd() == 5L)
        self.assertTrue(self.lines[2].beg().xcrd() == 54 and self.lines[2].beg().ycrd() == 0.234)
        self.assertIsNone(self.lines[3].beg())
       
    ##  @breif Tests end()
    #   @details Comapres the x and y coordinates of the end point to the expected
    #   values
    def testEnd(self):
        self.assertTrue(self.lines[0].end().xcrd() == 4.76 and self.lines[0].end().ycrd() == -0.663)
        self.assertTrue(self.lines[1].end().xcrd() == -27.4 and self.lines[1].end().ycrd() == 2L)
        self.assertTrue(self.lines[2].end().xcrd() == 8.223 and self.lines[2].end().ycrd() == -8L)
        self.assertIsNone(self.lines[3].end())
       
    ##  @brief Tests len()
    def testLen(self):
        self.assertAlmostEqual(self.lines[0].len(), 5.7399624563232114, None, None, 0.1)
        self.assertAlmostEqual(self.lines[1].len(), 51.487474204897644, None, None, 0.1)
        self.assertAlmostEqual(self.lines[2].len(), 46.511638167237244, None, None, 0.1)
        
    ##  @brief Tests mdpt()
    #   @details Compares the x and y coordinates of the midpoint to the expected values
    def testMdpt(self):
        self.assertAlmostEqual(self.lines[0].mdpt().xcrd(), 2.88, None, None, 0.1)
        self.assertAlmostEqual(self.lines[0].mdpt().ycrd(), -2.8315, None, None, 0.1)

        self.assertAlmostEqual(self.lines[1].mdpt().xcrd(), -1.7, None, None, 0.1)
        self.assertAlmostEqual(self.lines[1].mdpt().ycrd(), 3.5, None, None, 0.1)
        
        self.assertAlmostEqual(self.lines[2].mdpt().xcrd(), 31.1115, None, None, 0.1)
        self.assertAlmostEqual(self.lines[2].mdpt().ycrd(), -3.883, None, None, 0.1)

        self.assertTrue(self.lines[4].mdpt().xcrd() == 1)
        self.assertTrue(self.lines[4].mdpt().ycrd() == -5)
        
    ##  @brief Tests rot()
    #   @details Rotates each point then compares the x and y coordinates of the 
    #   beginning and end points to the expected values
    def testRot(self):
        self.lines[0].rot(math.pi / 4)
        self.lines[1].rot(0)
        self.lines[2].rot(-50)

        self.assertAlmostEqual(self.lines[0].beg().xcrd(), 1.11022302463e-16, None, None, 0.1)
        self.assertAlmostEqual(self.lines[0].end().xcrd(), 5.28466159722e-16, None, None, 0.1)
        self.assertAlmostEqual(self.lines[0].beg().ycrd(), -7.07106781187, None, None, 0.1)
        self.assertAlmostEqual(self.lines[0].end().ycrd(), -0.937623591853, None, None, 0.1)

        self.assertTrue(self.lines[1].beg().xcrd() == 24L)
        self.assertTrue(self.lines[1].end().xcrd() == -27.4)
        self.assertTrue(self.lines[1].beg().ycrd() == 5L)
        self.assertTrue(self.lines[1].end().ycrd() == 2L)

        self.assertAlmostEqual(self.lines[2].beg().xcrd(), 37.9399234386, None, None, 0.1)
        self.assertAlmostEqual(self.lines[2].end().xcrd(), 5.77740723028, None, None, 0.1)
        self.assertAlmostEqual(self.lines[2].beg().ycrd(), 0.287197766434, None, None, 0.1)
        self.assertAlmostEqual(self.lines[2].end().ycrd(), -9.81872705757, None, None, 0.1)        
        
##  @brief Class contains tests for CircleT
class CircleTests(unittest.TestCase):
    
    ##  @brief Runs before test cases to initialize circles
    def setUp(self):
        p1 = PointT(0, 0)
        p2 = PointT(0, 10)
        p3 = PointT (-80.662, -45L)
        p4 = PointT (-15.234, 50L)

        c1 = CircleT(p1, 6)
        c2 = CircleT(p1, -9)
        c3 = CircleT(p2, 4)
        c4 = CircleT(p3, 2.726)
        c5 = CircleT(p3, 2L)
        c6 = CircleT(p4, -0.342)
        c7 = CircleT(p1, 0)
        c8 = CircleT("heck", [])

        self.circles = [c1, c2, c3, c4, c5, c6, c7, c8]
    
    ##  @brief Runs after test cases to remove circles
    def tearDown(self):
        self.circles = None
        
    ##  @brief Tests cen()
    #   @details Compares the x and y coordinates of the center point to the expected
    #   values
    def testCen(self):
        self.assertTrue(self.circles[0].cen().xcrd() == 0)
        self.assertTrue(self.circles[0].cen().ycrd() == 0)

        self.assertTrue(self.circles[5].cen().xcrd() == -15.234)
        self.assertTrue(self.circles[5].cen().ycrd() == 50L)

        self.assertIsNone(self.circles[6].cen())

        self.assertIsNone(self.circles[7].cen())
        
    ##  @brief Tests rad()
    def testRad(self):
        self.assertTrue(self.circles[0].rad() == 6)
        self.assertTrue(self.circles[5].rad() == 0.342)
        self.assertIsNone(self.circles[6].rad())
        self.assertIsNone(self.circles[7].rad())
           
    ## @brief Tests area()
    def testArea(self):
        self.assertAlmostEqual(self.circles[1].area(), 254.46900494077323, None, None, 0.1)
        self.assertAlmostEqual(self.circles[2].area(), 50.26548245743669, None, None, 0.1)
        self.assertAlmostEqual(self.circles[4].area(), 12.566370614359172, None, None, 0.1)
        
    ##  @brief Tests intersect()
    def testIntersect(self):
        self.assertTrue(self.circles[0].intersect(self.circles[1]))
        self.assertTrue(self.circles[0].intersect(self.circles[2]))
        self.assertFalse(self.circles[3].intersect(self.circles[5]))
        
    ##  @brief Tests connection()
    #   @details Creates lines for the connections and compares the x and y 
    #   coordinates of the begining and end points to the expected values
    def testConnection(self):
        l1 = self.circles[0].connection(self.circles[1])
        l2 = self.circles[2].connection(self.circles[3])
        l3 = self.circles[4].connection(self.circles[5])

        self.assertTrue(l1.beg().xcrd() == 0)
        self.assertTrue(l1.beg().ycrd() == 0)
        self.assertTrue(l1.end().xcrd() == 0)
        self.assertTrue(l1.end().ycrd() == 0)

        self.assertTrue(l2.beg().xcrd() == 0)
        self.assertTrue(l2.beg().ycrd() == 10)
        self.assertTrue(l2.end().xcrd() == -80.662)
        self.assertTrue(l2.end().ycrd() == -45L)

        self.assertTrue(l3.beg().xcrd() == -80.662)
        self.assertTrue(l3.beg().ycrd() == -45L)
        self.assertTrue(l3.end().xcrd() == -15.234)
        self.assertTrue(l3.end().ycrd() == 50L)
        
    ##  @brief Tests force()
    #   @details Creates the lambda function and passes it to force for tests
    def testForce(self):
        f = lambda r: (6.672e-11) / (r ** 2)
        
        self.assertAlmostEqual(self.circles[2].force(f)(self.circles[1]), 8.5341600731e-09, None, None, 0.1)
        self.assertAlmostEqual(self.circles[0].force(f)(self.circles[3]), 2.06486568875e-11, None, None, 0.1)
        self.assertAlmostEqual(self.circles[4].force(f)(self.circles[5]), 2.31540111708e-14, None, None, 0.1)

##  @brief Class contains tests for Deq     
class DequeTests(unittest.TestCase):
    
    ##  @brief Runs before the test cases to initialize deque
    def setUp(self):
        p1 = PointT(0, 0)
        p2 = PointT(0, 10)
        p3 = PointT (-80.662, -45L)
        p4 = PointT (-15.234, 50L)

        c1 = CircleT(p1, 6)
        c2 = CircleT(p1, -9)
        c3 = CircleT(p2, 4)
        c4 = CircleT(p3, 2.726)
        c5 = CircleT(p3, 2L)
        c6 = CircleT(p4, -0.342)

        self.circles = [c1, c2, c3, c4, c5, c6]

        Deq.init()

    ##  @brief Runs after test cases to remove deque
    def tearDown(self):
        self.circles = None
        Deq.s = None
        
    ##  @brief Tests pushBack()
    #   @details Pushes circles onto the deque. Creates an array for the expected
    #   result and compares the deque to it
    def testDeq_pushBack(self):
        for i in range(6):
            Deq.pushBack(self.circles[0])
            Deq.pushBack(self.circles[2])
            Deq.pushBack(self.circles[4])

        Deq.pushBack(self.circles[5])
        Deq.pushBack(self.circles[5])

        a = []

        for i in range(6):
            a.append(self.circles[0])
            a.append(self.circles[2])
            a.append(self.circles[4])

        a.append(self.circles[5])
        a.append(self.circles[5])

        self.assertTrue(Deq.s == a)
        with self.assertRaises(Full):
            Deq.pushBack(self.circles[3])
        
    ##  @brief Tests pushFront()
    #   @details Pushes circles onto the deque. Creates an array for the expected
    #   result and compares the deque to it
    def testDeq_pushFront(self):
        for i in range(6):
            Deq.pushFront(self.circles[1])
            Deq.pushFront(self.circles[3])
            Deq.pushFront(self.circles[5])
            
        Deq.pushFront(self.circles[0])
        Deq.pushFront(self.circles[0])

        a = []

        for i in range(6):
            a.insert(0, self.circles[1])
            a.insert(0, self.circles[3])
            a.insert(0, self.circles[5])

        a.insert(0, self.circles[0])
        a.insert(0, self.circles[0])

        self.assertTrue(Deq.s == a)
        with self.assertRaises(Full):
            Deq.pushFront(self.circles[4])
    
    ##  @brief Tests popBack()
    #   @details Pushes circles onto the deque. Pops from the back once and creates 
    #   an array for the expected result and compares the deque to it
    def testDeq_popBack(self):
        for i in range(6):
            Deq.pushBack(self.circles[0])
            Deq.pushBack(self.circles[2])
            Deq.pushBack(self.circles[4])

        Deq.popBack()

        a = []

        for i in range(6):
            a.append(self.circles[0])
            a.append(self.circles[2])
            a.append(self.circles[4])

        del a[len(a) - 1]

        self.assertTrue(Deq.s == a)
       
    ##  @brief Tests popFront()
    #   @details Pushes circles onto the deque. Pops from the front once and creates 
    #   an array for the expected result and compares the deque to it
    def testDeq_popFront(self):
        for i in range(6):
            Deq.pushFront(self.circles[1])
            Deq.pushFront(self.circles[3])
            Deq.pushFront(self.circles[5])

        Deq.popFront()

        a = []

        for i in range(6):
            a.insert(0, self.circles[1])
            a.insert(0, self.circles[3])
            a.insert(0, self.circles[5])

        del a[0]

        self.assertTrue(Deq.s == a)
        
    ##  @brief Tests back()
    #   @details Pushes circles onto the deque. Creates an array for the 
    #   expected result and compares the back values
    def testDeq_back(self):
        for i in range(6):
            Deq.pushBack(self.circles[0])
            Deq.pushBack(self.circles[2])
            Deq.pushBack(self.circles[4])

        a = []

        for i in range(6):
            a.append(self.circles[0])
            a.append(self.circles[2])
            a.append(self.circles[4])

        self.assertTrue(Deq.back() == a[len(a)-1])
        
    ##  @brief Tests front()
    #   @details Pushes circles onto the deque. Creates an array for the 
    #   expected result and compares the front values
    def testDeq_front(self):
        for i in range(6):
            Deq.pushFront(self.circles[1])
            Deq.pushFront(self.circles[3])
            Deq.pushFront(self.circles[5])

        a = []

        for i in range(6):
            a.insert(0, self.circles[1])
            a.insert(0, self.circles[3])
            a.insert(0, self.circles[5])

        self.assertTrue(Deq.front() == a[0])
       
    ##  @brief Tests back()
    #   @details Pushes circles onto the deque. Creates an array for the expected 
    #   result and compares the sizes
    def testDeq_size(self):
        for i in range(6):
            Deq.pushFront(self.circles[1])
            Deq.pushBack(self.circles[5])
            Deq.pushFront(self.circles[2])

        a = []

        for i in range(6):
            a.insert(0, self.circles[1])
            a.append(self.circles[5])
            a.insert(0, self.circles[2])

        self.assertTrue(Deq.size() == len(a))
      
    ##  @brief Tests disjoint()
    #   @details Pushes circles that don't intersec onto the deque. Checks disjoint()
    #   returns True. Pops all circles off the deque. Pushes circles that do intersect
    #   onto the deque. Checks that disjoint() returns True. Pops all but one circle.
    #   Checks that disjoint() returns True. Pops the last circle and checks that calling
    #   disjoint() raises an error
    def testDeq_disjoint(self):
        Deq.pushFront(self.circles[0])
        Deq.pushBack(self.circles[3])
        Deq.pushFront(self.circles[5])

        self.assertTrue(Deq.disjoint())

        Deq.popBack()
        Deq.popBack()
        Deq.popBack()

        Deq.pushFront(self.circles[0])
        Deq.pushBack(self.circles[1])
        Deq.pushFront(self.circles[1])

        self.assertFalse(Deq.disjoint())

        Deq.popFront()
        Deq.popFront()

        self.assertTrue(Deq.disjoint())

        Deq.popFront()

        with self.assertRaises(Empty):
            Deq.disjoint()

    ##  @brief Tests sumFx()
    #   @details Defines the lambda function for force() and pushes circles onto the
    #   deque. Creates an array of expected values and computes the sum of the forces
    #   in the x direction. Compares result to sumFx()
    def testDeq_sumFx(self):
        f = lambda r: (6.672e-11) / (r ** 2)

        
        Deq.pushFront(self.circles[0])
        Deq.pushFront(self.circles[2])
        Deq.pushFront(self.circles[3])
        Deq.pushFront(self.circles[5])

        a = []

        a.insert(0, self.circles[0])
        a.insert(0, self.circles[2])
        a.insert(0, self.circles[3])
        a.insert(0, self.circles[5])

        sfx = 0
        Deq.sumFx(f)
        
        for i in range(len(a)):
            if (i != 0):
                sfx += a[i].force(f)(a[0]) * ((a[i].cen().xcrd() - a[0].cen().xcrd()) / a[i].connection(a[0]).len())
        self.assertTrue(sfx == Deq.sumFx(f))
        
##  @brief Runs the test cases
if __name__ == '__main__':
    unittest.main()