# Project 4 \- Cave Database

Your employer has been hired by a mining company to prototype a mineshaft entrance monitor.  Your colleague Dave is the lead on the project, and has chosen you to assist him.

The device you prototype needs to store three different sensor values into a database as well as display the last 10 minutes of data via a web browser application.  Data retention past 1 day is not necessary.

The device itself will be installed at the opening of the mine shaft. The data will be displayed over the network at the foreman's trailer which is within wifi range of the device. 

Dave decided to use an Influx Database Brick for storing the time-series data, and the Streamlit UI Brick for displaying charts.

You have been tasked with finishing up the project.

Dave's Python code already includes everything needed for two sensors: writing readings to the database, querying them back out, and rendering them as charts. You'll be following the existing patterns to add the third.

## Your tasks:

For all coding tasks below, look for comment sections that direct you where to write your code.  
**Also, follow suit with the naming and design convention in the existing code.**

1. Wire three simple “sensor” circuits of your choice to the pins of your Q board.  These could simply be potentiometers, temp sensors, buttons \- anything is fine. Optionally, you can use sensors on the Kit-on-a-Shield.  
2. Ensure your Arduino Q is connected to your local WiFi network.   
3. In the Arduino Sketch, **provide\_safe** a function that will provide a sensor reading.   
4. In the Arduino Sketch, **write the function** referred to in the previous step.  
5. In the Python file, in the `store_sensor_data_to_db()` function, add code to call the function created above, and write its value to the database.  
6. In the Python file, in the `read_write_display_loop()` function, add code to retrieve the new sensor's data from the database using `get_samples_for_chart()`.  
7. In the Python file, add a new chart placeholder in the body section, and update the loop to render the new chart.

## Notes:

You could complete this work order in SBC mode entirely, however you would need to add a keyboard, mouse, and monitor to your Arduino Q. Network mode is the preferred option, allowing you to develop from your main workstation.

When you first run your app, the charts will be empty, after about 10 minutes you’ll have accumulated enough readings for it to display fully. 

Take some time to look at the Overview, Usage Examples, and API Documentation tabs in the Time Series Store Brick and the Streamlit UI Brick.

## Testing Criteria:

Once completed with these tasks, you can check your work by ensuring the following while the App is running: 

* All three sensor values appear as separate line charts in the browser  
* Charts update with new data points roughly once per minute  
* No errors appear in the AppLab consoles (Arduino, Python, or Streamlit)