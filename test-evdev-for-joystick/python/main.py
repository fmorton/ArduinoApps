import time

from arduino.app_utils import App
import evdev
#from evdev import InputDevice

print("Hello world!-----------------------------------------------------------------------------")


def loop():
    """This function is called repeatedly by the App framework."""
    # You can replace this with any code you want your App to run repeatedly.
    time.sleep(10)

    #print("DEBUG: find game pads.........")
    #find_gamepads()



def find_gamepads():
    print("Searching for connected input devices...\n")
    #devices = [InputDevice(path) for path in evdev.list_devices()]
    
    #if not devices:
    #    print("[-] No input devices found. Check your USB connection or permissions.")
    #    print("    Try running with: sudo python script.py")
    #    return

    #gamepads_found = []

    #print(f"{'Device Path':<18} | {'Device Name'}")
    #print("-" * 50)
    
    #for device in devices:
    #    print(f"{device.path:<18} | {device.name}")
        
    #    # Match common controller keywords
    #    name_lower = device.name.lower()
    #    if any(keyword in name_lower for keyword in ["xbox", "microsoft", "controller", "gamepad", "joystick"]):
    #        gamepads_found.append(device)

    #print("\n" + "="*50)
    #if gamepads_found:
    #    print(f"[+] Found {len(gamepads_found)} potential controller(s):")
    #    for pad in gamepads_found:
    #        print(f"    -> Use path '{pad.path}' for your Pygame project.")
    #else:
    #    print("[-] Could not find an Xbox controller by name.")
    #    print("    Look at the list above and manually choose the path that looks correct (e.g., /dev/input/event0).")

#if __name__ == "__main__":
#    find_gamepads()
#print("DEBUG: __name__ is:::::::::::::::::::::::::::::::::::::::::", __name__)
#find_gamepads()

# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
App.run(user_loop=loop)
