void setup() {
  Serial.begin(115200);
}

void loop() {
  while(!Serial.available());
  Serial.println(Serial.read());
}
