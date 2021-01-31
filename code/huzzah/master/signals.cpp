#include "Arduino.h"
#include "signals.h"

WiFiUDP UDP;
Command recCommand;

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
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
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
    int len = UDP.read(_packet, sizeof(_packet));
    if(len > 0)
    {
      _packet[len] = '\0';
    }

    for(int i = 0; i < min(BULKSIZE*9, len); i += 10) {
      memcpy(&recCommand, &(_packet[i]), 10);
  
      //Command* reply = (Command*) (const char *)"E\0\0\0\0\0\0\0\0"; // = {(uint8_t) 'E', (uint16_t) 255, (uint16_t) 255, (uint16_t) 255, (uint16_t) 255};
      //reply->cmd = 'E';
      
      for(int j = 0; j < _numCommands; j++)
      {
        if(_commands[j] == recCommand.cmd)
        {
          digitalWrite(LED, HIGH);
          (*_callbacks[j])(&recCommand);
          break;
        }
      }
      memcpy(&_resultBuf[i], &recCommand, 10);
      yield();
    }
    
    // Reply:
    //Serial.println("Responding...");
    UDP.beginPacket(UDP.remoteIP(), UDP.remotePort());
    UDP.write(&_resultBuf[0], len);
    UDP.endPacket();
    digitalWrite(LED, LOW);
  }
}
