package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.Commands.SetPosition;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;
import com.hosticlefifer.lsm_control.data_handling.Scan;
import com.hosticlefifer.lsm_control.scanners.ConsecutiveScanner;
import com.hosticlefifer.lsm_control.scanners.SScanner;
import com.hosticlefifer.lsm_control.scanners.ZScanType;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.text.DefaultCaret;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.TimerTask;
import java.util.Timer;

public class App {
    private JPanel rootPanel;
    private JButton connectButton;
    private JButton disconnectButton;
    private JTextArea LDCurrent;
    private JButton laserOffButton;
    private JButton laserOnButton;
    private JSpinner xPos;
    private JSpinner yPos;
    private JSpinner zPos;
    private JTextArea txSensorVal;
    private JTextArea reflSensorVal;
    private JSpinner resolution;
    private JSpinner fov;
    private JSpinner yRes;
    private JCheckBox invertCheckBox;
    private JSpinner scanQuality;
    private JComboBox patternType;
    private JComboBox zScanType;
    private JSpinner zMin;
    private JSpinner zStep;
    private JSpinner zMax;
    private JComboBox scanMode;
    private JButton runButton;
    private JButton stopButton;
    private JButton focusButton;
    private JComboBox focusMode;
    private JButton openButton;
    private JButton saveButton;
    private JButton contourButton;
    private JFormattedTextField infoBox;
    private JTextArea outputBox;
    private JPanel scanR;
    private JPanel scanP;
    private JPanel scanZ;
    private JPanel scanM;
    private JCheckBox listPointsCheckBox;
    private JScrollPane scroll;

    private Thread scannerThread;
    private SScanner scanner;
    private Timer timer;
    private LSM microscope = null;
    private ArrayList<Command> queue;
    private Focus focus;
    private Scan image;

    final class UpdateInfo extends TimerTask {
        @Override
        public void run() {
            ArrayList<Command> commandQueue = new ArrayList<>();
            commandQueue.add(new Command((byte)'A', 0, 0, 0, 0));
            commandQueue.add(microscope.getSensorC());
            commandQueue.add(microscope.getSensorT());
            commandQueue.add(microscope.getLaserVoltage());
            ArrayList<Response> results = microscope.request(commandQueue);
            if(results.get(0).isACK()) {
                infoBox.setText("Connected");
                if(!xPos.hasFocus())
                    xPos.setValue(results.get(3).getX());
                if(!yPos.hasFocus())
                    yPos.setValue(results.get(3).getY());
                if(!zPos.hasFocus())
                    zPos.setValue(results.get(3).getZ());
                LDCurrent.setText(String.format("%04f", (results.get(3).getA())*(double)5/1023) + " V");
                reflSensorVal.setText(String.format("%04d", results.get(1).getA()));
                txSensorVal.setText(String.format("%04d", results.get(2).getA()));
                //outputBox.append("\n[Info updating service ran.]");
            }
        }
    }

