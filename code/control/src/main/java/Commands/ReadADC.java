package Commands;

public class ReadADC extends Command {

    /**
     * Constructs a Commands.Command object.
     *
     * @param pin   The ADC pin to read from
     */
    public ReadADC(int pin) {
        super((byte) 'V', pin, 0, 0, 0);
    }
}
