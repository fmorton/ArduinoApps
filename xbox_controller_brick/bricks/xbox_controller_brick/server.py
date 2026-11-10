import os
import sys
import threading
import time

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


controller = XboxController().connect()

controller_thread = XboxControllerThread(controller)

while True:
    print(controller.state.__dict__)

    time.sleep(5)
