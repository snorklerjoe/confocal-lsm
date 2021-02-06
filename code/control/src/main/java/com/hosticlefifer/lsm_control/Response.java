package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;

import java.util.Arrays;

public class Response extends Command {

    /**
     * Constructs a Commands.Command object.
     *
     * @param command A byte to specify the command
     * @param a       Generic parameter of the command
     * @param x       Coordinate parameter of the command
     * @param y       Coordinate parameter of the command
     * @param z       Coordinate parameter of the command
     */
    public Response(byte command, int a, int x, int y, int z) {
        super(command, a, x, y, z);
    }

    public static Response fromBytes(byte[] bytes) {
        if(bytes.length < 9)
        {
            bytes = pad(bytes, 9);
        }
        //for(int i = 0; i < 9; i++)
        //    if((int)bytes[i] == -1)
        //        bytes[i] = 0;
        //System.out.println(Arrays.toString(bytes));
        //System.out.println(getBytesAsWord(bytes[2], bytes[3]));
        //System.out.println(bytes[2] + " " + bytes[3]);
        return new Response(bytes[0], getBytesAsWord(bytes[2], bytes[3]),
                getBytesAsWord(bytes[4], bytes[5]),
                getBytesAsWord(bytes[6], bytes[7]),
                getBytesAsWord(bytes[8], bytes[9]));
    }

    private static byte[] pad(byte[] bytes, int len) {
        byte[] retVal = new byte[len];
        Arrays.fill(retVal, (byte)0x00);
        System.arraycopy(bytes, 0, retVal, 0, bytes.length);
        return retVal;
    }

    private static int getBytesAsWord(byte byte1, byte byte2) {
        return ((byte2 & 0xff) << 8) | (byte1 & 0xff);
    }
}
