
/**
 * Class creates an exception to be called when an invalid region is called.
 * @author Susan Fayez
 * 001404420
 */
public class InvalidRegionException extends Exception{

	/**
	 * Throws the exception.
	 * 
	 * @param message - the message to be displayed to the user.
	 */
	public InvalidRegionException(String message) {
        super(message);
    }
}
