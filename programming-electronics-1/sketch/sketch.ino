#include <Arduino_RouterBridge.h>

const int sensor = A0;

int readSensor() {
  return(analogRead(sensor));
}

void setup() {
  Serial.begin(115200);

  delay(1000);

  Bridge.begin();
  Bridge.provide_safe("readSensor", readSensor);
}

void loop() {
  Serial.println(analogRead(sensor));

  delay(1000);
}
