package com.hosticlefifer.lsm_control.data_handling;

import com.hosticlefifer.lsm_control.ErrorDisplay;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;

/**
 * Stores a large number of data points, taken in a single scan of a single type.
 */
public class Scan implements java.io.Serializable {
    private final LinkedHashMap<DataPoint> dataPoints;
    private final DataPointType scanType;

    /**
     * Converts an ArrayList of DataPoint's into a Scan object.
     * @param dataPoints An ArrayList of the data points collected by a scan
     */
    public Scan(LinkedHashMap<DataPoint> dataPoints) {
        this.dataPoints = dataPoints;
        if(dataPoints.size() > 1) {
            scanType = dataPoints.0).getType();
            for (DataPoint point : dataPoints) {
                if (!point.getType().equals(scanType))
                    throw new IllegalArgumentException("All data points MUST be of the same type as defined in the enum DataPointType");
            }
        }
        else
            scanType = null;
    }

    public Scan() {
        this(new ArrayList<DataPoint>());
    }

    /**
     * Deep copies a scan
     * @param image The image to copy (deep copy; copies DataPoints)
     */
    public Scan(Scan image) {
        this();
        for(DataPoint point : image.dataPoints)
            dataPoints.add(new DataPoint(point));
    }

    /**
     * @return The entire set of data points
     */
    public ArrayList<DataPoint> getDataPoints() {
        return dataPoints;
    }

    /**
     * @return the type od scan
     * @see DataPointType
     */
    public DataPointType getScanType() {
        return scanType;
    }

    /**
     * Loads a Scan object from a serialized file.
     * @param filename Name & path to the file
     * @return Scan object, or null if unsuccessful
     * @see Scan(ArrayList)
     */
    public static Scan load(String filename) {
        FileInputStream file;
        try {
            file = new FileInputStream(filename);
            ObjectInputStream object = new ObjectInputStream(file);
            Scan loadedScan = (Scan) object.readObject();
            file.close();
            object.close();
            return loadedScan;
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            return null;
        }
    }

    /**
     * Saves a Scan
     * @param filename File & path to save to
     * @return Whether or not the save was successful
     */
    public boolean save(String filename) {
        FileOutputStream file;
        if(!filename.endsWith(".ser"))
            filename += ".ser";
        try {
            file = new FileOutputStream(filename);
            ObjectOutputStream object = new ObjectOutputStream(file);
            object.writeObject(this);
            file.close();
            object.close();
            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    /**
     * The method to process a Scan-- can point out contours, do focal scanning, etc.
     * @param normal The normal vector of the plane, with the size being equivalent to the distance along the normal from the origin to the plane.
     * @param tolerance The tolerance from the given plane that is allowed
     * @param number The number of points in the axis of the normal to allow (Will choose the [number]th most intense points). Set to 0 for all.
     * @param minIntensity The minimum intensity of a point to include
     * @return Data points withing a given distance from the given plane
     * @see Vector
     */
    public ArrayList<DataPoint> getPlane(Vector normal, int tolerance, int number, int minIntensity) {
        // Slice out a plane:
        ArrayList<DataPoint> plane = new ArrayList<>();
        for(DataPoint point : dataPoints) {
            if(point.getMeasurement() > minIntensity) {
                switch (normal.getDirection()) {
                    case X:
                        if (Math.abs(point.getX() - normal.getMagnitude()) <= tolerance)
                            plane.add(point);
                        break;
                    case Y:
                        if (Math.abs(point.getY() - normal.getMagnitude()) <= tolerance)
                            plane.add(point);
                        break;
                    case Z:
                        if (Math.abs(point.getZ() - normal.getMagnitude()) <= tolerance)
                            plane.add(point);
                        break;
                }
            }
        }
        // Pick out the brightest ones (for contour):
        if(number > 0) {  // Well, if necessary anyway!
            // Organize the data:
            DataPoint[][][] organizedData = organize(plane);

            // Clear plane so we can refill it with only the points we want:
            plane.clear();

            // Next step is to iterate through the deepest nested arrays and keep only the brightest points:
            int count;
            for(DataPoint[][] jkPlane : organizedData) {
                for(DataPoint[] kLine : jkPlane) {
                    Arrays.sort(kLine);  // Sort by intensity
                    count = 0;
                    for(DataPoint point : kLine) {
                        plane.add(point);
                        count++;
                        if(count > number)
                            break;
                    }
                }
            }
        }

        return plane;
    }

    private static int countUnique(ArrayList<DataPoint> plane, int maxNum, Axis directionOfUniqueness) {
        Integer[] numX = new Integer[maxNum];
        int i = 0;
        for(DataPoint point : plane) {
            boolean absent = true;  // To keep track if the current point's x value is (so far) absent from numX
            for(Integer coordinate : numX) {
                if (point.getCoordinate(directionOfUniqueness) == (int) coordinate) {
                    absent = false;
                    break;
                }
            }
            if(absent) {
                numX[i] = point.getX();  // Add this no-longer-absent value to the array
                i++;
            }
        }
        return i;
    }

    private static Integer[] getUnique(ArrayList<DataPoint> plane, int maxNum, Axis directionOfUniqueness) {
        Integer[] numX = new Integer[maxNum];
        int i = 0;
        for(DataPoint point : plane) {
            boolean absent = true;  // To keep track if the current point's x value is (so far) absent from numX
            for(Integer coordinate : numX) {
                if (point.getCoordinate(directionOfUniqueness) == (int) coordinate) {
                    absent = false;
                    break;
                }
            }
            if(absent) {
                numX[i] = point.getX();  // Add this no-longer-absent value to the array
                i++;
            }
        }
        return numX;
    }

    private DataPoint[][][] organize(ArrayList<DataPoint> plane) {
        DataPoint[][][] scan = new DataPoint
                [countUnique(plane, dataPoints.size(), Axis.X)]
                [countUnique(plane, dataPoints.size(), Axis.Y)]
                [countUnique(plane, dataPoints.size(), Axis.Z)];  // TODO: Enable contour resolution on more than just the XY plane. Could be implemented with a simple switch/case here.
        Integer[] xVals = getUnique(plane, dataPoints.size(), Axis.X);
        Integer[] yVals = getUnique(plane, dataPoints.size(), Axis.Y);
        Integer[] zVals = getUnique(plane, dataPoints.size(), Axis.Z);
        Integer i = null;
        Integer j = null;
        Integer k = null;
        int count;
        for(DataPoint point : plane) {
            // Find the i, j, and k index values for scan[i][j][k]:
            count = 0;
            for(int xVal : xVals) {
                if(xVal == point.getX()) {
                    i = count;
                    break;
                }
                count++;
            }
            count = 0;
            for(int yVal : yVals) {
                if(yVal == point.getY()) {
                    j = count;
                    break;
                }
                count++;
            }
            count = 0;
            for(int zVal : zVals) {
                if(zVal == point.getZ()) {
                    k = count;
                    break;
                }
                count++;
            }
            try {
                if(i == null || j == null || k == null) {
                    throw new NullPointerException("i, j, or k index variable remains null in contour processing");  // Means there's an issue with getUnique()
                }
                scan[i][j][k] = point;  // Store the point where it belongs
            }
            catch(NullPointerException e) {
                ErrorDisplay.alert("Error processing the scan data. Could not resolve contour on point "+point.toString(), e);
            }
        }
        return scan;
    }

    /**
     * Adds all datapoints from fromResponse to this scan
     * @param fromResponse The scan to merge into this one.
     */
    public void merge(Scan fromResponse) {
        dataPoints.addAll(fromResponse.dataPoints);
    }
}