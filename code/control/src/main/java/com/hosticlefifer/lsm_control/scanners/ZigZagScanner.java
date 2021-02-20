package com.hosticlefifer.lsm_control.scanners;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.Commands.Delay;
import com.hosticlefifer.lsm_control.Commands.SetPosition;
import com.hosticlefifer.lsm_control.ErrorDisplay;
import com.hosticlefifer.lsm_control.LSM;
import com.hosticlefifer.lsm_control.Response;
import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;
import com.hosticlefifer.lsm_control.data_handling.Scan;

import java.util.ArrayList;

public class ZigZagScanner extends SScanner { // TODO: Make different from ConsecutiveScanner
    private int[] measurementIndices;

    public ZigZagScanner(LSM microscope, int quality, boolean invert, int res, int fov, DataPointType mode, ZScanType type, int zMin, int zStep, int zMax) {
        super(microscope, quality, invert, res, fov, mode, type, zMin, zStep, zMax);
    }

    @Override
    public final ArrayList<Command> getScanningPattern() {
        // Calculate image:
        final int maxRes = Integer.parseInt(microscope.getProperties().getProperty("maxRes"));
        final int p1 = maxRes/2 - (int)(maxRes * (double)fov/200);
        final int p2 = maxRes/2 + (int)(maxRes * (double)fov/200);
        final int step = (p2-p1)/res;

        // Generate points:
        ArrayList<Command> retVal = getPreamble();
        retVal.add(microscope.setLaser(true));
        measurementIndices = new int[(int)(res * res * (1+(zMax-zMin)/zStep) * 1.5)];
        int count = 0;
        for(int i = p1; i <= p2; i += step) {
            for(int j = p1; j <= p2; j += step) {
                for(int k = zMin; k <= zMax; k += zStep) {
                    if(invert) {
                        if(type == ZScanType.DISCRETE) {
                            retVal.add(new SetPosition(j, i, k, quality));
                        } else
                            retVal.add(new SetPosition(k, j, i, quality));
                    } else {
                        if (type == ZScanType.DISCRETE) {
                            retVal.add(new SetPosition(i, j, k, quality));
                        } else
                            retVal.add(new SetPosition(k, i, j, quality));
                    }
                    if(quality > 0) {
                        retVal.add(microscope.setLaser(true));  // Pulse the laser to improve quality
                        retVal.add(new Delay(quality));
                    }
                    measurementIndices[count] = retVal.size();  // Keep track of which indices are important
                    count++;
                    retVal.add(microscope.getSensor(mode));
                    if(quality > 0)
                        retVal.add(microscope.setLaser(false));
                }
            }
        }
        retVal.add(microscope.setLaser(false));
        return retVal;
    }

    @Override
    public final Scan fromResponse(ArrayList<Response> fromMicroscope, int offset) {
        ArrayList<DataPoint> data = new ArrayList<>();
        for(int i : measurementIndices) {
            try {
                Response point = fromMicroscope.get(i - offset);
                data.add(new DataPoint(point.getX(), point.getY(), point.getZ(), point.getA(), mode));
            } catch(IndexOutOfBoundsException ignored){
            } catch(Exception e) {
                ErrorDisplay.alert("Issue when picking data points out from the microscope's response.", e);
            }
        }
        return new Scan(data);
    }
}
