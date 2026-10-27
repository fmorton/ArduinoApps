# Project 1 \- Bridge Builders

You are working with a colleague (Dave) to develop a simple proof of concept application for a meat packing company.

The company is building a new line of conveyor systems that integrates what used to be two separate steps in the meat packing operation.

They need sensor data to be collected and displayed to Quality Control Technicians.  

The data needs to be presented in a tab on a browser window, so that the technicians can switch between the sensor data view, and another web application the company maintains internally for reporting.

You and Dave have decided to use the Arduino Q family of boards because it allows you to run a Linux environment alongside a microcontroller that can be used to perform sensor readings.

Dave (your colleague) has already developed a simple “Sensor Data View” for the browser using the Streamlit UI brick available in Arduino AppLab.

Your job is to build the bridge between the microcontroller and microprocessor, so that sensor data collected from the microcontroller can be displayed on a web browser that is running on the microprocessor.

## Your tasks:

1. Ensure that the appropriate code library necessary for bridge communication is **added** to the AppLab App for the arduino sketch.  
2. Ensure that the Arduino sketch **includes** the library added above.  
3. Ensure that the Python file **imports** the proper module for bridge communication.  
4. Ensure the Arduino sketch **begins** bridge communication.  
5. Ensure the Arduino sketch **provides** a function named `readSensor_1` that accepts no arguments, but returns a sensor reading in numeric form.  Any sensor is fine.  For example, simply using analogRead() with a potentiometer would fulfill the requirement.  Creating the pin numbers is implicit in this requirement.

## Notes:

You own the Arduino sketch.  Your only non-negotiable requirement is making sure to provide a function with the name `readSensor_1`.  The pin number, the sensor type, and all the other details are decided by you.  
You DO NOT own the Python file.

There is a single import that needs to be added to the Python file, otherwise, do not change it.

      