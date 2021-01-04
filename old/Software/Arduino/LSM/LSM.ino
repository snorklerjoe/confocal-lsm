#include "LSM.h"
#include "WString.h"

bool laserval, LEDval;
char data[64];
char buf;
int tx,ty,tz;

void setup() {
  laserval=false;
  LEDval=false;
  initLSM();
  Serial.begin(115200);
  Serial.setTimeout(5); //Otherwise, it is WICKED slow! (default means each serial read takes 1 second!)
  setLaser(false);
  //Serial.println("LSM is booted up!");
}

void loop() {
  if(Serial.available()){
    Serial.readString().toCharArray(data, 64);
    //Serial.println(data);
    if(String(data).equals(String("Laser on\n"))){
      Serial.println("Yup.");
      setLaser(true);
    }
    if(String(data).equals(String("Laser off\n"))){
      Serial.println("Yup.");
      setLaser(false);
    }

    if(String(data).equals(String("TEST\n"))){
      Serial.println("OK.");
    }
    
    if(String(data).equals(String("Current\n"))){
      Serial.println((analogRead(currentsense)));
    }
    
    if(sscanf(data, "(%i,%i,%i)\n", &tx, &ty, &tz)==3){
      //Serial.println("Setting Y/Z position...");
      place(ty, tz); //Set Y and Z (focus) by PWMing the H-bridge motor controller that moves the CD RW head.
      //Serial.println("Setting X position...");
      setspeaker(tx); //Set the X by PWMing the 2N2222As/low pass filter circuit that controls the speaker. 
      Serial.println("Done!");
    }
    /*if(String(data).equals(String("JOY\n"))){
      Serial.println(String(analogRead(2))+" "+String(analogRead(3)));
    }*/
    if(String(data).equals(String("GETPOS\n"))){
      Serial.println(String(getx())+" "+String(gety()));
    }
    /*if(String(data).equals(String("LDR\n"))){
      delay(100);
      Serial.println(String(getLDR(ldr0))+" "+String(getLDR(ldr1)));
    }*/
  }
}
