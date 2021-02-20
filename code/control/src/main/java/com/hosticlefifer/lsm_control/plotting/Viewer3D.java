package com.hosticlefifer.lsm_control.plotting;

import com.hosticlefifer.lsm_control.data_handling.Axis;
import com.hosticlefifer.lsm_control.data_handling.DataPoint;
import com.hosticlefifer.lsm_control.data_handling.DataPointType;
import com.hosticlefifer.lsm_control.data_handling.Scan;

import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.xml.crypto.Data;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Ellipse2D;
import java.util.ArrayList;

/**
 * A 3D-Viewer, based on the ui used here: http://blog.rogach.org/2015/08/how-to-create-your-own-simple-3d-render.html
 */
public class Viewer3D {
    private ArrayList<DataPoint> dataPoints;
    private double scale, wScale;
    private int fov, fovZ;
    private JPanel renderPanel = new JPanel();

    public Viewer3D(ArrayList<DataPoint> points, int fov, int fovZ) {
        dataPoints = points;
        this.fov = fov;
        this.fovZ = fovZ;
    }

    public Viewer3D(Scan points, int fov, int fovZ) {
        if(points != null) {
            dataPoints = points.getDataPoints();
        } else
            dataPoints = new ArrayList<>();
        this.fov = fov;
        this.fovZ = fovZ;
    }

    public void setPoints(Scan points) {
        dataPoints = points.getDataPoints();
    }

    /**
     * Normalizes the magnitudes for display, between 0 and newMax
     * @param newMax The maximum magnitude present after the normalization
     */
    public void normalizeMagnitude(int newMax) {
        int curMax = 0;
        int curMin = 1000000;  // TODO: Remove arbitrary constant
        wScale = newMax;
        for(DataPoint point : dataPoints) {
            if (point.getMeasurement() > curMax)
                curMax = point.getMeasurement();
            if (point.getMeasurement() < curMin)
                curMin= point.getMeasurement();
        }
        final double scaleFactor = (double)newMax / curMax;
        for(DataPoint point : dataPoints)
            point.scaleMeasurement(scaleFactor, -curMin);
    }

