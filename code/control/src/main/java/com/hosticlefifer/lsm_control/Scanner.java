package com.hosticlefifer.lsm_control;

import com.hosticlefifer.lsm_control.Commands.Command;
import com.hosticlefifer.lsm_control.data_handling.Scan;

import java.util.ArrayList;

/**
 * Defines a scanner, capable of scanning (duh).
 * @see com.hosticlefifer.lsm_control.data_handling.Scan
 */
public abstract class Scanner {
    private int quality;
    private boolean invert;
    private int xRes, yRes;
    private int fov;

    public Scanner(int quality, boolean invert, int xRes, int yRes, int fov) {
        this.quality = quality;
        this.invert = invert;
        this.xRes = xRes;
        this.yRes = yRes;
        this.fov = fov;
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
    public abstract Scan fromResponse(ArrayList<Response> fromMicroscope);

}
