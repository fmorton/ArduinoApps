import os
import time

os.environ["APP_SOCKET"] = "unix:///var/run/arduino-router.sock"

from arduino.app_utils import App
from arduino.app_utils import Bridge
#from xbox_controller_brick import XboxControllerBrick


def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    print("python task running")

    try:
        print("try to call.....")
        xbox_controller_state = Bridge.call("xbox_controller_state", None)
        print("try to call.....DONE")
        print("state", xbox_controller_state)
    except Exception as e:
        print(f"[Main Loop] RPC Call failed: {e}")

    time.sleep(1)

    #controller = XboxControllerBrick()

# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)

# Start application
#if __name__ == "__main__":
#    # In App Lab environments, you can spawn tasks before blocking with App.run()
#    # Or place handling loops inside your concurrent scheduler.
#    pass
#    # App.run()
