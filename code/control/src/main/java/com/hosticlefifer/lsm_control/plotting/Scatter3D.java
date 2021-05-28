package com.hosticlefifer.lsm_control.plotting;

import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;
import org.jzy3d.analysis.AWTAbstractAnalysis;
import org.jzy3d.analysis.AnalysisLauncher;
import org.jzy3d.chart.Chart;
import org.jzy3d.chart.EmulGLSkin;
import org.jzy3d.chart.factories.AWTChartFactory;
import org.jzy3d.chart.factories.EmulGLChartFactory;
import org.jzy3d.colors.Color;
import org.jzy3d.colors.ColorMapper;
import org.jzy3d.colors.colormaps.*;
import org.jzy3d.maths.Coord3d;
import org.jzy3d.plot3d.primitives.Scatter;
import org.jzy3d.plot3d.rendering.canvas.Quality;

import javax.xml.crypto.Data;
import java.util.ArrayList;
import java.util.Random;

public class Scatter3D {

    public static Scatter scatter(ArrayList<DataPoint> dataPoints) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for(DataPoint point : dataPoints) {
            if(point.getMeasurement() > max) max = point.getMeasurement();
            if(point.getMeasurement() < min) min = point.getMeasurement();
        }
        ColorMapper colorMapper = new ColorMapper(new ColorMapRainbow(), min, max);
        Coord3d[] points = new Coord3d[dataPoints.size()];
        Color[] colors = new Color[dataPoints.size()];

        for(int i = 0; i < points.length; i++) {
            DataPoint point = dataPoints.get(i);
            points[i] = new Coord3d(point.getX(), point.getY(), point.getZ());
            colors[i] = colorMapper.getColor(dataPoints.get(i).getMeasurement());
        }
        Scatter output = new Scatter(points, colors);
        output.setWidth(5);
        return output;
    }

    public static void main(String[] args) throws Exception {
        //Quality q = Quality.Advanced();
        Quality q = Quality.Intermediate();
        q.setAnimated(true);
        q.setHiDPIEnabled(true); // need java 9+ to enable HiDPI & Retina displays
        q.setSmoothColor(true);

        Chart chart = new EmulGLChartFactory().newChart(q);

        ArrayList<DataPoint> points = new ArrayList<>();
        for(int i = 0; i < 500; i++) {
            points.add(new DataPoint(Math.random()*500, Math.random()*500, 100+(50*Math.random()), (int)(Math.random()*500), DataPointType.CONFOCAL));
        }
        chart.add(scatter(points));
        chart.addLight(new Coord3d(0, 0, 10000));
        chart.addLight(new Coord3d(0, 10000, 10000));
        chart.addLight(new Coord3d(10000, 0, 10000));
        chart.addLight(new Coord3d(10000, 10000, 10000));
        chart.getAxisLayout().setMainColor(Color.GRAY);
        chart.getView().setBackgroundColor(Color.BLACK);
        chart.open();
        chart.addMouseCameraController();

        EmulGLSkin skin = EmulGLSkin.on(chart);
        skin.getCanvas().setProfileDisplayMethod(true);
    }
}
