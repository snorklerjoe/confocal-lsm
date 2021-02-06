package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.util.ArrayList;
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
    private JSpinner xRes;
    private JSpinner xyScale;
    private JSpinner yRes;
    private JCheckBox invertCheckBox;
    private JSpinner scanQuality;
    private JComboBox patternType;
    private JComboBox comboBox1;
    private JSpinner zMin;
    private JSpinner zStep;
    private JSpinner zMax;
    private JComboBox comboBox2;
    private JButton runButton;
    private JButton stopButton;
    private JButton calculateButton;
    private JComboBox comboBox3;
    private JButton openButton;
    private JButton saveButton;
    private JButton contourButton;
    private JFormattedTextField infoBox;
    private JTextArea outputBox;
    private SpinnerModel xAxis, yAxis, xResModel, yResModel, zAxis, scaling, zMinModel, zMaxModel, zStepModel;

    Timer timer;
    LSM microscope = null;

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
        xAxis = new SpinnerNumberModel(0, 0, 4096, 1);
        yAxis = new SpinnerNumberModel(0, 0, 4096, 1);
        xResModel = new SpinnerNumberModel(0, 0, 4096, 1);
        yResModel = new SpinnerNumberModel(0, 0, 4096, 1);
        zAxis = new SpinnerNumberModel(0, 0, 255, 1);
        scaling = new SpinnerNumberModel(100, 1, 100, 1);
        zMinModel = new SpinnerNumberModel(100, 0, 255, 1);
        zStepModel = new SpinnerNumberModel(1, 1, 255, 1);
        zMaxModel = new SpinnerNumberModel(100, 0, 255, 1);
        xPos.setModel(xAxis);
        yPos.setModel(yAxis);
        xRes.setModel(xResModel);
        yRes.setModel(yResModel);
        zPos.setModel(zAxis);
        xyScale.setModel(scaling);
        zMax.setModel(zMaxModel);
        zStep.setModel(zStepModel);
        zMin.setModel(zMinModel);

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
                        setEnabledRecursive(rootPanel, true);
                        connectButton.setEnabled(false);
                        microscope.request(microscope.setConnectedLed(true));
                        infoBox.setText("Connected.");
                        outputBox.setText("Connected.\n");
                        timer = new Timer(true);
                        timer.schedule(new UpdateInfo(), 0, 1000);
                        outputBox.append("\nStarted info updating service.");
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
