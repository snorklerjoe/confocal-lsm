package com.hosticlefifer.lsm_control.data_handling;

/**
 * Defines a <a href="https://youtu.be/A05n32Bl0aY?t=11">vector</a>, "with both direction, and magnitude, oh yeah, oh yeah!"
 * (Mostly just used as the normal for a plane, with the "magnitude" being the position of the plane in the direction of the normal)
 */
public class Vector {
    Axis direction;
    int magnitude;

    public Vector(Axis direction, int magnitude) {
        this.direction = direction;
        this.magnitude = magnitude;
    }

    public Axis getDirection() {
        return direction;
    }

    public void setDirection(Axis direction) {
        this.direction = direction;
    }

    public int getMagnitude() {
        return magnitude;
    }

    public void setMagnitude(int magnitude) {
        this.magnitude = magnitude;
    }

    public void setPosition(int position) {
        this.magnitude = position;
    }
}
