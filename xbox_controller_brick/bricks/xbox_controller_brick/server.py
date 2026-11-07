import os
import sys
#from arduino.app_utils.logger import Logger
#from arduino.app_utils import brick
import os

# 1. Force a dummy audio driver to bypass the PulseAudio/XDG error
os.environ["SDL_AUDIODRIVER"] = "dummy"

# 2. Force a dummy video driver to avoid X11/Wayland display errors
os.environ["SDL_VIDEODRIVER"] = "dummy"

# 3. Prevent background event blocking if using controllers
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

# 4. Safely redirect the runtime directory if needed
if "XDG_RUNTIME_DIR" not in os.environ:
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"

# NOW you can safely import and initialize your library
import pygame
import time
import socket

from robot.xbox_controller import XboxController

#class XboxControllerBrick:
#    def __init__(self):
#        pygame.init()

#        print("DEBUG: init brick!!!!!!!!!!!")
#        #self.controller = XboxController().connect()
#        #self.controller = XboxController()
#        while True:
#            for event in pygame.event.get():
#                print("Event:" + str(event))

#            time.sleep(0.25)

 #       print("DEBUG: init brick!!!!!!!!!!! DONE")

#from arduino.app_utils import brick, Logger
#import time

#logger = Logger("GreeterBrick")


#@@brick
class XboxControllerBrick:
    def __init__(self, name="World"):
       self.name = name
#
#    def start(self):
#        logger.info("Starting Greeter")
#
#    def stop(self):
#        logger.info("Stopping Greeter")
#
#    # This is a non-blocking method that will be called repeatedly
#    def loop(self):
#        logger.info(f"Hello, {self.name}!")
#        time.sleep(1)

#logger = Logger('my_brick_logger')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5001))

#pygame.init()

def robot(controller):
  print("runner", controller.state.state_string())

  if controller.state.button_down_milliseconds(XboxController.BUTTON_XBOX):
      return False

  sleep(XboxController.EVENT_LOOP_DELAY)

  return True


controller = XboxController().connect()

controller.run(robot)

print("Server loop starting up")

while True:
    print("Server is running")
    #print("runner", controller.state.state_string())

    time.sleep(10)
