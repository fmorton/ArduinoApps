import time
from arduino.app_utils import App
from xbox_controller import XboxControllerManager

print("Initializing Python-Only Environment...")

# Instantiate our custom Python-only brick
gamepad = XboxControllerManager()

def user_loop():
    while True:
        # Pull latest gamepad updates strictly inside the container
        data = gamepad.get_telemetry()
        print(f"Telemetry Update -> Status: {data['status']} | Left Stick: {data['left_stick']}")
        
        # Keep execution cycle steady
        time.sleep(0.1)

# Start application
if __name__ == "__main__":
    # In App Lab environments, you can spawn tasks before blocking with App.run()
    # Or place handling loops inside your concurrent scheduler.
    print("Application Ready. Starting telemetry tracking...")
    # App.run()
