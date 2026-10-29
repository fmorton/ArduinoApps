#include <Arduino_RouterBridge.h>

const byte PIEZO_PIN = A3;
const int LED_PIN = 6;

void makeNoise() {
  byte num_beeps = 10;
  for(int i = 0; i < num_beeps; i++)   {
    tone(PIEZO_PIN, 400,100);
    delay(200);
  }
}

void flashLED() {
  byte num_flashes = 10;
  for(int i = 0; i < num_flashes; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }
}

void bothThings(int count) {
  for(int i = 0; i < count; i++)   {
    tone(PIEZO_PIN, 400,100);
    digitalWrite(LED_PIN, HIGH);
    delay(200);
    digitalWrite(LED_PIN, LOW);
    delay(200);
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);

  Bridge.begin();
  Bridge.provide_safe("makeNoise", makeNoise);
  Bridge.provide_safe("flashLED", flashLED);
  Bridge.provide_safe("bothThings", bothThings);
}

void loop() {
}