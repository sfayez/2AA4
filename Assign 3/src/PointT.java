/**
 * A class for a point ADT.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class PointT {
	
	//Defining global variables
	private double xc;
	private double yc;
	
	/**
	 * Constructor for PointT
	 * 
	 * @param x - the x-coordinate of the point.
	 * @param y - the y-coordinate of the point.
	 * @throws InvalidPointException - if the coordinates are out of range.
	 */
	public PointT(double x, double y) throws InvalidPointException{
		if(x <= 0 || x >= Constants.MAX_X || y <= 0 || y >= Constants.MAX_Y){
			throw new InvalidPointException("Invalid Point");
		}
		
		this.xc = x;
		this.yc = y;
	}
	
	/**
	 * @return - the x-coordinate of the point.
	 */
	public double xcrd(){
		return this.xc;
	}
	
	/**
	 * @return - the y-coordinate of the point.
	 */
	public double ycrd(){
		return this.yc;
	}
	/**
	 * Calculates the distance between two points.
	 * 
	 * @param p - the point to find the distance from.
	 * @return - the distance between the two points.
	 */
	public double dist(PointT p){
		return Math.sqrt(Math.pow(this.xc - p.xcrd(), 2)+ Math.pow(this.yc - p.ycrd(), 2));
	}
	
}
