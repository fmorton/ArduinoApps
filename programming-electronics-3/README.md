# Project 3 \- Video Boo

You are working with your colleague Dave on an application for BigBoo Scary Town Inc.  They sell products to companies that run haunted houses.  

They want a device that will analyze a video stream for specific objects, and then trigger an action depending on the object.  

While currently in the prototyping phase, the basic idea is to “customize” a haunted house experience by giving a specific object to a person as they walk through a haunted house allowing for different things to be triggered.

Dave and you have decided to use the Arduino Q again, because of the pre-built Video Object Detection Brick in AppLab which allows a developer to quickly add video stream object detection functionality.  

He has already written a program that can identify a person in a video stream and triggers a buzzer on the MCU.

He has asked you to finish the project, by adding “cup” detection which will trigger an LED to flash.

Dave let you know the demo is tomorrow morning with the CEO of BigBoo.  He also produced some fake sounding coughs, mentioned he wasn’t feeling well, and that you needed to be sure you could give a solid brief on the project.

## Your Tasks:

For all coding tasks below, look for comment sections that direct you where to write your code.

1. Set up your Arduino Q with a USB dongle and USB Camera.  
2. Ensure your Arduino Q is connected to your local WiFi network.   
3. Create a simple piezo buzzer circuit on pin A3, and an LED circuit on pin D6.  
4. On another workstation where you have AppLab installed, open AppLab, and connect to the board via Network mode.  
5. In the Arduino Sketch, **provide\_safe** a function named `flashLED` that will rapidly turn an LED on and off 10 times.  
6. In the Arduino Sketch, **write the function** referred to in the previous step.  The function returns no values, takes no parameters: it simply blinks an LED 10 times.  Make sure to add a pin number for the LED.  
7. In the Python file, ensure the **General purpose object detection \- YoloX** AI model tagged as IN USE, by clicking the Video Object Detection brick in the file explorer, and checking the AI Models tab.  
8. In the Python file, add an additional `video_detector.on_detect()` call that will identify “cup” and trigger a function named `cup_detected`.    
9. In the Python file, write the callback function `cup_detected`.  The function returns no values, takes no parameters: it **notifies** the MCU function created in the previous steps.

## Notes:

You *could* complete this work order in SBC mode entirely, however you would need to add a keyboard and mouse to your Arduino Q.  Network mode is the preferred option.

Take some time and look at the Overview, Usage examples, API Documentation, and AI Models tabs in the Video Object Detection Brick.

## Testing Criteria:   

Once completed with these tasks, you can check your work by ensuring the following while the App is running: 

* When a person is in front of the USB camera, the piezo makes noise.  The noise should stop, and begin again after 10 seconds if a person is still in view.  
* When a cup is in front of the camera, the LED blinks rapidly 10 times. The blinking should stop, and begin again after 10 seconds if a cup is still in view.  
* If a person or cup is not in view of the USB camera, no beeping or blinking should happen.  
* No errors in the AppLab consoles