import time
<<<<<<< HEAD

from arduino.app_utils import App

print("Hello world!")


def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    time.sleep(10)


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
=======
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
>>>>>>> refs/remotes/origin/main
