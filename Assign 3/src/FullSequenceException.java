
/**
 * Class defines an exception to be thrown when entering into a full sequence.
 * 
 * @author Susan Fayez
 * 001404420
 */
public class FullSequenceException extends Exception{

	/**
	 * Throws the exception.
	 * 
	 * @param message - The message displayed to the user when the exception is thrown.
	 */
	public FullSequenceException(String message) {
        super(message);
    }
}
