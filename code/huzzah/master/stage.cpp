#include "Arduino.h"
#include "stage.h"

Stage::Stage()
{
  _currentX = 0;
  _currentY = 0;
}

void Stage::begin()
{
	Wire.begin();
}

int Stage::getX()
{
	return _currentX;
}

int Stage::getY()
{
	return _currentY;
}

void Stage::setX(int newVal)
{
	setDAC(X_AXIS, newVal);
	_currentX = newVal;
}

void Stage::setY(int newVal)
{
	setDAC(Y_AXIS, newVal);
	_currentY = newVal;
}

void Stage::setDAC(int addr, int val)
{
	// Based on code @ https://learn.sparkfun.com/tutorials/mcp4725-digital-to-analog-converter-hookup-guide
	Wire.beginTransmission(addr);// Start I2C cmd:
	Wire.write(64);              // CMD -> update DAC value
	Wire.write(val >> 4);        // the 8 most significant bits...
	Wire.write((val & 15) << 4); // the 4 least significant bits...
	Wire.endTransmission();
}
