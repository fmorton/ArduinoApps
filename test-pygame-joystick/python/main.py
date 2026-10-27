import time

#from arduino.app_utils import App

#print("Hello world!")


#def loop():
#    """This function is called repeatedly by the App framework."""
#    # You can replace this with any code you want your App to run repeatedly.
#    time.sleep(10)

import os
import sys

# UID is 100 from within arduino lab and from the command line
# However, the groups do not match when comparing running under arduino app lab and a terminal session
# AppLab: Current Execution Groups: [20, 29, 44, 991, 1000, 1001]
# Terminal: Current Execution Groups: [4, 20, 27, 29, 44, 100, 101, 102, 103, 987, 991, 995, 1000, 1001]
print(f"Current Execution UID: {os.getuid()}")
print(f"Current Execution Groups: {os.getgroups()}")

os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

# Force Pygame to use a dummy graphic driver (avoids X11/Wayland errors)
os.environ["SDL_VIDEODRIVER"] = "dummy"

# If your project doesn't use audio, disable the audio driver too
# this removes the startup error XDG_RUNTIME_DIR (/run/user/1000) is not owned by us (uid 1000), but by uid 0!
#(This could e.g. happen if you try to connect to a non-root PulseAudio as a root user, over the native protocol. Don't do that.)

os.environ["SDL_AUDIODRIVER"] = "dummy" 

# Force standard Linux event system fallback inside isolated containers
os.environ["SDL_JOYSTICK_DEVICE"] = "/dev/input/js0"  # Adjust index if necessary

if "XDG_RUNTIME_DIR" not in os.environ:
  os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"

import pygame
# Force SDL to look at the correct input system if it's defaulting elsewhere

print("DEBUG::::::::::::::::::::::::::::::::::::::::::::::: init pygame")
pygame.init()
print("DEBUG::::::::::::::::::::::::::::::::::::::::::::::: init pygame completed...init joystick")
pygame.joystick.init()
print("DEBUG::::::::::::::::::::::::::::::::::::::::::::::: init joystick completed")

# CRITICAL: Let SDL process and register the connected devices
print("DEBUG::::::::::::::::::::::::::::::::::::::::::::::: doing the pumping")
pygame.event.pump() 
time.sleep(0.1) # Give it a fraction of a second to settle
pygame.event.pump()

# Check how many joysticks are connected
joystick_count = pygame.joystick.get_count()
print(f"Number of joysticks::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {joystick_count}")

if joystick_count > 0:
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  print(f"Connected to: {joystick.get_name()}")

# See: https://docs.arduino.cc/software/app-lab/tutorials/getting-started/#app-run
#App.run(user_loop=loop)
