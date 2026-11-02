import time
from arduino.app_utils import App
from xbox_controller_brick import XboxControllerBrick

print("Initializing Python-Only Environment...")

controller = XboxControllerBrick()

# Start application
if __name__ == "__main__":
    # In App Lab environments, you can spawn tasks before blocking with App.run()
    # Or place handling loops inside your concurrent scheduler.
    pass
    # App.run()
