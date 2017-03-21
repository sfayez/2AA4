

/**
 * Class stores lists that contain the locations on the map.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class Map {
	
	//Defining global variables.
	private static Obstacles obstacles;
	private static Destinations destinations;
	private static SafeZone safezone;

	/**
	 * Method initializes the map.
	 * 
	 * @param o - the list of obstacles.
	 * @param d - the list of destinations.
	 * @param sz - the list of safe zones.
	 */
	public static void init(Obstacles o, Destinations d, SafeZone sz){
		obstacles = o;
		destinations = d;
		safezone = sz;
	}
	
	/**
	 * @return - the list of obstacles.
	 */
	public static Obstacles get_obstacles(){
		return obstacles;
	}
	
	/**
	 * @return - the list of destinations.
	 */
	public static Destinations get_destinations(){
		return destinations;
	}
	
	/**
	 * @return - the list of safe zones.
	 */
	public static SafeZone get_safeZone(){
		return safezone;
	}
}
