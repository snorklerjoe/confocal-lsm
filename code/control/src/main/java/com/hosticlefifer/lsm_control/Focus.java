package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.Commands.Delay;
import com.hosticlefifer.lsm_control.Commands.SetPosition;
import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Focus {
    private final LSM microscope;
    private int focalPoint;
    private final DataPointType sensor;

    public Focus(LSM microscope, DataPointType sensor) {
        this.microscope = microscope;
        this.sensor = sensor;
    }

    /**
     * Finds the focal point
     * @return The focal distance that was optimal
     */
    public final int find() {
        Response position = microscope.request(microscope.setLaser(true));
        ArrayList<Command> commands = new ArrayList<>();
        // Generates the commands to scan through all possible Z values:
        for(int i = 0; i < Integer.parseInt(microscope.getProperties().getProperty("maxZRes")); i++) {
            commands.add(new SetPosition(position.getX(), position.getY(), i, 0));
            commands.add(new Delay(10));
            commands.add(microscope.getSensor(sensor));
            commands.add(microscope.getSensor(sensor));
            commands.add(microscope.getSensor(sensor));
            commands.add(microscope.getSensor(sensor));
        }
        ArrayList<Response> rawData = microscope.request(commands);
        ArrayList<DataPoint> data = new ArrayList<>();
        // Pick out all of the data points:
        for(int i = 0; i < 6*Integer.parseInt(microscope.getProperties().getProperty("maxZRes")); i += 6) {
            data.add(new DataPoint(rawData.get(i).getX(), rawData.get(i).getY(), rawData.get(i).getZ(),
                    trimmedMean(new int[]{rawData.get(i + 2).getA(), rawData.get(i + 3).getA(), rawData.get(i + 4).getA(), rawData.get(i + 5).getA()}), sensor));
        }
        Collections.sort(data);
        focalPoint = trimmedMean(new int[]{data.get(0).getZ(), data.get(0).getZ(), data.get(0).getZ()});
        return focalPoint;
    }

    /**
     * Generates a trimmed mean, excluding one value.
     * @param values The values to process. One will be excluded (the furthest from the average), and the average of the remaining values will be calculated.
     * @return The trimmed mean
     */
    private int trimmedMean(int[] values) {  // TODO: This can probably be more efficient:
        int total = 0;
        for (int value : values) total += value;
        int mean = total / values.length;
        // "Trim" the biggest outlier:
        int outlierIndex = 0;
        for (int i = 0; i < values.length; i++) {
            if(Math.abs(values[i] - mean) > Math.abs(values[outlierIndex] - mean))
                outlierIndex = i;
        }
        // Calculate trimmed mean:
        total = 0;
        for (int i = 0; i < values.length; i++) {
            if(i != outlierIndex)
                total += values[i];
        }
        return total / (values.length - 1);
    }

    public final int getFocalPoint() {
        return focalPoint;
    }
}
