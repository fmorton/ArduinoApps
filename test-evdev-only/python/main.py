import time

from arduino.app_utils import App

#import evdev
import subprocess
import sys

try:
    import evdev
except ModuleNotFoundError:
    print("Installing evdev package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "evdev", "--break-system-packages"])
    print("Evdev package installed successfully!")
    import evdev
print("Hello world!")


def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    time.sleep(10)


# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
