package com.hosticlefifer.lsm_control.Commands;

public class SetPosition extends Command{

    /**
     * Constructs a Commands.Command object.
     *
     * @param speed   Speed at which to move to this point
     * @param x       Coordinate parameter of the command
     * @param y       Coordinate parameter of the command
     * @param z       Coordinate parameter of the command
     */
    public SetPosition(int x, int y, int z, int speed) {
        super((byte) 'S', speed, x, y, z);
        if(speed <= 0)
        {
            setCmd((byte) 'R');  // For rapid/high-speed
        }
    }
}
