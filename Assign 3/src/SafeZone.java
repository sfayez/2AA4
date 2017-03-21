import java.util.ArrayList;

/**
 * Class for a GenericList to hold the safe zone.
 *
 *@author Susan Fayez
 *001404420
 */
public class SafeZone extends GenericList{
	
	//Redefining the constant from GenericList
	public static final int MAX_SIZE = 1;
	protected ArrayList<RegionT> s;
	
	/**
	 * Constructor for SafeZone
	 */
	public SafeZone(){
		this.s = new ArrayList<RegionT>();
	}
}
