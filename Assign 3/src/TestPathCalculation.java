import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

/**
 * Class that tests all of the functions in PathCalculation.
 * 
 * @author Susan Fayez
 *001404420
 */
public class TestPathCalculation {
	// safe zone global variables
	PointT szp;
	RegionT sz;
	SafeZone szl;

	// destinations global variables
	PointT dp1;
	PointT dp2;
	PointT dp3;
	PointT dp4;
	RegionT d1;
	RegionT d2;
	RegionT d3;
	RegionT d4;
	Destinations dl;

	// obstacles global variables
	PointT op1;
	PointT op2;
	PointT op3;
	PointT op4;
	PointT op5;
	PointT op6;
	RegionT o1;
	RegionT o2;
	RegionT o3;
	RegionT o4;
	RegionT o5;
	RegionT o6;
	Obstacles ol;

	// valid path
	PointT p1_1;
	PointT p1_2;
	PointT p1_3;
	PointT p1_4;
	PointT p1_5;
	PointT p1_6;
	PointT p1_7;
	PointT p1_8;
	PointT p1_9;
	PointT p1_10;
	PointT p1_11;
	PointT p1_12;
	PathT p1;

	// global variables for path that avoids obstacles and reaches safe zone but
	// doesn't visit all destinations
	PointT p2_1;
	PointT p2_2;
	PointT p2_3;
	PointT p2_4;
	PointT p2_5;
	PointT p2_6;
	PointT p2_7;
	PointT p2_8;
	PointT p2_9;
	PointT p2_10;
	PathT p2;

	// global variables for path that visits all destinations and reaches safe
	// zone but goes through obstacles
	PointT p3_1;
	PointT p3_2;
	PointT p3_3;
	PointT p3_4;
	PointT p3_5;
	PointT p3_6;
	PointT p3_7;
	PathT p3;

	// global variables for path that avoids obstacles and visits all
	// desinations but doesn't reach safe zone
	PointT p4_1;
	PointT p4_2;
	PointT p4_3;
	PointT p4_4;
	PointT p4_5;
	PointT p4_6;
	PointT p4_7;
	PointT p4_8;
	PointT p4_9;
	PointT p4_10;
	PathT p4;

	// global variables for path that avoids obstacles and reaches safe zone but
	// doesn't visit any destinations
	PointT p5_1;
	PointT p5_2;
	PointT p5_3;
	PointT p5_4;
	PointT p5_5;
	PointT p5_6;
	PointT p5_7;
	PointT p5_8;
	PointT p5_9;
	PathT p5;

	// global variables for straight line path
	PointT p6_1;
	PointT p6_2;
	PointT p6_3;
	PointT p6_4;
	PathT p6;

	// global variables for zero length path
	PointT p7_1;
	PathT p7;

