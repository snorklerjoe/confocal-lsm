#include "Arduino.h"
#include "signals.h"

WiFiUDP UDP;

SignalServer::SignalServer(const char * ssid, const char * pass, int localport) {
  //strcpy(_wifi_ssid, ssid);
  //strcpy(_wifi_pass, pass);
  _wifi_ssid = ssid;
  _wifi_pass = pass;
  _port = localport;
  _numCommands = 0;
}

void SignalServer::begin()
{
  WiFi.begin(_wifi_ssid, _wifi_pass);
  // Connecting to WiFi...
  Serial.print("Connecting to ");
  Serial.print(_wifi_ssid);
  // Loop continuously while WiFi is not connected
  while (WiFi.status() != WL_CONNECTED)
  {
    yield();
    delay(100);
    Serial.print(".");
  }
  Serial.print("\nConnected! IP address: ");
  Serial.println(WiFi.localIP());
  UDP.begin(_port);
}

void SignalServer::connect(int cmdNo, void (*callback)(Command* commandToProcess))
{
  _commands[_numCommands] = cmdNo;
  _callbacks[_numCommands] = callback;
  _numCommands++;
}

void SignalServer::loop()
{
  int packetSize = UDP.parsePacket();
  if(packetSize)
  {
    int len = UDP.read(_packet, 255);
    if(len > 0)
    {
      _packet[len] = '\0';
    }
    Command* recCommand = (Command*) _packet;
    Serial.println(recCommand->cmd);

    //Command* reply = (Command*) (const char *)"E\0\0\0\0\0\0\0\0"; // = {(uint8_t) 'E', (uint16_t) 255, (uint16_t) 255, (uint16_t) 255, (uint16_t) 255};
    //reply->cmd = 'E';
    
    for(int i = 0; i < _numCommands; i++)
    {
      if(_commands[i] == recCommand->cmd)
      {
      (*_callbacks[i])(recCommand);
      }
    }
    Serial.println(recCommand->cmd);
    
    // Reply:
    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());
    UDP.write(*(char*)recCommand);
    UDP.endPacket();
  }
}
