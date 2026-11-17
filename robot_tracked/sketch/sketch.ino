#include "Arduino_RouterBridge.h"
#include <Wire.h>

const byte I2C_ADDR = 0x34;
const uint8_t MOTOR_TYPE_ADDR = 20;
const uint8_t MOTOR_ENCODER_POLARITY_ADDR = 21;
const uint8_t MOTOR_FIXED_PWM_ADDR = 31;   // Open-loop PWM (-100 to 100)
const uint8_t MOTOR_FIXED_SPEED_ADDR=  51; // Closed-loop speed (-50 to 50)

uint8_t MotorType = 3; 
uint8_t MotorEncoderPolarity = 0; 

byte _wire_transmission(uint8_t reg, uint8_t *val, unsigned int len) {
  Wire.beginTransmission(I2C_ADDR);
  Wire.write(reg);
  for (unsigned int i = 0; i < len; i++) {
    Wire.write(val[i]);
  }
  return(Wire.endTransmission());
}

void move(int8_t m1, int8_t m2, int8_t m3, int8_t m4) {
  int8_t speeds[] = {-m1, -m2, m3, m4};
  
  _wire_transmission(MOTOR_FIXED_SPEED_ADDR, (uint8_t*)speeds, 4);
}

void setup() {
  Serial.begin(115200);

  delay(5000);

  Wire.begin();
  delay(200);

  Wire.beginTransmission(I2C_ADDR);  // ping driver board to verify wiring
  byte error = Wire.endTransmission();
  if (error != 0) {
    Serial.print("[FAIL] Driver not found! I2C error code: ");
    Serial.println(error);
    Serial.println("Check SDA (A4), SCL (A5), GND, and board power.");
    while (1); // halt
  }

  _wire_transmission(MOTOR_TYPE_ADDR, &MotorType, 1);
  delay(5);
  _wire_transmission(MOTOR_ENCODER_POLARITY_ADDR, &MotorEncoderPolarity, 1);
  delay(5);

  Bridge.begin();
  Bridge.provide_safe("move", move);
}

void loop() {
  Serial.println("Running");

  delay(1000);
}
