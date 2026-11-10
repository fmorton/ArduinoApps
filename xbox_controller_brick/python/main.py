import time

from arduino.app_utils import App
#from xbox_controller_brick import XboxControllerBrick

def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    print("python task running")

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
