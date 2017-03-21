
/**
 * Class contains functions that calculate data on paths.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class PathCalculation {

	/**
	 * Checks if given path segment is valid.
	 * 
	 * @param p1 - start point of segment
	 * @param p2 - end point of segment
	 * @return - whether given path segment is valid
	 * @throws InvalidPointException - if values entered into point constructor are invalid.
	 */
	public static boolean is_validSegment(PointT p1, PointT p2) throws InvalidPointException{
		boolean check = true;
		for(int i = 0; i < Map.get_obstacles().size(); i++){
			Object o = Map.get_obstacles().getval(i);
			for(int j=0; j<200; j++){
				double xp = (j/200) * p1.xcrd() + (1-(j/200)) * p2.xcrd();
				double yp = (j/200) * p1.ycrd() + (1-(j/200)) * p2.ycrd();
				PointT p = new PointT(xp, yp);
				if (((RegionT) o).pointInRegion(p)){
					check = false;
				}
			}
		}
		return check;
	}
	
	/**
	 * Checks whether a given path is valid.
	 * 
	 * @param p - Path for validity check.
	 * @return - whether or not the path is valid.
	 * @throws InvalidPointException - if cast to PointT is invalid.
	 */
	public static boolean is_validPath(PathT p) throws InvalidPointException{
		boolean check1 = true;
		boolean check2 = true;
		if(((RegionT) Map.get_safeZone().getval(0)).pointInRegion(((PointT)p.getval(0)))){
			if(((RegionT) Map.get_safeZone().getval(0)).pointInRegion(((PointT)p.getval(p.size()-1)))){
				for(int i=0; i < Map.get_destinations().size();i++){
					Object d = Map.get_destinations().getval(i);
					for(int j=0; j < p.size(); j++){
						if(!(((RegionT)d).pointInRegion((PointT)p.getval(j)))){
							check1 = false;
						}
					}
				}
				for(int i=0; i < p.size()-1; i++){
					if(!(is_validSegment((PointT)p.getval(i), (PointT)p.getval(i+1)))){
						check2 = false;
					}
				}
			}
		}
		return (check1 && check2);
	}
	
	/**
	 * Calculates the total distance of a path.
	 * 
	 * @param p - path for distance calculation.
	 * @return - total distance of the path.
	 */
	public static double totalDistance(PathT p){
		double dist = 0;
		
		for(int i=0; i < p.size()-1; i++){
			dist += ((PointT)p.getval(i)).dist(((PointT)p.getval(i+1)));
		}
		
		return dist;
	}
	
	/**
	 * Calculates the number of turns made in a path.
	 * 
	 * @param p - path for turns calculation.
	 * @return - number of turns in the path.
	 */
	public static int totalTurns(PathT p){
		int count = 0;
		
		for(int i=0; i < p.size()-2; i++){
			if(angle(((PointT)p.getval(i)), ((PointT)p.getval(i+1)), ((PointT)p.getval(i+2))) != 0){
				count += 1;
			}
		}
		
		return count;
	}
	
	/**
	 * Calculates the time to complete a path.
	 * 
	 * @param p - path for time calculation.
	 * @return - time to complete the path.
	 */
	public static double totalTime(PathT p){
		double ltime = 0;
		double atime = 0;
		
		for(int i=0; i < p.size()-1; i++){
			if(((PointT)p.getval(i)).dist(((PointT)p.getval(i+1))) == 0){
				ltime += 0;
			}
			else{
				ltime += ((PointT)p.getval(i)).dist(((PointT)p.getval(i+1))) / Constants.VELOCITY_LINEAR;
			}
		}
		
		for(int i=0; i < p.size()-2; i++){
			if(angle(((PointT)p.getval(i)), ((PointT)p.getval(i+1)), ((PointT)p.getval(i+2))) == 0){
				atime += 0;
			}
			else{
				atime += angle(((PointT)p.getval(i)), ((PointT)p.getval(i+1)), ((PointT)p.getval(i+2))) / Constants.VELOCITY_ANGULAR;
			}
			
		}
		
		Double ans = ltime + atime;
		if(ans.isNaN()){
			ans = (double) 0;
		}
		
		return ans;
	}
	
	/**
	 * Local function to calculate the angle of a turn.
	 * 
	 * @param p1 - the first point.
	 * @param p2 - the second point.
	 * @param p3 - the third point.
	 * @return - the angle of the turn.
	 */
	private static double angle(PointT p1, PointT p2, PointT p3){
		double u1 = p2.xcrd() - p1.xcrd();
		double u2 = p2.ycrd() - p1.ycrd();
		double v1 = p3.xcrd() - p2.xcrd();
		double v2 = p3.ycrd() - p2.ycrd();
		double ud = p1.dist(p2);
		double vd = p2.dist(p3);
		
		return Math.acos(((u1 * v1) + (u2 * v2)) / (ud * vd));
	}
	
}
