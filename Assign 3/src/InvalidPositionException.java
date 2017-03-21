
/**
 * Class creates an exception to be thrown when an invalid position is called.
 * @author Susan Fayez
 * 001404420
 */
public class InvalidPositionException extends Exception{

	/**
	 * Throws the exception.
	 * 
	 * @param message - the message to be displayed to the user.
	 */
	public InvalidPositionException(String message) {
        super(message);
    }
}
