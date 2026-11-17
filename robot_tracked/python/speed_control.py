from arduino.app_utils import Bridge


class SpeedControl:
    def __init__(self):
        pass

    def move(self, xbox_controller_state):
        speed = int(xbox_controller_state["left_y"] * -100.0)

        Bridge.call("move", speed, speed, 0, 0)
