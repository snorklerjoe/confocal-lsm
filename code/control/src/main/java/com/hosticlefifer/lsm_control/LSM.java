package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.Commands.ReadADC;
import com.hosticlefifer.lsm_control.Commands.SetPosition;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;

import java.io.IOException;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.Properties;

public final class LSM {
    private final PacketCom microscope;
    private Properties prop;
    private int quality;

    public LSM() throws IOException {
        prop = new Properties();
        prop.load(LSM.class.getClassLoader().getResourceAsStream("config.properties"));
        microscope = new PacketCom(Integer.parseInt(prop.getProperty("localPort")),
                InetAddress.getByName(prop.getProperty("remoteIp")),
                Integer.parseInt(prop.getProperty("remotePort")));
    }

    public void disconnect() {
        microscope.close();
    }

    public boolean ping() {
        try {
            return microscope.request(new Command((byte) 'A', 0, 0, 0, 0)).isACK();
        }
        catch(Exception e) {
            ErrorDisplay.alert("Cannot detect microscope!", e);
            return false;
        }
    }

    public Response request(Command cmd) {
        try {
            return microscope.request(cmd);
        }
        catch(Exception e) {
            ErrorDisplay.alert("Cannot reach microscope while requesting a command!", e);
            return (Response) cmd;
        }
    }

    public ArrayList<Response> request(ArrayList<Command> commands) {
        ArrayList<Command> command_subset;
        ArrayList<Response> response = new ArrayList<>();
        for(int i = 0; i < commands.size(); i+=PacketCom.MAX_BULKSIZE) {  // Send the instructions in chunks
            command_subset = new ArrayList<>(commands.subList(i, Math.min(i + PacketCom.MAX_BULKSIZE, commands.size())));
            try {
                response.addAll(microscope.request(command_subset));
            } catch (Exception e) {
                ErrorDisplay.alert("Cannot reach microscope while requesting bulk commands!", e);
                return new ArrayList<Response>();
            }
        }
        if(commands.size() != response.size())
            ErrorDisplay.alert("Error when requesting bulk commands!", new RuntimeException(commands.size() + " commands sent, but " + response.size() + " responses received."));
        return response;
    }

    public Command getSensorC() {
        return new ReadADC(Integer.parseInt(prop.getProperty("confocalSensorPin")));
    }

    public Command getSensorT() {
        return new ReadADC(Integer.parseInt(prop.getProperty("transmissionSensorPin")));
    }

    public Command getSensor(DataPointType mode) {
        if (mode == DataPointType.TRANSMISSION) {
            return getSensorT();
        }
        return getSensorC();
    }

    public Command getLaserVoltage() {
        return new ReadADC(Integer.parseInt(prop.getProperty("laserVoltagePin")));
    }

    public Command setLaser(boolean value) {
        return new SetIo(Integer.parseInt(prop.getProperty("laserControlPin")), value);
    }

    public Command setConnectedLed(boolean value) {
        return new SetIo(Integer.parseInt(prop.getProperty("connectedLedPin")), value);
    }

    public void setQuality(int val) {
        quality = val;
    }

    public Command position(int x, int y, int z) {
        return new SetPosition(x, y, z, quality);
    }

    public Properties getProperties() {
        return prop;
    }
}
