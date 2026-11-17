import os
import time

from arduino.app_utils import App
from arduino.app_utils import Bridge
from arduino.router_bridge import RpcError
from robot_control import RobotControl
from speed_control import SpeedControl


def loop():
    bridge = Bridge()

    robot_control = RobotControl()
    speed_control = SpeedControl()

    robot_control.bridge_ready()

    while True:
        try:
            xbox_controller_state = bridge.call("xbox_controller_state", {}, timeout=32)

            speed_control.move(xbox_controller_state)

            time.sleep(0.05)
        except Exception as e:
            print(f"Robot exception: {e}")


App.run(user_loop=loop)
