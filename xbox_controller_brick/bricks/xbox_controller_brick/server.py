import os
import sys
import threading
import time

#from arduino.app_utils import brick
from arduino.router_bridge import Bridge
from robot.xbox_controller import XboxController

class XboxControllerThread:
    def __init__(self, controller):
        self.controller = controller

        self.thread = threading.Thread(target=controller.run, args=(self.process_event,), daemon=True)

        self.thread.start()

    def process_event(self, controller):
        time.sleep(XboxController.EVENT_LOOP_DELAY)

        return True

def xbox_controller_state(payload):
    return(controller.state.dictionary())


controller = XboxController().connect()
controller_thread = XboxControllerThread(controller)

bridge = Bridge()

if not bridge.connect(timeout=32):
    pass
else:
    bridge.provide("xbox_controller_state", xbox_controller_state)

    while True:
        time.sleep(5)