	/**
	 * Runs before test cases. Sets up the map and paths.
	 * 
	 * @throws Exception  if invalid parameters are entered into the constructors.
	 */
	@Before
	public void setup() throws Exception {
		szl = new SafeZone();
		szp = new PointT(10, 15);
		sz = new RegionT(szp, 20, 15);
		szl.add(0, sz);

		dl = new Destinations();
		dp1 = new PointT(145, 20);
		d1 = new RegionT(dp1, 10, 10);
		dl.add(0, d1);

		dp2 = new PointT(55, 75);
		d2 = new RegionT(dp2, 10, 10);
		dl.add(1, d2);

		dp3 = new PointT(30, 125);
		d3 = new RegionT(dp3, 10, 10);
		dl.add(2, d3);

		dp4 = new PointT(125, 125);
		d4 = new RegionT(dp4, 10, 10);
		dl.add(3, d4);

		ol = new Obstacles();
		op1 = new PointT(40, 40);
		o1 = new RegionT(op1, 20, 10);
		ol.add(0, o1);

		op2 = new PointT(15, 70);
		o2 = new RegionT(op2, 20, 40);
		ol.add(1, o2);

		op3 = new PointT(10, 150);
		o3 = new RegionT(op3, 30, 5);
		ol.add(2, o3);

		op4 = new PointT(65, 120);
		o4 = new RegionT(op4, 30, 15);
		ol.add(3, o4);

		op5 = new PointT(90, 45);
		o5 = new RegionT(op5, 35, 45);
		ol.add(4, o5);

		op6 = new PointT(155, 70);
		o6 = new RegionT(op6, 10, 80);
		ol.add(0, o6);

		Map.init(ol, dl, szl);

		p1 = new PathT();
		p1_1 = new PointT(30, 25);
		p1_2 = new PointT(150, 25);
		p1_3 = new PointT(150, 135);
		p1_4 = new PointT(110, 135);
		p1_5 = new PointT(110, 150);
		p1_6 = new PointT(55, 150);
		p1_7 = new PointT(40, 125);
		p1_8 = new PointT(40, 90);
		p1_9 = new PointT(55, 80);
		p1_10 = new PointT(40, 65);
		p1_11 = new PointT(25, 65);
		p1_12 = new PointT(25, 30);

		p1.add(0, p1_1);
		p1.add(1, p1_2);
		p1.add(2, p1_3);
		p1.add(3, p1_4);
		p1.add(4, p1_5);
		p1.add(5, p1_6);
		p1.add(6, p1_7);
		p1.add(7, p1_8);
		p1.add(8, p1_9);
		p1.add(9, p1_10);
		p1.add(10, p1_11);
		p1.add(11, p1_12);

		p2 = new PathT();
		p2_1 = new PointT(30, 15);
		p2_2 = new PointT(145, 15);
		p2_3 = new PointT(145, 40);
		p2_4 = new PointT(80, 40);
		p2_5 = new PointT(60, 70);
		p2_6 = new PointT(60, 105);
		p2_7 = new PointT(50, 105);
		p2_8 = new PointT(50, 130);
		p2_9 = new PointT(10, 130);
		p2_10 = new PointT(10, 30);

		p2.add(0, p2_1);
		p2.add(1, p2_2);
		p2.add(2, p2_3);
		p2.add(3, p2_4);
		p2.add(4, p2_5);
		p2.add(5, p2_6);
		p2.add(6, p2_7);
		p2.add(7, p2_8);
		p2.add(8, p2_9);
		p2.add(9, p2_10);

		p3 = new PathT();
		p3_1 = new PointT(30, 20);
		p3_2 = new PointT(165, 20);
		p3_3 = new PointT(165, 130);
		p3_4 = new PointT(35, 130);
		p3_5 = new PointT(35, 85);
		p3_6 = new PointT(55, 85);
		p3_7 = new PointT(30, 30);

		p3.add(0, p3_1);
		p3.add(1, p3_2);
		p3.add(2, p3_3);
		p3.add(3, p3_4);
		p3.add(4, p3_5);
		p3.add(5, p3_6);
		p3.add(6, p3_7);

		p4 = new PathT();
		p4_1 = new PointT(25, 15);
		p4_2 = new PointT(25, 10);
		p4_3 = new PointT(145, 10);
		p4_4 = new PointT(160, 30);
		p4_5 = new PointT(160, 50);
		p4_6 = new PointT(135, 50);
		p4_7 = new PointT(135, 115);
		p4_8 = new PointT(130, 125);
		p4_9 = new PointT(65, 85);
		p4_10 = new PointT(35, 125);

		p4.add(0, p4_1);
		p4.add(1, p4_2);
		p4.add(2, p4_3);
		p4.add(3, p4_4);
		p4.add(4, p4_5);
		p4.add(5, p4_6);
		p4.add(6, p4_7);
		p4.add(7, p4_8);
		p4.add(8, p4_9);
		p4.add(9, p4_10);

		p5 = new PathT();
		p5_1 = new PointT(30, 30);
		p5_2 = new PointT(75, 30);
		p5_3 = new PointT(75, 115);
		p5_4 = new PointT(55, 115);
		p5_5 = new PointT(55, 155);
		p5_6 = new PointT(175, 155);
		p5_7 = new PointT(175, 5);
		p5_8 = new PointT(20, 5);
		p5_9 = new PointT(20, 15);

		p5.add(0, p5_1);
		p5.add(1, p5_2);
		p5.add(2, p5_3);
		p5.add(3, p5_4);
		p5.add(4, p5_5);
		p5.add(5, p5_6);
		p5.add(6, p5_7);
		p5.add(7, p5_8);
		p5.add(8, p5_9);

		p6 = new PathT();
		p6_1 = new PointT(10, 5);
		p6_2 = new PointT(10, 10);
		p6_3 = new PointT(10, 30);
		p6_4 = new PointT(10, 45);

		p6.add(0, p6_1);
		p6.add(1, p6_2);
		p6.add(2, p6_3);
		p6.add(3, p6_4);

		p7 = new PathT();
		p7_1 = new PointT(30, 15);

		p7.add(0, p7_1);
		p7.add(1, p7_1);
		p7.add(2, p7_1);
		p7.add(3, p7_1);
		p7.add(4, p7_1);

	}