    /**
     * Shows the data in a new window.
     */
    public void show(final Color color) {
        JFrame frame = new JFrame();
        Container pane = frame.getContentPane();
        pane.setLayout(new BorderLayout());

        // Horizontal/vertical rotation:
        final JSlider headingSlider = new JSlider(180, 360+180, 360-45);
        final JSlider pitchSlider = new JSlider(SwingConstants.VERTICAL,0, 360, 180-45);
        pane.add(headingSlider, BorderLayout.SOUTH);
        pane.add(pitchSlider, BorderLayout.EAST);

        final int[] xOffset = {0};
        final int[] yOffset = {0};
        final double[] originX = {0};
        final double[] originY = {0};

        renderPanel = new JPanel() {
            public void paintComponent(Graphics g) {
                Graphics2D g2 = (Graphics2D) g;
                g2.setColor(Color.BLACK);
                g2.fillRect(0, 0, getWidth(), getHeight());
                g2.setColor(color);

                double min = 0;
                for(DataPoint point : dataPoints)
                    if(point.getX() < min || point.getY() < min || point.getZ() < min)
                        min = Math.min(Math.min(point.getX(), point.getY()), -point.getZ());
                min -= 10;

                // From http://blog.rogach.org/2015/08/how-to-create-your-own-simple-3d-render.html
                double heading = Math.toRadians(headingSlider.getValue());
                Matrix3 headingTransform = new Matrix3(new double[] {
                        Math.cos(heading), 0, -Math.sin(heading),
                        0, 1, 0,
                        Math.sin(heading), 0, Math.cos(heading)
                });
                double pitch = Math.toRadians(pitchSlider.getValue());
                Matrix3 pitchTransform = new Matrix3(new double[] {
                        1, 0, 0,
                        0, Math.cos(pitch), Math.sin(pitch),
                        0, -Math.sin(pitch), Math.cos(pitch)
                });
                Matrix3 transform = headingTransform.multiply(pitchTransform);
                //double angleCurr, r, x, y;
                // Render static lines:
                double x, y, x1, y1;
                g2.setColor(Color.WHITE);
                x = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                x1 = transform.transform(new DataPoint(fov, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y1 = transform.transform(new DataPoint(fov, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                g2.drawLine((int)x, (int)y, (int)x1, (int)y1);
                originX[0] = x;
                originY[0] = y;
                x = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                x1 = transform.transform(new DataPoint(0, fov, 0, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y1 = transform.transform(new DataPoint(0, fov, 0, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                g2.drawLine((int)x, (int)y, (int)x1, (int)y1);
                x = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y = transform.transform(new DataPoint(0, 0, 0, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                g2.fill((Ellipse2D.Double) new Ellipse2D.Double(x*Math.exp(scale), y*Math.exp(scale), 10, 10));
                x1 = transform.transform(new DataPoint(0, 0, fovZ, (int)wScale, DataPointType.CONFOCAL)).getX()*Math.exp(scale)-min-xOffset[0];
                y1 = transform.transform(new DataPoint(0, 0, fovZ, (int)wScale, DataPointType.CONFOCAL)).getZ()*-1*Math.exp(scale)-min-yOffset[0];
                g2.drawLine((int)x, (int)y, (int)x1, (int)y1);


                // Render data:
                for(DataPoint point : dataPoints) {
                    double colorScale = point.getMeasurement()/wScale;
                    try {
                        g2.setColor(new Color((int) (color.getRed() * colorScale), (int) (color.getGreen() * colorScale), (int) (color.getBlue() * colorScale)));
                    } catch(IllegalArgumentException e) {
                        g2.setColor(Color.WHITE);
                    }
                    x = transform.transform(point).getX();  // TODO: Rendering could be more efficient!
                    y = transform.transform(point).getZ()*-1;
                    g2.fill((Ellipse2D.Double) new Ellipse2D.Double(x*Math.exp(scale)-min-xOffset[0], y*Math.exp(scale)-min-yOffset[0], point.getMeasurement(), point.getMeasurement()));
                }
            }
        };

        // Zoom:
        renderPanel.addMouseWheelListener(new MouseWheelListener() {
            @Override
            public void mouseWheelMoved(MouseWheelEvent mouseWheelEvent) {
                scale += 0.3 * -mouseWheelEvent.getWheelRotation();
                if(mouseWheelEvent.getWheelRotation() < 0) {
                    xOffset[0] -= ((int)originX[0] - mouseWheelEvent.getX())/2;
                    yOffset[0] -= ((int)originY[0] - mouseWheelEvent.getY())/2;
                }
                else {
                    xOffset[0] += ((int)originX[0] - mouseWheelEvent.getX())/2;
                    yOffset[0] += ((int)originY[0] - mouseWheelEvent.getY())/2;
                }
                System.out.println("Scale: " + scale);
                renderPanel.updateUI();
            }
        });

        headingSlider.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent changeEvent) {
                renderPanel.updateUI();
            }
        });

        pitchSlider.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent changeEvent) {
                renderPanel.updateUI();
            }
        });

        renderPanel.addMouseListener(new MouseListener() {
            private int x = 0;
            private int y = 0;
            MouseMotionListener dragListener = new MouseMotionListener() {
                @Override
                public void mouseDragged(MouseEvent mouseEvent) {
                    if((mouseEvent.getModifiersEx() & (MouseEvent.BUTTON2_DOWN_MASK | MouseEvent.BUTTON1_DOWN_MASK)) == MouseEvent.BUTTON1_DOWN_MASK) {
                        headingSlider.setValue(headingSlider.getValue() + mouseEvent.getX() - x);
                        pitchSlider.setValue(pitchSlider.getValue() + mouseEvent.getY() - y);
                    }
                    else {
                        xOffset[0] -= (mouseEvent.getX() - x);
                        yOffset[0] -= (mouseEvent.getY() - y);
                        System.out.println("Offset: " + xOffset[0] + ", " + yOffset[0]);
                        renderPanel.updateUI();
                    }
                    x = mouseEvent.getX();
                    y = mouseEvent.getY();
                }

                @Override
                public void mouseMoved(MouseEvent mouseEvent) {

                }
            };

            @Override
            public void mouseClicked(MouseEvent mouseEvent) {

            }

            @Override
            public void mousePressed(MouseEvent mouseEvent) {
                x = mouseEvent.getX();
                y = mouseEvent.getY();
                renderPanel.addMouseMotionListener(dragListener);
            }

            @Override
            public void mouseReleased(MouseEvent mouseEvent) {
                //headingSlider.setValue(headingSlider.getValue() + mouseEvent.getX() - x);
                //pitchSlider.setValue(pitchSlider.getValue() + mouseEvent.getY() - y);
                //renderPanel.removeMouseMotionListener(dragListener);
            }

            @Override
            public void mouseEntered(MouseEvent mouseEvent) {

            }

            @Override
            public void mouseExited(MouseEvent mouseEvent) {

            }
        });

        pane.add(renderPanel, BorderLayout.CENTER);

        try {
            frame.setTitle(((dataPoints.get(0).getType() == DataPointType.CONFOCAL) ? "CLSM" : "TLSM") + " Image Acquisition");
        } catch(IndexOutOfBoundsException e) {
            frame.setTitle("LSM Image Acquisition");
        }
        frame.setSize(400, 400);
        frame.setVisible(true);
    }

    public void refresh() {
        renderPanel.updateUI();
    }
}
