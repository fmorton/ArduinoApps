import os
import time

from arduino.app_utils import Bridge
from arduino.router_bridge import RpcError


class RobotControl:
    def __init__(self):
        pass

    def bridge_ready(self):
        waiting = True

        while waiting:
            try:
                reading = Bridge.call("move", 0, 0, 0, 0)

                waiting = False
            except RpcError as e:
                print(f"Robot bridge_ready exception[1]: {e}")
            except Exception as e:
                print(f"Robot bridge_ready exception[2]: {e}")

            time.sleep(1)
