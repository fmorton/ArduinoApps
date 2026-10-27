# joystick_evdev.py
import threading
from evdev import InputDevice, ecodes
from detect_joystick import find_gamepad_event

class Joystick:
    def __init__(self, device=None):
        """
        Initializes the Joystick handler.
        If no device path is provided, it tries to auto-detect one using detect_joystick.
        """
        if device is None:
            device = find_gamepad_event()

        if device is None:
            raise RuntimeError("No PS4 controller detected")

        self.device_path = device  # e.g., "/dev/input/eventX"
        self.dev = None

        # Maps and state trackers
        self.axis_map = []          # List of registered hardware axis codes (EV_ABS)
        self.button_map = []        # List of registered hardware button codes (EV_KEY)
        self.axis_states = {}       # Dictionary tracking current position of each axis {code: value}
        self.button_states = {}     # Dictionary tracking current state of each button {code: 0 or 1}
                
        # Delta tracking flags (has anything shifted since the last time get_state was polled?)
        self.axis_changed = False
        self.buttons_changed = False

        self.num_axes = 0
        self.num_buttons = 0
        self.name = ""

        self.running = False
        
        # Threading Lock: Ensures data isn't modified by the background loop 
        # at the exact moment the main thread is reading it via the Public API.
        self.lock = threading.Lock()

    # ----------------------------------------------------
    # Initialization
    # ----------------------------------------------------
    def open(self):
        """
        Opens the Linux input device and queries its capabilities 
        to dynamically map all available axes and buttons.
        """
        # Connect to the evdev interface for the specified device path
        self.dev = InputDevice(self.device_path)
        self.name = self.dev.name

        # Query the device capabilities (returns a dict of input types and their supported codes)
        caps = self.dev.capabilities(verbose=False)

        # Extract Absolute Axis Capabilities (EV_ABS includes Joysticks, Triggers, D-Pads)
        abs_caps = caps.get(ecodes.EV_ABS, [])
        
        # Each item in abs_caps is a tuple: (axis_code, AbsInfo_object). We just need the code.
        self.axis_map = []
        self.axis_ranges = {}

        for code, info in abs_caps:
            self.axis_map.append(code)
            self.axis_ranges[code] = (info.min, info.max, info.fuzz, info.flat)

        self.num_axes = len(self.axis_map)

        # Extract Key/Button Capabilities (EV_KEY includes X, O, Square, Triangle, Bumpers)
        key_caps = caps.get(ecodes.EV_KEY, [])
        self.button_map = list(key_caps)
        self.num_buttons = len(self.button_map)

        # Seed the state dictionaries with baseline zero values under a thread lock
        with self.lock:
            for a in self.axis_map:
                self.axis_states[a] = 0
            for b in self.button_map:
                self.button_states[b] = 0

    # ----------------------------------------------------
    # Background event loop
    # ----------------------------------------------------
    def loop(self):
        """
        An infinite block loop meant to run in a background thread.
        Listens to continuous hardware event streams and updates state cache.
        """
        self.running = True
        self.open()

        # read_loop() blocks the thread and yields events from Linux as they happen physically
        for event in self.dev.read_loop():
            if not self.running:
                break

            # Lock the data structures while writing updates to prevent race conditions
            with self.lock:
                
                # Check if the hardware event represents an Absolute Axis movement
                if event.type == ecodes.EV_ABS:
                    # Verify this specific axis code was recognized during setup
                    if event.code in self.axis_states:
                        # Only trigger updates and flags if the position actually shifted
                        if self.axis_states[event.code] != event.value:
                            self.axis_states[event.code] = event.value
                            self.axis_changed = True

                # Check if the hardware event represents a Button press or release
                elif event.type == ecodes.EV_KEY:
                    # Verify this specific button code was recognized during setup
                    if event.code in self.button_states:
                        # evdev values: 1 = Press, 0 = Release, 2 = Hold. 
                        # We convert this cleanly to a boolean-like integer (1 or 0).
                        new_val = 1 if event.value else 0
                        
                        # Only trigger updates if the button transitioned states
                        if self.button_states[event.code] != new_val:
                            self.button_states[event.code] = new_val
                            self.buttons_changed = True
                                                    
    # ----------------------------------------------------
    # Public API (Safe to call from other threads)
    # ----------------------------------------------------
    def get_num_axes(self):
        return self.num_axes

    def get_num_buttons(self):
        return self.num_buttons

    def get_axis_map(self):
        return list(self.axis_map)

    def get_axis_range(self, code):
        return self.axis_ranges.get(code)
    
    def get_axis_ranges(self):
        return dict(self.axis_ranges)

    def get_button_map(self):
        return list(self.button_map)

    def get_axis_values(self):
        """Returns a snapshot copy of all current axis positions."""
        with self.lock:
            return dict(self.axis_states)

    def get_button_values(self):
        """Returns a snapshot copy of all current button positions."""
        with self.lock:
            return dict(self.button_states)

    def get_state(self):
        """
        Returns the full combined state dictionary and marks 
        the 'changed' tracking flags back to False for the next poll cycle.
        """
        with self.lock:
            ret = {
                "axes_changed": self.axis_changed,
                "axes": dict(self.axis_states),
                "buttons_changed": self.buttons_changed,
                "buttons": dict(self.button_states),
            }
            # Reset delta tracking indicators after delivering them to the caller
            self.axis_changed = False
            self.buttons_changed = False
            return ret