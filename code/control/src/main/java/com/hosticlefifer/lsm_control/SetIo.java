package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;

public class SetIo extends Command {
    /**
     * Constructs a Commands.Command object.
     *
     * @param pin    Io pin to set
     * @param value  value to set it to
     */
    public SetIo(int pin, boolean value) {
        super((byte) 'O', value?1:0, pin, 0, 0);
    }

    /**
     * Constructs a Commands.Command object.
     *
     * @param command A byte to specify the command
     * @param a       Generic parameter of the command
     * @param x       Coordinate parameter of the command
     * @param y       Coordinate parameter of the command
     * @param z       Coordinate parameter of the command
     */
    public SetIo(byte command, int a, int x, int y, int z) {
        super(command, a, x, y, z);
    }
}
