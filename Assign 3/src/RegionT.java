
/**
 * A class for a region ADT.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class RegionT {
	
	//Defining global variables.
	private PointT lower_left;
	private double width;
	private double height;
	
	/**
	 * Constructor for RegionT.
	 * 
	 * @param p - the lower left point in the region.
	 * @param w - the width of the region.
	 * @param h - the height of the region.
	 * @throws InvalidRegionException - if the region falls out of range.
	 */
	public RegionT(PointT p, double w, double h) throws InvalidRegionException{
		if(w < 0 || h < 0 || (p.xcrd() + w) >= Constants.MAX_X || (p.ycrd() + h) >= Constants.MAX_Y){
			throw new InvalidRegionException("Invalid Region.");
		}
		
		this.lower_left = p;
		this.width = w;
		this.height = h;
	}
	/**
	 * Checks whether a given point is in the region.
	 * @param p - the point to be checked.
	 * @return - whether the point is in the region.
	 */
	public boolean pointInRegion(PointT p){
		boolean ans1 = false;
		boolean ans2 = false;
		if(p.xcrd() - Constants.TOLERANCE > this.lower_left.xcrd() && p.xcrd() + Constants.TOLERANCE < this.lower_left.xcrd() + width){
			ans1 = true;
		}
		if(p.ycrd() - Constants.TOLERANCE > this.lower_left.ycrd() && p.ycrd() + Constants.TOLERANCE < this.lower_left.ycrd() + height){
			ans2 = true;
		}
		boolean ans3 = ans1 && ans2;
		return ans3;
	}
}
