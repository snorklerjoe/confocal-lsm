#include <Wire.h>
#include "stage.h"
#include "signals.h"

#define WIFI_SSID "***REMOVED***"
#define WIFI_PASS "***REMOVED***"
#define UDP_PORT  4210
#define HOSTNAME  "LSM"

#define TIME_PRECISION_US 100  // The precision of time in related operations (in us, hence the name)

//Wifi setup
IPAddress static_ip(192, 168, 1, 193);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);


Stage stage;
SignalServer server(WIFI_SSID, WIFI_PASS, UDP_PORT);
int currentZ = 0;

int compare(int num1, int num2) {
  if(num1 > num2) {
    return -1;
  }
  if(num2 > num1) {
    return 1;
  }
  return 0;
}

void setStage(Command* command)
{
  if(command->x > STAGE_MAX_COORD)
    command->x = STAGE_MAX_COORD;
  if(command->y > STAGE_MAX_COORD)
    command->y = STAGE_MAX_COORD;
  if(command->z > 1024)
    command->z = 1024;
  unsigned long startOfCommand = millis();
  while(stage.getX() != command->x || stage.getY() != command->y || currentZ != command->z) {
    unsigned long start = micros();
    stage.setPosition(stage.getX()+compare(stage.getX(), command->x), stage.getY()+compare(stage.getY(), command->y));
    currentZ += compare(currentZ, command->z);
    analogWrite(15, currentZ);
    while((micros() - start) < (unsigned long)command->a)  // Accurate time wait
      delayMicroseconds(TIME_PRECISION_US);
    if(millis()-startOfCommand > 500) {                    // Don't let the thing crash...
        yield();
        start = millis();
    }
  }
  command->cmd = 'A';
  command->z = 0;
}

void rapidSetStage(Command* command)
{
  stage.setPosition(command->x, command->y);
  currentZ = command->z;
  analogWrite(15, command->z);
  command->cmd = 'A';
}

void readADC(Command* command)
{
  //Serial.println(command->a);
  while (Serial.available() > 0) Serial.read();
  Serial.write(command->a%256);
  command->a = Serial.parseInt();
  command->cmd = 'A';
  command->x = stage.getX();
  command->y = stage.getY();
  command->z = currentZ;
}

void setIo(Command* command)
{
  pinMode(command->x, OUTPUT);
  digitalWrite(command->x, command->a);
  command->cmd = 'A';
  command->x = stage.getX();
  command->y = stage.getY();
  command->z = currentZ;
}

void pause(Command* command)
{
  delay(command->a);
  command->cmd = 'A';
  command->x = stage.getX();
  command->y = stage.getY();
  command->z = currentZ;
}

void setup() {
  Serial.begin(115200);
  stage.begin();
  yield();
  WiFi.hostname(HOSTNAME);
  WiFi.config(static_ip, gateway, subnet);
  server.begin();
  server.connect('S', &setStage);
  server.connect('R', &rapidSetStage);
  server.connect('V', &readADC);
  server.connect('O', &setIo);
  server.connect('D', &pause);
}

void loop() {
  yield();
  server.loop();
  /*for(int i=0; i < 4096; i++)
  {
    stage.setX(i);
    stage.setY(i);
    delay(1);
  }
  for(int i=4095; i > 0; i--)
  {
    stage.setX(i);
    stage.setY(i);
    delay(1);
  }*/
}
