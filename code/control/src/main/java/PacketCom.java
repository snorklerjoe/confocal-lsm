import Commands.Command;
import Commands.ReadADC;
import Commands.SetPosition;

import java.io.IOException;
import java.net.*;
import java.util.ArrayList;
import java.util.Arrays;

/**
 * Communication via UDP packets to the microscope
 * @author Joseph R. Freeston
 */
public class PacketCom {
    private final InetAddress hostAddress;
    private final int hostPort;
    private DatagramSocket socket;
    public static final int MAX_BULKSIZE = 256;

    /**
     * Connects to the microscope:
     * @param listenPort Local port to use
     * @param address    Remote address to connect to
     * @param port       Remote port
     */
    public PacketCom(int listenPort, InetAddress address, int port) throws SocketException {
        socket = new DatagramSocket(listenPort);
        socket.setSoTimeout(20000);
        hostAddress = address;
        hostPort = port;
    }

    /**
     * Sends data and returns the response
     * @param data The data to send to the microscope
     * @return     The data received from the microscope
     * @throws IOException (if there is a problem with sending/receiving the packet)
     */
    public byte[] request(byte[] data) throws IOException {
        DatagramPacket packet = new DatagramPacket(data, data.length, hostAddress, hostPort);
        socket.send(packet);
        byte[] buf = new byte[9216];
        DatagramPacket recPacket = new DatagramPacket(buf, buf.length);
        socket.receive(recPacket);
        //System.out.println(new String(recPacket.getData(), recPacket.getOffset(), recPacket.getLength()));
        //if(recPacket.getAddress().equals(hostAddress)) {
            return Arrays.copyOfRange(recPacket.getData(), recPacket.getOffset(), recPacket.getLength());
        //}
        //else
        //    return new byte[0];
    }

    public Response request(Command command) throws IOException {
        return Response.fromBytes(request(command.getBytes()));
    }

    public ArrayList<Response> request(ArrayList<Command> commands) throws IOException {
        if(commands.size() > MAX_BULKSIZE)
            throw new IllegalArgumentException("Cannot send more than " + MAX_BULKSIZE + " commands at once!");
        ArrayList<Response> retVal = new ArrayList<>();
        byte[] buf = new byte[MAX_BULKSIZE*10];
        byte[] cmdBuf = new byte[10];
        int offset = 0;
        for(Command command : commands) {
            System.arraycopy(command.getBytes(), 0, buf, offset, 10);
            offset += 10;
        }
        buf = request(buf);
        for(int i = 0; i < offset; i += 10) {
            System.arraycopy(buf, i, cmdBuf, 0, 10);
            retVal.add(Response.fromBytes(cmdBuf));
        }
        return retVal;
    }

    /**
     * For use in adjusting the timeout, etc.
     * @return The DatagramSocket object used to send/receive packets
     */
    public DatagramSocket getSocket() {
        return socket;
    }


    public static void main(String[] args) throws IOException {
        PacketCom microscope = new PacketCom(8080, InetAddress.getByName("192.168.1.193"), 4210);
        ArrayList<Command> commandsToSend= new ArrayList<>();
        //for(int i = 0; i < MAX_BULKSIZE; i+=(int)((double)4095/MAX_BULKSIZE)) {
        //    System.out.println(i);
        //    commandsToSend.add(new SetPosition(i, i, 0, 100));
        //}
        //microscope.request(commandsToSend);
        //commandsToSend.clear();
        //commandsToSend.add(new SetPosition(4000, 4000, 0, 1));
        //commandsToSend.add(new SetPosition(0, 0, 0, 0));
        //commandsToSend.add(new SetPosition(10, 10, 10, 0));
        commandsToSend.add(new ReadADC(1));
        //commandsToSend.add(new Command((byte)'Z', 1, 1, 1, 1));
        System.out.println(microscope.request(commandsToSend).get(0).getA());
    }
}

