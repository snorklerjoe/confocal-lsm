/**
 * signals.h
 * Easy slot/signal server for receiving commands from the Java controller program
 */
#ifndef SIGNALS_H
#define SIGNALS_H

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include "Arduino.h"

typedef struct Command {
  uint8_t cmd;
  uint16_t a;
  uint16_t x;
  uint16_t y;
  uint16_t z;
} Command;

class SignalServer
{
  public:
    SignalServer(const char * ssid, const char * pass, int localport);
    void begin();
    void connect(int cmdNo, void (*callback)(Command* commandToProcess));
    void loop();
  private:
    const char * _wifi_ssid;
    const char * _wifi_pass;
    int _port;
    void (*_callbacks[64])(Command* commandToProcess);
    uint8_t _commands[64];
    int _numCommands;
    char _packet[255];
};


#endif
