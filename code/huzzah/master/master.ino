#include <Wire.h>
#include "stage.h"
#include "signals.h"

#define WIFI_SSID "***REMOVED***"
#define WIFI_PASS "***REMOVED***"
#define UDP_PORT  4210
#define HOSTNAME  "LSM"

//Wifi setup
IPAddress static_ip(192, 168, 1, 193);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);


Stage stage;
SignalServer server(WIFI_SSID, WIFI_PASS, UDP_PORT);

void cb_test(Command* command)
{
  Serial.println((char*)command);
  command->cmd = 'A';
}

void setup() {
  Serial.begin(115200);
  stage.begin();
  yield();
  WiFi.hostname(HOSTNAME);
  WiFi.config(static_ip, gateway, subnet);
  server.begin();
  server.connect('T', &cb_test);
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