    public App() {
        infoBox.setText("Disconnected.");
        outputBox.setText("Disconnected.\n");
        setEnabledRecursive(rootPanel, false);
        connectButton.setEnabled(true);

        connectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                try {
                    microscope = new LSM();
                    if(microscope.ping()) {
                        // Set up spinner models:
                        final SpinnerModel xAxis, yAxis, resModel, zAxis, scaling, zMinModel, zMaxModel, zStepModel;
                        xAxis = new SpinnerNumberModel(0, 0, Integer.parseInt(microscope.getProperties().getProperty("maxRes")), 1);
                        yAxis = new SpinnerNumberModel(0, 0, Integer.parseInt(microscope.getProperties().getProperty("maxRes")), 1);
                        resModel = new SpinnerNumberModel(10, 10, Integer.parseInt(microscope.getProperties().getProperty("maxRes")), 1);
                        zAxis = new SpinnerNumberModel(0, 0, Integer.parseInt(microscope.getProperties().getProperty("maxZRes")), 1);
                        scaling = new SpinnerNumberModel(100, 1, 100, 1);
                        zMinModel = new SpinnerNumberModel(100, 0, Integer.parseInt(microscope.getProperties().getProperty("maxZRes")), 1);
                        zStepModel = new SpinnerNumberModel(1, 1, Integer.parseInt(microscope.getProperties().getProperty("maxZRes")), 1);
                        zMaxModel = new SpinnerNumberModel(100, 0, Integer.parseInt(microscope.getProperties().getProperty("maxZRes")), 1);
                        xPos.setModel(xAxis);
                        yPos.setModel(yAxis);
                        resolution.setModel(resModel);
                        zPos.setModel(zAxis);
                        fov.setModel(scaling);
                        zMax.setModel(zMaxModel);
                        zStep.setModel(zStepModel);
                        zMin.setModel(zMinModel);
                        // Some other stuff to do when connecting:
                        setEnabledRecursive(rootPanel, true);
                        connectButton.setEnabled(false);
                        microscope.request(microscope.setConnectedLed(true));  // Turn on a little LED to show that we're connected
                        infoBox.setText("Connected.");
                        outputBox.setText("Connected.\n");
                        timer = new Timer(true);
                        timer.schedule(new UpdateInfo(), 0, 1000);
                        outputBox.append("\nStarted info updating service.");
                        DefaultCaret caret = (DefaultCaret)outputBox.getCaret();
                        caret.setUpdatePolicy(DefaultCaret.ALWAYS_UPDATE);
                    }
                } catch (IOException e) {
                    ErrorDisplay.alert("Cannot access configuration file.", e);
                    outputBox.setText("Disconnected, CANNOT ACCESS CONFIG FILE.\n");
                }
            }
        });
        disconnectButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                if(!microscope.request(microscope.setLaser(false)).isACK())
                    ErrorDisplay.alert("Could not turn off laser!", new RuntimeException(microscope.request(microscope.setLaser(false)).toString()));
                microscope.request(microscope.setConnectedLed(false));
                microscope.disconnect();
                microscope = null;
                setEnabledRecursive(rootPanel, false);
                connectButton.setEnabled(true);
                timer.cancel();
                infoBox.setText("Disconnected.");
                outputBox.setText("Disconnected.\n\nStopped.");
            }
        });
        laserOnButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                microscope.request(microscope.setLaser(true));
            }
        });
        laserOffButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                microscope.request(microscope.setLaser(false));
            }
        });
        runButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                // Disable the scan-related fields; they won't update mid-scan!
                setEnabledRecursive(scanM, false);
                setEnabledRecursive(scanR, false);
                setEnabledRecursive(scanP, false);
                setEnabledRecursive(scanZ, false);
                runButton.setEnabled(false);
                stopButton.setEnabled(true);

                DataPointType type = DataPointType.CONFOCAL;
                if(scanMode.getSelectedIndex() == 1) {
                    type = DataPointType.TRANSMISSION;
                }
                ZScanType zScan = ZScanType.DISCRETE;
                if(zScanType.getSelectedIndex() == 1) {
                    zScan = ZScanType.FRAMES;
                }
                outputBox.append("\nGenerating scanning pattern...");
                switch(patternType.getSelectedIndex()) {
                    case 0:
                        scanner = new ConsecutiveScanner(microscope, getSpinner(scanQuality), invertCheckBox.isSelected(), getSpinner(resolution),
                                getSpinner(fov), type, zScan, getSpinner(zMin), getSpinner(zStep), getSpinner(zMax));
                        break;
                    default:
                        ErrorDisplay.alert("Unsupported scanning pattern type " + patternType.getSelectedIndex(), new RuntimeException());
                }

                queue = scanner.getScanningPattern();
                scannerThread = new Thread(){
                    private boolean running = true;

                    public void interrupt() {
                        running = false;
                    }
                    public void run() {
                        ArrayList<Response> rawData = new ArrayList<>();
                        for(int i = 0; i < queue.size(); i+=PacketCom.MAX_BULKSIZE) {  // Split up the scan into chunks that the microscope can receive in packets:
                            if(!running)
                                break;
                            ArrayList<Response> rawDataChunk = microscope.request(new ArrayList(queue.subList(i, Math.min(i+PacketCom.MAX_BULKSIZE-1, queue.size()-1))));
                            if(listPointsCheckBox.isSelected())
                                outputBox.append(rawDataChunk.toString());
                            rawData.addAll(rawDataChunk);
                            image = scanner.fromResponse(rawData, i);
                            outputBox.append(".");
                        }
                        if(running) {
                            outputBox.append("\n\nFinished scan!");
                            setEnabledRecursive(scanM, true);
                            setEnabledRecursive(scanR, true);
                            setEnabledRecursive(scanP, true);
                            setEnabledRecursive(scanZ, true);
                            runButton.setEnabled(true);
                            stopButton.setEnabled(false);
                        } else
                            outputBox.append("\n\nAborted scan.");
                        infoBox.setText("Connected.");
                    }
                };
                infoBox.setText("Scanning...");
                outputBox.append("\nScanning");
                scannerThread.start();
            }
        });
        stopButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                infoBox.setText("Connected.");
                setEnabledRecursive(scanM, true);
                setEnabledRecursive(scanR, true);
                setEnabledRecursive(scanP, true);
                setEnabledRecursive(scanZ, true);
                runButton.setEnabled(true);
                stopButton.setEnabled(false);
                scannerThread.interrupt();
                if(!microscope.request(microscope.setLaser(false)).isACK())
                    ErrorDisplay.alert("Could not turn off laser!", new RuntimeException(microscope.request(microscope.setLaser(false)).toString()));
            }
        });
        xPos.addMouseWheelListener(new MouseWheelListener() {
            @Override
            public void mouseWheelMoved(MouseWheelEvent mouseWheelEvent) {
                microscope.request(new SetPosition(getSpinner(xPos)-mouseWheelEvent.getWheelRotation(), getSpinner(yPos), getSpinner(zPos), 0));
            }
        });
        yPos.addMouseWheelListener(new MouseWheelListener() {
            @Override
            public void mouseWheelMoved(MouseWheelEvent mouseWheelEvent) {
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos)-mouseWheelEvent.getWheelRotation(), getSpinner(zPos), 0));
            }
        });
        zPos.addMouseWheelListener(new MouseWheelListener() {
            @Override
            public void mouseWheelMoved(MouseWheelEvent mouseWheelEvent) {
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos), getSpinner(zPos)-mouseWheelEvent.getWheelRotation(), 0));
            }
        });
        xPos.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos), getSpinner(zPos), 0));
                xPos.grabFocus();
            }
        });
        yPos.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos), getSpinner(zPos), 0));
                yPos.grabFocus();
            }
        });
        zPos.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent e) {
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos), getSpinner(zPos), 0));
                zPos.grabFocus();
            }
        });
        focusButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                DataPointType type = DataPointType.CONFOCAL;
                if(focusMode.getSelectedIndex() == 1)
                    type = DataPointType.TRANSMISSION;
                focus = new Focus(microscope, type);
                int distance = (getSpinner(zMax) - getSpinner(zMin))/2;
                zMin.setValue(focus.find() - distance);
                zMax.setValue(focus.getFocalPoint() + distance);
                microscope.request(new SetPosition(getSpinner(xPos), getSpinner(yPos), focus.getFocalPoint(), 0));
            }
        });
    }

    private static int getSpinner(JSpinner spinner) {
        return (int)spinner.getModel().getValue();
    }

    private void setEnabledRecursive(JPanel panel, boolean en) {
        for(Component toBeDisabled : panel.getComponents()) {
            toBeDisabled.setEnabled(en);
            if(toBeDisabled instanceof JPanel)
                setEnabledRecursive((JPanel)toBeDisabled, en);
        }
    }

    private static void message(String msg) {
        JOptionPane.showMessageDialog(JOptionPane.getRootFrame(), msg);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("LSM Control");
        frame.setContentPane(new App().rootPanel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        /*try {
            UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
        }
        catch(Exception e) {
            System.out.println(Arrays.toString(UIManager.getInstalledLookAndFeels()));
        }*/
    }

    private void createUIComponents() {
        // TODO: place custom component creation code here
    }
}
