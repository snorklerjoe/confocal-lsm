package com.hosticlefifer.lsm_control.Commands;

public class Delay extends Command {
    /**
     * Constructs a Commands.Command object.
     *
     * @param milliseconds The number of milliseconds to pause for
     */
    public Delay(int milliseconds) {
        super((byte) 'D', milliseconds, 0, 0, 0);
    }
}