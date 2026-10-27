from robot.xbox_controller import XboxController
from time import sleep

from arduino.app_utils import App

import os

if "XDG_RUNTIME_DIR" not in os.environ:
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"
    # Ensure the directory exists
    os.makedirs("/tmp/runtime-root", exist_ok=True)

os.environ["SDL_VIDEODRIVER"] = "dummy" 

# Force SDL to look at the correct input system if it's defaulting elsewhere
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

def robot(controller):
  print("runner", controller.state.state_string())

  if controller.state.button_down_milliseconds(XboxController.BUTTON_XBOX):
      return False

  sleep(XboxController.EVENT_LOOP_DELAY)

  return True


print("DEBUG: start the controller...")
controller = XboxController().connect()

print("DEBUG: start the controller...RUN")

controller.run(robot, True)
print("DEBUG: start the controller...RUNNING")

def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    time.sleep(10)


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
