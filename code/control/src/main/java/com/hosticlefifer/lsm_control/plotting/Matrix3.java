package com.hosticlefifer.lsm_control.plotting;

import com.hosticlefifer.lsm_control.data_handling.DataPoint;

/**
 * From: http://blog.rogach.org/2015/08/how-to-create-your-own-simple-3d-render.html
 */
class Matrix3 {
    double[] values;
    Matrix3(double[] values) {
        this.values = values;
    }
    Matrix3 multiply(Matrix3 other) {
        double[] result = new double[9];
        for (int row = 0; row < 3; row++) {
            for (int col = 0; col < 3; col++) {
                for (int i = 0; i < 3; i++) {
                    result[row * 3 + col] +=
                            this.values[row * 3 + i] * other.values[i * 3 + col];
                }
            }
        }
        return new Matrix3(result);
    }

    /**
     * Altered to work with DataPoint objects
     * @param in DataPoint to transform
     * @return The transformed datapoint
     */
    DataPoint transform(DataPoint in) {
        return new DataPoint(
                in.getX() * values[0] + in.getY() * values[6] + in.getZ() * values[3],
                in.getX() * values[1] + in.getY() * values[7] + in.getZ() * values[4],
                in.getX() * values[2] + in.getY() * values[8] + in.getZ() * values[5],
                in.getMeasurement(), in.getType()
        );
    }
}
