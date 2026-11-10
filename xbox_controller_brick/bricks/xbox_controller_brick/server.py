import os
import sys
import threading
import time

#os.environ["SDL_AUDIODRIVER"] = "dummy"
#os.environ["SDL_VIDEODRIVER"] = "dummy"
#os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
#if "XDG_RUNTIME_DIR" not in os.environ:
#    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"

#from arduino.app_utils.logger import Logger
#from arduino.app_utils import brick
from robot.xbox_controller import XboxController

class XboxControllerThread:
    def __init__(self, controller):
        self.controller = controller

        self.thread = threading.Thread(target=controller.run, args=(self.process_event,), daemon=True)

        self.thread.start()

    def process_event(self, controller):
        time.sleep(XboxController.EVENT_LOOP_DELAY)

        return True

# this is the direct pygame approach
#import pygame
#pygame.init()
#
#joystick_count = pygame.joystick.get_count()
#print(f"Number of joysticks::::: {joystick_count}")
#
#if joystick_count > 0:
#  joystick = pygame.joystick.Joystick(0)
#  joystick.init()
#  print(f"Connected to: {joystick.get_name()}")
#
#while True:
#    for event in pygame.event.get():
#        print("Event:" + str(event))
#
#    time.sleep(0.25)

controller = XboxController().connect()

controller_thread = XboxControllerThread(controller)

while True:
    time.sleep(5)
