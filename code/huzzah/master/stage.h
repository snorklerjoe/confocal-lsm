/**
 * stage.h
 * Easy control over each axis via 2 MCP4725 DACs
 */
#ifndef AXIS_H
#define AXIS_H

#include "Arduino.h"
#include <Wire.h>

#define X_AXIS 0x60
#define Y_AXIS 0x61

#define STAGE_MAX_COORD 4095

class Stage
{
  public:
    Stage();
    void begin();
    int getX();
    int getY();
    void setX(int newVal);
    void setY(int newVal);
  private:
    int _currentX;
    int _currentY;
    static void setDAC(int addr, int val);
};


#endif
