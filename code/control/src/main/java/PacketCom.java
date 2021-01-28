import java.io.IOException;
import java.net.*;
import java.util.Arrays;

/**
 * Packetcom-- Communication via UDP packets to the microscope
 * @author Joseph R. Freeston
 * @since 1/25/21
 */
public class PacketCom {
    private final InetAddress hostAddress;
    private final int hostPort;
    private DatagramSocket socket;

    /**
     * Connects to the microscope:
     * @param listenPort Local port to use
     * @param address    Remote address to connect to
     * @param port       Remote port
     */
    public PacketCom(int listenPort, InetAddress address, int port) throws SocketException {
        socket = new DatagramSocket(listenPort);
        socket.setSoTimeout(500);
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
        byte[] buf = new byte[4096];
        DatagramPacket recPacket = new DatagramPacket(buf, buf.length);
        socket.receive(recPacket);
        //System.out.println(new String(recPacket.getData(), recPacket.getOffset(), recPacket.getLength()));
        //if(recPacket.getAddress().equals(hostAddress)) {
            return Arrays.copyOfRange(recPacket.getData(), recPacket.getOffset(), recPacket.getLength());
        //}
        //else
        //    return new byte[0];
    }

    public static void main(String[] args) throws IOException {
        PacketCom microscope = new PacketCom(8080, InetAddress.getByName("192.168.1.193"), 4210);
        System.out.println(new String(microscope.request("This data is sent from the java program!".getBytes())));
    }
}