	/**
	 * Emptys all the variables after test cases run.
	 */
	@After
	public void tearDown() {

		szp = null;
		sz = null;
		szl = null;
		
		dp1 = null;
		dp2 = null;
		dp3 = null;
		dp4 = null;
		d1 = null;
		d2 = null;
		d3 = null;
		d4 = null;
		dl = null;
		
		op1 = null;
		op2 = null;
		op3 = null;
		op4 = null;
		op5 = null;
		op6 = null;
		o1 = null;
		o2 = null;
		o3 = null;
		o4 = null;
		o5 = null;
		o6 = null;
		ol = null;
		
		p1_1 = null;
		p1_2 = null;
		p1_3 = null;
		p1_4 = null;
		p1_5 = null;
		p1_6 = null;
		p1_7 = null;
		p1_8 = null;
		p1_9 = null;
		p1_10 = null;
		p1_11 = null;
		p1_12 = null;
		p1 = null;
		
		p2_1 = null;
		p2_2 = null;
		p2_3 = null;
		p2_4 = null;
		p2_5 = null;
		p2_6 = null;
		p2_7 = null;
		p2_8 = null;
		p2_9 = null;
		p2_10 = null;
		p2 = null;
		
		p3_1 = null;
		p3_2 = null;
		p3_3 = null;
		p3_4 = null;
		p3_5 = null;
		p3_6 = null;
		p3_7 = null;
		p3 = null;
		
		p4_1 = null;
		p4_2 = null;
		p4_3 = null;
		p4_4 = null;
		p4_5 = null;
		p4_6 = null;
		p4_7 = null;
		p4_8 = null;
		p4_9 = null;
		p4_10 = null;
		p4 = null;

		p5_1 = null;
		p5_2 = null;
		p5_3 = null;
		p5_4 = null;
		p5_5 = null;
		p5_6 = null;
		p5_7 = null;
		p5_8 = null;
		p5_9 = null;
		p5 = null;
		
		p6_1 = null;
		p6_2 = null;
		p6_3 = null;
		p6_4 = null;
		p6 = null;
		
		p7_1 = null;
		p7 = null;
		
	}

	/**
	 * Tests totalDistance()
	 */
	@Test
	public void test_totalDistance() {
		
		assertTrue(PathCalculation.totalDistance(p1) == 493.39571928714287);
		assertTrue(PathCalculation.totalDistance(p2) == 451.0555127546399);
		assertTrue(PathCalculation.totalDistance(p3) == 500.41522986797287);
		assertTrue(PathCalculation.totalDistance(p4) == 397.5020274998677);
		assertTrue(PathCalculation.totalDistance(p5) == 625.0);
		assertTrue(PathCalculation.totalDistance(p6) == 40.0);
		assertTrue(PathCalculation.totalDistance(p7) == 0.0);
		
	}

	/**
	 * Tests totalTurns()
	 */
	@Test
	public void test_totalTurns() {
		assertTrue(PathCalculation.totalTurns(p1) == 10);
		assertTrue(PathCalculation.totalTurns(p2) == 8);
		assertTrue(PathCalculation.totalTurns(p3) == 5);
		assertTrue(PathCalculation.totalTurns(p4) == 8);
		assertTrue(PathCalculation.totalTurns(p5) == 7);
		assertTrue(PathCalculation.totalTurns(p6) == 0);
		assertTrue(PathCalculation.totalTurns(p7) == 3);
	}

	/**
	 * Tests totalTime()
	 */
	@Test
	public void test_totalTime() {
		assertTrue(PathCalculation.totalTime(p1) == 33.32508667694483);
		assertTrue(PathCalculation.totalTime(p2) == 30.436886659894807);
		assertTrue(PathCalculation.totalTime(p3) == 33.63703562876823);
		assertTrue(PathCalculation.totalTime(p4) == 26.829621393892285);
		assertTrue(PathCalculation.totalTime(p5) == 42.033185809585476);
		assertTrue(PathCalculation.totalTime(p6) == 2.6666666666666665);
		assertTrue(PathCalculation.totalTime(p7) == 0);
	}

}
