##### IMPORTS ###################
# Standard library

# AppLab packages/bricks
from arduino.app_utils import App, Bridge
from arduino.app_bricks.video_objectdetection import VideoObjectDetection

##### GLOBALS ###################

# Initialize detector with custom confidence and debounce settings
video_detector = VideoObjectDetection(confidence=0.4, debounce_sec=10)

##### FUNCTIONS #################

def person_detected():
    """Call MCU function to make noise"""
    Bridge.notify("makeNoise")
    print("Person detected!  Get a hair cut!")


#############################################
## ADD ADDITIONAL CALL BACK FUNCTION BELOW ##
#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇#


#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆#
## ADD ADDITIONAL CALL BACK FUNCTION ABOVE ###
#############################################

##### BODY ######################
video_detector.on_detect("person", person_detected)

#############################################
## ADD ADDITIONAL DETECTOR CODE BELOW #######
#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇#


#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆#
## ADD ADDITIONAL DETECTOR CODE ABOVE #######
#############################################

App.run()