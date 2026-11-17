import os
import time

os.environ["APP_SOCKET"] = "unix:///var/run/arduino-router.sock"

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
    while True:
        try:
            xbox_controller_state = bridge.call("xbox_controller_state", {}, timeout=32)

            # print("state", xbox_controller_state)

            speed = int(xbox_controller_state["left_y"] * -100.0)

            reading = Bridge.call("move", speed, speed, 0, 0)

            time.sleep(0.05)
        except RpcError as rpc_err:
            print(
                f"[Main Loop] Router rejected execution. Code {rpc_err.code}: {rpc_err.message}"
            )
        except TimeoutError:
            print(
                "[Main Loop] Network processing timed out waiting for server process."
            )
        except Exception as e:
            print(f"[Main Loop] RPC Call failed: {e}")
        # finally:
        #    print("DEBUG: finally stop the motor")
        #    reading = Bridge.call("move", 0, 0, 0, 0)


bridge = Bridge()

setup()

App.run(user_loop=loop)
