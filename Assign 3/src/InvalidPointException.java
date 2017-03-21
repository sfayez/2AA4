
/**
 * Class creates an exception to be thrown when an invalid point is called.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class InvalidPointException extends Exception{

	/**
	 * Throws the exception.
	 * 
	 * @param message - the message to be displayed to the user.
	 */
	public InvalidPointException(String message) {
        super(message);
    }
}
