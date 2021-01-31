int buf;

void setup() {
  Serial.begin(115200);
}

void loop() {
  while(!Serial.available());
  buf = analogRead(Serial.read());
  Serial.println(buf);
  //Serial.write(buf >> 8);
  //Serial.write(buf && 0xFF);
}
