/**** INCLUDES *********************/
#include <Arduino_RouterBridge.h>

/**** CONSTANTS ********************/
const byte SENSOR_1_PIN = A0;
const byte SENSOR_2_PIN = 5;

/**************************************/
/** ADD PIN NUMBERS AS REQUIRED BELOW */
/*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/


/*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
/** ADD PIN NUMBERS AS REQUIRED ABOVE */
/**************************************/

/**** FUNCTIONS ********************/

// Read analog sensor on A1 (returns 0-1023)
int readSensor_1() 
{
  return analogRead(SENSOR_1_PIN);
}

// Read digital sensor on D5 (returns 0 or 1)
int readSensor_2() 
{ 
  return digitalRead(SENSOR_2_PIN);
}

/**************************************/
/** ADD SENSOR READING FUNCTION BELOW */
/*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/


/*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
/** ADD SENSOR READING FUNCTION ABOVE */
/**************************************/

/**** SETUP ************************/
void setup() 
{
  pinMode(SENSOR_2_PIN, INPUT);
  
  Bridge.begin();
  Bridge.provide_safe("readSensor_1", readSensor_1);
  Bridge.provide_safe("readSensor_2", readSensor_2);

  /************************************/
  /** ADD FUNCTION PROVIDE CODE BELOW */
  /*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/
  
  
  /*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
  /** ADD FUNCTION PROVIDE CODE ABOVE */
  /************************************/
}

/**** LOOP *************************/
void loop() 
{

}