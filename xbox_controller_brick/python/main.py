import os
import time

os.environ["APP_SOCKET"] = "unix:///var/run/arduino-router.sock"

from arduino.app_utils import App
from arduino.app_utils import Bridge

def loop():
    try:
        xbox_controller_state = bridge.call("xbox_controller_state", {}, timeout=3)
        print("state", xbox_controller_state)
    except RpcError as rpc_err:
        print(f"[Main Loop] Router rejected execution. Code {rpc_err.code}: {rpc_err.message}")
    except TimeoutError:
        print("[Main Loop] Network processing timed out waiting for server process.")
    except Exception as e:
        print(f"[Main Loop] RPC Call failed: {e}")

    time.sleep(0.05)

bridge = Bridge()

App.run(user_loop=loop)

# Start application
#if __name__ == "__main__":
#    # In App Lab environments, you can spawn tasks before blocking with App.run()
#    # Or place handling loops inside your concurrent scheduler.
#    pass
#    # App.run()
