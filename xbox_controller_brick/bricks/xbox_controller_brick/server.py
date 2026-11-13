import os
import sys
import threading
import time

from arduino.router_bridge import Bridge
from robot.xbox_controller import XboxController
from robot.xbox_controller_thread import XboxControllerThread
from robot.xbox_state_linux import XboxStateLinux


def xbox_controller_state(payload):
    return controller.state.dictionary()


controller = XboxController().connect()
controller_thread = XboxControllerThread(controller)

bridge = Bridge()

if not bridge.connect(timeout=32):
    pass
else:
    bridge.provide("xbox_controller_state", xbox_controller_state)

    while True:
        time.sleep(5)
