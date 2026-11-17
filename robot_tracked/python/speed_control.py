from arduino.app_utils import Bridge


class SpeedControl:
    def __init__(self):
        self.current_left_speed = 0
        self.current_right_speed = 0

    def move(self, xbox_controller_state):
        turn_sensitivity = 0.5  # 0.5 to 1.0

        x = xbox_controller_state["left_x"]
        y = xbox_controller_state["left_y"]

        x = -x * turn_sensitivity

        left = y + x
        right = y - x

        max_val = max(abs(left), abs(right), 1.0)
        left /= max_val
        right /= max_val

        left_speed = -round(left * 100)
        right_speed = -round(right * 100)

        if (left_speed != self.current_left_speed) or (
            right_speed != self.current_right_speed
        ):
            Bridge.call("move", left_speed, right_speed, 0, 0)

            self.current_left_speed = left_speed
            self.current_right_speed = right_speed
