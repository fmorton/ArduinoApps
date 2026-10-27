# main.py
import time
# Assuming your client SDK script (from the previous step) is saved as joystickbridge.py
import joystickbridge as joystick

# ----------------------------------------------------
# PS4 Axis + Button Names (EVDEV codes)
# ----------------------------------------------------
AXIS_NAMES = {
    0: "lx",      # ABS_X
    1: "ly",      # ABS_Y
    2: "rx",      # ABS_RX
    5: "ry",      # ABS_RY

    3: "L2 Analog", 
    4: "R2 Analog", 
    9: "R2 Analog", 
    10: "L2 Analog", 

    16: "dpad_x", # ABS_HAT0X
    17: "dpad_y", # ABS_HAT0Y
}

AXIS_ORDER = [
    0,   # lx
    1,   # ly
    2,   # rx
    5,   # ry
    3,   # l2 analog
    4,   # r2 analog
    10,
    9,
    16,  # dpad_x
    17,  # dpad_y
]

BUTTON_NAMES = {
    305: "cross",      # BTN_SOUTH
    306: "circle",     # BTN_EAST
    307: "triangle",   # BTN_NORTH
    304: "square",     # BTN_WEST

    308: "l1/Y",         # BTN_TL
    309: "r1",         # BTN_TR
    310: "l2_btn",     # BTN_TL2
    311: "r2_btn",     # BTN_TR2

    312: "share",      # BTN_SELECT
    313: "options",    # BTN_START
    316: "ps",         # BTN_MODE

    314: "l3",         # BTN_THUMBL
    315: "r3/options", # BTN_THUMBR

    317: "touchpad/Stl Lt Bth",   # Touchpad click
    318: "Stick Rt Btn",

    158: "share",   # legacy fallback
    172: "guide",   # legacy fallback
}

BUTTON_ORDER = [
    158, 172, 305, 306, 307, 304,
    308, 309, 310, 311, 312, 313, 
    316, 314, 315, 317, 318
]

# ----------------------------------------------------
# Inspector Class (Pretty Printing)
# ----------------------------------------------------
class Inspector:
    def __init__(self):
        self.last_axes = {}
        self.last_buttons = {}

    def button_label(self, code):
        return BUTTON_NAMES.get(code, f"btn_{code}")

    def print_changes(self, axes, buttons):
        changed = False

        # AXES
        for raw_code, value in axes.items():
            code = int(raw_code)
            name = AXIS_NAMES.get(code, f"axis_{code}")

            old = self.last_axes.get(code)
            if old is None or old != value:
                delta = 0 if old is None else value - old
                # evdev raw values are ints, changed formatting from float to signed integer tracking
                print(f"Axis {name:<8} {value:>7} (Δ {delta:+7})")
                self.last_axes[code] = value
                changed = True

        # BUTTONS
        for raw_code, value in buttons.items():
            code = int(raw_code)
        
            old = self.last_buttons.get(code)
            if old is None or value != old:
                name = self.button_label(code)
                print(f"Button {name:<10} {value}")
                self.last_buttons[code] = value
                changed = True

        return changed


# ----------------------------------------------------
# MAIN
# ----------------------------------------------------
def main():
    print("=== PS4 EVDEV Joystick Test ===")
    
    # 1. Remotely fire the initialization sequence
    print("Initializing Bluetooth & input device node on the brick framework...")
    init_status = joystick.startJoystick()
    print("Bridge Response:", init_status)
    
    if init_status.get("status") == "error":
        print("❌ Could not stand up Joystick hardware link. Exiting.")
        return

    # 2. Metadata Queries (Safely extracting strings/integers from dictionary keys)
    try:
        # FIX: Appended .get() keys to resolve dict wrappers cleanly
        name = joystick.getName().get("name", "Unknown")
        print("Joystick Name:", name)

        num_axes = joystick.getNumAxes().get("num_axes", 0)
        print("Number of Axes:", num_axes)

        num_buttons = joystick.getNumButtons().get("num_buttons", 0)
        print("Number of Buttons:", num_buttons)

        axis_map = joystick.getAxisMap().get("axis_map", [])
        print("RAW axis_map:", axis_map)

        button_map = joystick.getButtonMap().get("button_map", [])
        print("RAW button_map:", button_map)

        # Get left joystick range details
        resp = joystick.getAxisRange(0)
        
        # Access by explicit dictionary keys rather than index numbers
        axis_min = resp["range"]["min"]
        axis_max = resp["range"]["max"]
        
        print("Lx - min:", axis_min, "lx max:", axis_max)

    except Exception as e:
        print("Error reading joystick metadata:", e)
        return

    # Fetch axis ranges
    try:
        # 1. Grab the "axis_ranges" dictionary from the API response
        response_data = joystick.getAxisRanges()  # Assuming this hits the API route
        axis_ranges = response_data.get("axis_ranges", {})
        
        print("\n=== Axis Range Details ===")
        print(f"{'Axis Name':<12} {'Code':<6} {'Min':<8} {'Max':<8} {'Fuzz':<6} {'Flat':<6}")
        print("-" * 52)
        
        for code in axis_map:
            name = AXIS_NAMES.get(code, f"axis_{code}")
            
            # API keys from JSON are always strings, check str(code) first
            rng = axis_ranges.get(str(code)) or axis_ranges.get(code)
            
            if rng and isinstance(rng, dict):
                print(f"{name:<12} {code:<6} {rng.get('min'):<8} {rng.get('max'):<8} {rng.get('fuzz'):<6} {rng.get('flat'):<6}")
            else:
                print(f"{name:<12} {code:<6} Data missing or malformed")
                
    except Exception as e:
        print("Error reading axis ranges:", e)


    print("\n=== Live Joystick State (Move sticks or press keys) ===")
    inspector = Inspector()

    while True:
        try:
            state = joystick.getState()
            
            # Catch network/bridge errors gracefully out of the server response
            if state.get("status") == "error":
                print(f"Bridge error: {state.get('message')}")
                time.sleep(1.0)
                continue

            # OPTIMIZATION: Check the backend change flags first.
            # If nothing shifted, skip calculating string arrays entirely to reduce engine drag.
            if state.get("axes_changed") or state.get("buttons_changed") or not inspector.last_axes:
                
                axes = {int(k): v for k, v in state.get("axes", {}).items()}
                buttons = {int(k): v for k, v in state.get("buttons", {}).items()}
        
                axis_values = [axes.get(code, 0) for code in AXIS_ORDER]
                button_values = [buttons.get(code, 0) for code in BUTTON_ORDER]
        
                if inspector.print_changes(axes, buttons):
                    print("AX:", axis_values)
                    print("BT:", button_values)
                    print()
        
        except Exception as e:
            print("Error reading joystick state:", e)
    
        # 100Hz poll rate matching standard controller broadcast intervals
        time.sleep(0.01)

if __name__ == "__main__":
    main()