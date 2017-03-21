import java.util.ArrayList;

/**
 * Class defines a list to be used to hold various objects on the map.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class GenericList {
	
	//Defining global variables and constants
	public static final int MAX_SIZE = 100;
	protected ArrayList s;
	
	/**
	 * Constructor for GenericList. Creates an empty array.
	 */
	public GenericList(){
		this.s = new ArrayList();
	}
	
	/**
	 * Method to add objects to the list at a certain index and shift the other values.
	 * 
	 * @param i - index of position of insertion
	 * @param p - object to be inserted
	 * @throws Exception - if list is already full or an invalid position index is entered.
	 */
	public void add(int i, Object p) throws Exception{
		if(this.s.size() == MAX_SIZE){
			throw new FullSequenceException("Sequence is full.");
		}
		if(i > this.s.size() || i < 0){
			throw new InvalidPositionException("Invalid Position.");
		}
		
		this.s.add(i, p);
	}
	
	/**
	 * Deletes an object from the list.
	 * 
	 * @param i - index of object to be deleted.
	 * @throws InvalidPositionException - if invalid index is entered.
	 */
	public void del(int i) throws InvalidPositionException{
		if(i > this.s.size() - 1){
			throw new InvalidPositionException("Invalid Position.");
		}
		this.s.remove(i);
	}
	
	/**
	 * Changes the value at a certain position in the list.
	 * 
	 * @param i - index of change position.
	 * @param p - object to replace value.
	 * @throws InvalidPositionException  - if invalid index is entered.
	 */
	public void setval(int i, Object p) throws InvalidPositionException{
		if(i > this.s.size() - 1){
			throw new InvalidPositionException("Invalid Position.");
		}
		this.s.set(i, p);
	}
	
	/**
	 * Returns the object at a given index.
	 * 
	 * @param i - index of returned object.
	 * @return object at position i.
	 */
	public Object getval(int i){
		return this.s.get(i);
	}
	
	/**
	 * @return the number of items in the list.
	 */
	public int size(){
		return this.s.size();
	}
	
	
}
