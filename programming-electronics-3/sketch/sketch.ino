/**** INCLUDES *********************/
#include <Arduino_RouterBridge.h>


/**** CONSTANTS ********************/
const byte PIEZO_PIN = A3;

/**********************************************/
/** ADD PIN NUMBER(S) AS REQUIRED CODE BELOW **/
/*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/


/*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
/** ADD PIN NUMBERS AS REQUIRED CODE ABOVE ****/
/**********************************************/

/**** FUNCTIONS ********************/

/* Plays beeps from attached piezo buzzer */
void makeNoise() 
{
  byte num_beeps = 10;
  for(int i = 0; i < num_beeps; i++) 
  {
    tone(PIEZO_PIN, 400,100);
    delay(200);
  }
}

/************************************************/
/** ADD FUNCTION CODE BELOW *********************/
/*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/


/*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
/** ADD FUNCTION CODE ABOVE *********************/
/************************************************/

/**** SETUP ************************/
void setup() 
{
  pinMode(LED_PIN, OUTPUT);

  Bridge.begin();
  Bridge.provide_safe("makeNoise", makeNoise);
  
  
  /************************************************/
  /** ADD BRIDGE CODE BELOW ***********************/
  /*⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇*/
  
  
  
  /*⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆*/
  /** ADD BRIDGE CODE ABOVE ***********************/
  /************************************************/
}

/**** LOOP *************************/
void loop() {
}