#include <Arduino_RouterBridge.h>

const byte PIEZO_PIN = A3; 

/*************************************************************
This function expects a vector of vectors.
The inner vectors are of form (frequency, duration, interval)

Example: ((880,50,10),(440,50,10),(880,50,10),(294,400,0))
*************************************************************/
void playSounds(MsgPack::arr_t<MsgPack::arr_t<int>> notes) {
  for(const auto& note : notes){

      int frequency = note[0];
      int duration = note[1];
      int interval = note[2];
      Serial.println("---------------------------------------");
      Serial.println(frequency);
      Serial.println(duration);
      Serial.println(interval);
      tone(PIEZO_PIN, frequency, duration);
      delay(duration + interval);
  }
}

void setup() {
  Serial.begin(115200);

  delay(1000);

  Bridge.begin();
  Bridge.provide_safe("playSounds", playSounds);
}

void loop() {
}
