//LSM.h V1.1.2

/*-----------------*
       LSM.h
  - - - - - - - - -
   This is an easy
   -to-use library
   to control a
   laser and three
   coils set up as
   an LSM.
  -----------------*/

const bool noramp = true; //No ramping. The LSM software can handle that.


//Variables:
int myx = 0; //Current position of specimen
int myy = 0;

//Constants:
//define pin number constants:
const int boardLed = 13; //The Arduino's on-board LED
const int laser = 4; //The pin controling the laser diode
const int coilp1 = 10; //The H-Bridge motor controller inputs:
const int coilp2 = 3;
const int coilp3 = 9;
const int coilp4 = 11;
const int speaker = 6; // PWM pin for speaker control
const int ldr0 = 0; //The Photoresistor voltage divider circuits
const int ldr1 = 1;
const int thumbX = 2;
const int thumbY = 3;
const int currentsense = 4;

//True and False (For those who do python):
const bool True = false;
const bool False = true;

//define functions:
void initLSM(void);
void setlaser(bool state);
void setLed(bool state);
void place(int x, int y);
void rampPWM(int pin, int current, int target, int rate);
int getLDR(int pin);
int getThumbStick(int axis);
int getx(void);
int gety(void);


int getx(void){
  return myx;
}
int gety(void){
  return myy;
}

void initLSM(void) {
  pinMode(boardLed, OUTPUT);
  pinMode(laser, OUTPUT);
  pinMode(coilp1, OUTPUT);
  pinMode(coilp2, OUTPUT);
  pinMode(coilp3, OUTPUT);
  pinMode(coilp4, OUTPUT);
  digitalWrite(laser, 1); //High is false. Defaults to on.
}

void setLaser(bool state) { //Set Laser State
  digitalWrite(laser, not state);
}

void setLed(bool state) { //Set Laser State
  digitalWrite(boardLed, state);
}

void rampPWM(int pin, int current, int target, int rate) { //low-level function to simply bring an axis to its position slowly, as to increase the lifespan of the CD read/write head
  while (abs(current - target) > (rate * 2)) {
    delay((10 / rate));
    if (current > target) {
      current = current - rate;
    }
    else {
      current = current + rate;
    }
    analogWrite(pin, current);
  }
  analogWrite(pin, target); //If it is a few off, we bring it back over
}

void place(int x, int y) {
 if((abs(myx-x)<10) || noramp){ //No ramping, just setpos
   if (x >= 0) {
     myx = x;
     analogWrite(coilp2, 0);
     analogWrite(coilp1, (x)); //PWM
   }
   else {
     myx = x;
     analogWrite(coilp1, 0);
     analogWrite(coilp2, abs(x)); //PWM in the other direction
   }
 }
 else {
    if (x >= 60) {
     rampPWM(coilp2, myx, 0, 4);
     rampPWM(coilp1, myx, x, 4);
     myx = x;
     analogWrite(coilp2, 0);
     analogWrite(coilp1, (x)); //PWM
   }
   else { //A little ways away, let's ramp it.
     rampPWM(coilp1, myx, 0, 4);
     rampPWM(coilp2, myx, x, 4);
     myx = x;
     analogWrite(coilp1, 0);
     analogWrite(coilp2, abs(x)); //PWM in the other direction
   }
 }
 if((abs(myy-y)<60) || noramp){ //No ramping, just setpos
   if (y >= 0) {
     myy = y;
     analogWrite(coilp4, 0);
     analogWrite(coilp3, y); //PWM
   }
   else {
     myy = y;
     analogWrite(coilp3, 0);
     analogWrite(coilp4, abs(y)); //PWM in the other direction
   }
 }
 else {
    if (y >= 0) {
     rampPWM(coilp4, myy, 0, 4);
     rampPWM(coilp3, myy, y, 4);
     myy = y;
     analogWrite(coilp4, 0);
     analogWrite(coilp3, (y)); //PWM
   }
   else { //A little ways away, let's ramp it.
     rampPWM(coilp3, myy, 0, 4);
     rampPWM(coilp4, myy, abs(y), 4);
     myy = y;
     analogWrite(coilp3, 0);
     analogWrite(coilp4, abs(y)); //PWM in the other direction
   }
 }

}
int getLDR(int pin) {
  return analogRead(pin);
}

void setspeaker(int val) {
  analogWrite(speaker, val);
}

int getThumbStick(int axis) {
  return analogRead(axis);
}
