package com.hosticlefifer.lsm_control.scanners;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.Commands.Delay;
import com.hosticlefifer.lsm_control.LSM;
import com.hosticlefifer.lsm_control.Response;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;
import com.hosticlefifer.lsm_control.data_handling.Scan;

import java.util.ArrayList;

/**
 * Defines a scanner, capable of scanning (duh).
 * @see com.hosticlefifer.lsm_control.data_handling.Scan
 */
public abstract class SScanner {
    protected int quality;
    protected boolean invert;
    protected int res;
    protected int fov;
    protected DataPointType mode;
    protected ZScanType type;
    protected LSM microscope;
    protected int zMin, zStep, zMax;

    /**
     * @param microscope A reference to the microscope's LSM object
     * @param quality Quality. 0 means suer fast, anything greater is slower but better.
     * @param invert Swaps x and y
     * @param res Resolution (Images will be square)
     * @param fov FOV in %, 100 means full.
     */
    public SScanner(LSM microscope, int quality, boolean invert, int res, int fov, DataPointType mode, ZScanType type, int zMin, int zStep, int zMax) {
        this.microscope = microscope;
        this.quality = quality;
        this.invert = invert;
        this.res = res;
        this.fov = fov;
        this.mode = mode;
        this.type = type;
        this.zMin = zMin;
        this.zStep = zStep;
        this.zMax = zMax;
    }

    /**
     * Generates the scanning pattern based on the parameters specified in the constructor
     * @return ArrayList of Command objects to be sent to the microscope
     * @see com.hosticlefifer.lsm_control.LSM#request(ArrayList)
     */
    public abstract ArrayList<Command> getScanningPattern();

    /**
     * Picks out and formats the data back from the microscope into a Scan object so that it may be processed.
     * @param fromMicroscope The raw data returned by the request, to be processed.
     * @return A Scan object which may be displayed and/or processed further
     */
    public abstract Scan fromResponse(ArrayList<Response> fromMicroscope, int offset);

    /**
     * @return The generated preamble for the scan
     */
    protected ArrayList<Command> getPreamble() {
        ArrayList<Command> retVal = new ArrayList<>();
        // Blink the LED 10 times:
        for(int i = 0; i < 10; i++) {
            retVal.add(microscope.setConnectedLed(true));
            retVal.add(new Delay(100));
            retVal.add(microscope.setConnectedLed(false));
            retVal.add(new Delay(100));
        }
        retVal.add(microscope.setConnectedLed(true));
        return retVal;
    }
}
