package com.hosticlefifer.lsm_control.data_handling;

/**
 * Stores a datapoint from a scan, representing an individual pixel at specific x, y, and z coordinates.
 */
public final class DataPoint implements Comparable<DataPoint>{
    private final int x, y, z, measurement;
    private final DataPointType type;

    /**
     * Constructs an immutable DataPoint object
     * @param x The x-coordinate of the data point
     * @param y The y-coordinate of the data point
     * @param z The z-coordinate of the data point
     * @param measurement The intensity value from the photodiode, specified by the DataPointType parameter
     * @param type The type of data point, confocal or transmission-mode
     */
    public DataPoint(int x, int y, int z, int measurement, DataPointType type) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.measurement = measurement;
        this.type = type;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public int getZ() {
        return z;
    }

    /**
     * @return The relative intensity of this data point.
     */
    public int getMeasurement() {
        return measurement;
    }

    public DataPointType getType() {
        return type;
    }

    public int getCoordinate(Axis direction) {
        switch(direction) {
            case X:
                return getX();
            case Y:
                return getY();
            default:
                return getZ();
        }
    }

    public int compareTo(DataPoint o) {
        return Integer.compare(measurement, o.measurement);
    }

    public String toString() {
        return type.toString()+": (" + x + ", " + y + ", " + z + ")->"+measurement;
    }
}
