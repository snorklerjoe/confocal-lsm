package com.hosticlefifer.lsm_control.data_handling;

/**
 * Stores a datapoint from a scan, representing an individual pixel at specific x, y, and z coordinates.
 */
public final class DataPoint implements Comparable<DataPoint>{
    private double x, y, z, measurement;

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setZ(double z) {
        this.z = z;
    }

    private final DataPointType type;

    /**
     * Constructs an immutable DataPoint object
     * @param x The x-coordinate of the data point
     * @param y The y-coordinate of the data point
     * @param z The z-coordinate of the data point
     * @param measurement The intensity value from the photodiode, specified by the DataPointType parameter
     * @param type The type of data point, confocal or transmission-mode
     */
    public DataPoint(double x, double y, double z, int measurement, DataPointType type) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.measurement = measurement;
        this.type = type;
    }

    /**
     * Clones a datapoint
     * @param point the point to clone
     */
    public DataPoint(DataPoint point) {
        this(point.x, point.y, point.z, (int)point.measurement, point.type);
    }

    public int getX() {
        return (int)x;
    }

    public int getY() {
        return (int)y;
    }

    public int getZ() {
        return (int)z;
    }

    public double doubleGetX() {
        return x;
    }

    public double doubleGetY() {
        return y;
    }

    public double doubleGetZ() {
        return z;
    }

    /**
     * @return The relative intensity of this data point.
     */
    public int getMeasurement() {
        return (int)measurement;
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

    /**
     * Scales measurement by a given amount
     * @param m amount to multiply measurement by
     * @param b amount to add to the measurement
     */
    public void scaleMeasurement(double m, double b) {
        measurement *= Math.abs(m);
        measurement += b;
    }

    public int compareTo(DataPoint o) {
        return Double.compare(measurement, o.measurement);
    }

    public String toString() {
        return type.toString()+": (" + x + ", " + y + ", " + z + ")->"+measurement;
    }
}
