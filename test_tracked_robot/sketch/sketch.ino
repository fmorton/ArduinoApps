#include <Wire.h>

#define I2C_ADDR 0x34

// Hiwonder Driver Register Addresses
#define MOTOR_TYPE_ADDR 20
#define MOTOR_ENCODER_POLARITY_ADDR 21
#define MOTOR_FIXED_PWM_ADDR 31   // Open-loop PWM (-100 to 100)
#define MOTOR_FIXED_SPEED_ADDR 51 // Closed-loop speed (-50 to 50)

// Motor configuration (3 = JGB37-520 motors; use 1 for TT or 2 for N20)
uint8_t MotorType = 3; 
uint8_t MotorEncoderPolarity = 0; 

// Helper function to write a byte array to a specific I2C register and print I2C status
void WireWriteDataArray(uint8_t reg, uint8_t *val, unsigned int len) {
  Wire.beginTransmission(I2C_ADDR);
  Wire.write(reg);
  for (unsigned int i = 0; i < len; i++) {
    Wire.write(val[i]);
  }
  byte status = Wire.endTransmission();

  if (status != 0) {
    Serial.print("  [I2C ERROR] Write to register ");
    Serial.print(reg);
    Serial.print(" failed with code: ");
    Serial.println(status);
  }
}

// Helper function to set closed-loop speeds for [M1, M2, M3, M4]
void setTrackSpeeds(int8_t m1, int8_t m2, int8_t m3 = 0, int8_t m4 = 0) {
  int8_t speeds[] = {-m1, -m2, m3, m4};
  Serial.print("  -> Sending speeds [");
  Serial.print(m1); Serial.print(", ");
  Serial.print(m2); Serial.print(", ");
  Serial.print(m3); Serial.print(", ");
  Serial.print(m4); Serial.println("]");
  
  WireWriteDataArray(MOTOR_FIXED_SPEED_ADDR, (uint8_t*)speeds, 4);
}

void setup() {
  Serial.begin(9600);
  while (!Serial) {
    ; // Wait for Serial Monitor to connect on boards with native USB
  }
  delay(10000);

  Serial.println("=== Starting Tracked Vehicle Sequence ===");
  Wire.begin();
  delay(200);

  // 0. Ping driver board to verify wiring
  Serial.println("Step 0: Checking I2C connection at 0x34...");
  Wire.beginTransmission(I2C_ADDR);
  byte error = Wire.endTransmission();
  if (error == 0) {
    Serial.println("  [OK] Hiwonder driver board detected!");
  } else {
    Serial.print("  [FAIL] Driver not found! I2C error code: ");
    Serial.println(error);
    Serial.println("  Check SDA (A4), SCL (A5), GND, and board power.");
    while (1); // Halt execution so you can fix wiring
  }

  // 1. Configure motor type and encoder polarity
  Serial.println("Step 1: Configuring MotorType and EncoderPolarity...");
  WireWriteDataArray(MOTOR_TYPE_ADDR, &MotorType, 1);
  delay(5);
  WireWriteDataArray(MOTOR_ENCODER_POLARITY_ADDR, &MotorEncoderPolarity, 1);
  delay(5);
  Serial.println("  [OK] Configuration sent.");

  // 2. Drive Forward
  Serial.println("Step 2: Driving FORWARD for 2 seconds...");
  setTrackSpeeds(25, 25);
  delay(2000);

  // 3. Brief pause
  Serial.println("Step 3: Pausing for 0.5 seconds...");
  setTrackSpeeds(0, 0);
  delay(500);

  // 4. Pivot Turn Right
  Serial.println("Step 4: Turning RIGHT in place for 1.5 seconds...");
  setTrackSpeeds(25, 0);
  delay(1500);

  // 5. Drive Forward again
  Serial.println("Step 5: Driving FORWARD for 2 seconds...");
  setTrackSpeeds(-25, -25);
  delay(2000);

  // 6. Final Stop
  Serial.println("Step 6: Stopping motors...");
  setTrackSpeeds(0, 0, 0, 0);
  Serial.println("=== Sequence Complete. Robot Stopped. ===");
}

void loop() {
  // Empty so the sequence runs once and stops
}
