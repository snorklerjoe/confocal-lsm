package com.hosticlefifer.lsm_control.plotting;

import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;

import java.awt.*;
import java.util.ArrayList;

class PlotTest {
    public static void main(String[] args) {
        ArrayList<DataPoint> points = new ArrayList<>();

        points.add(new DataPoint(0, 0, 100, 300, DataPointType.CONFOCAL));
        points.add(new DataPoint(0, 100, 100, 300, DataPointType.CONFOCAL));
        points.add(new DataPoint(100, 0, 100, 300, DataPointType.CONFOCAL));
        points.add(new DataPoint(100, 100, 100, 300, DataPointType.CONFOCAL));
        points.add(new DataPoint(0, 0, 0, 500, DataPointType.CONFOCAL));
        points.add(new DataPoint(0, 100, 0, 600, DataPointType.CONFOCAL));
        points.add(new DataPoint(100, 0, 0, 700, DataPointType.CONFOCAL));
        points.add(new DataPoint(100, 100, 0, 800, DataPointType.CONFOCAL));

        for(int i = 0; i < 100; i+=10)
            for(int j = 0; j < 100; j+=10)
                points.add(new DataPoint(i, j, 0, 1000, DataPointType.CONFOCAL));
        for(int i = 0; i < 100; i+=10)
            for(int j = 0; j < 100; j+=10)
                points.add(new DataPoint(i, j, 100, 1000, DataPointType.CONFOCAL));

        Viewer3D viewer = new Viewer3D(points, 100, 50);
        viewer.normalizeMagnitude(20);
        viewer.show(Color.GREEN);
    }
}