import time

from arduino.app_utils import App
from arduino.app_utils import Bridge
from arduino.router_bridge import RpcError

def setup():
    waiting = True

    while waiting:
        try:
            print("DEBUG: try to stop the robot")
            reading = Bridge.call("move", 0, 0, 0, 0)

            waiting = False
        except RpcError as e:
            print("DEBUG: bridge methods not yet available")

        time.sleep(1)

def loop():
    try:
        while True:
            print("DEBUG: loop started")
            reading = Bridge.call("move", 25, 25, 0, 0)
            time.sleep(0.33)

            reading = Bridge.call("move", 0, 0, 0, 0)
            time.sleep(3)
    finally:
        print("DEBUG: finally stop the motor")
        reading = Bridge.call("move", 0, 0, 0, 0)


setup()

App.run(user_loop=loop)
