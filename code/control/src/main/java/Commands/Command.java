package Commands;

import java.nio.ByteBuffer;
import java.util.Arrays;

/**
 * Represents a command
 * @author Joseph R. Freeston
 */
public class Command {
    private byte cmd;
    private final int a;
    private final int x;
    private final int y;
    private final int z;

    /**
     * Constructs a Commands.Command object.
     * @param command A byte to specify the command
     * @param a Generic parameter of the command
     * @param x Coordinate parameter of the command
     * @param y Coordinate parameter of the command
     * @param z Coordinate parameter of the command
     */
    public Command(byte command, int a, int x, int y, int z) {
        cmd = command;
        this.a = a;
        this.x = x;
        this.y = y;
        this.z = z;
    }

    /**
     * @return Bytes forming the command as it will be sent to the microcontroller
     */
    public final byte[] getBytes() {
        byte[] retVal = new byte[10];
        retVal[0] = cmd;
        retVal[2] = ByteBuffer.allocate(4).putInt(a).array()[3];
        retVal[3] = ByteBuffer.allocate(4).putInt(a).array()[2];
        retVal[4] = ByteBuffer.allocate(4).putInt(x).array()[3];
        retVal[5] = ByteBuffer.allocate(4).putInt(x).array()[2];
        retVal[6] = ByteBuffer.allocate(4).putInt(y).array()[3];
        retVal[7] = ByteBuffer.allocate(4).putInt(y).array()[2];
        retVal[8] = ByteBuffer.allocate(4).putInt(z).array()[3];
        retVal[9] = ByteBuffer.allocate(4).putInt(z).array()[2];
        //for(int i = 0; i < 9; i++)
        //    if((int)retVal[i] == 0)
        //        retVal[i] = (byte)0xFF;
        //System.out.println(Arrays.toString(retVal));
        return retVal;
    }

    public byte getCmd()
    {
        return cmd;
    }

    public void setCmd(byte val) {
        cmd = val;
    }

    public int getA()
    {
        return a;
    }

    public int getX()
    {
        return x;
    }

    public int getY()
    {
        return y;
    }

    public int getZ() {
        return z;
    }

    public boolean isACK() {
        return getCmd() == (byte) 'A';
    }

    public String toString() {
        return (char)cmd + " A" + a + " X" + x + " Y" + y + " Z" + z;
    }
}
