# 🎮 Xbox Controller Brick (`xbox_controller_brick`)

A custom **Arduino App Lab Brick** for the **Arduino UNO Q** that reads input events from a connected Xbox controller and exposes the controller state over the **Arduino Router RPC Bridge** (`xbox_controller_state`).

---

## 📋 Overview

In Arduino App Lab, application containers run isolated from host hardware interfaces like `/dev/input`. This Brick encapsulates the Xbox controller service in its own container (`bricks/xbox_controller_brick`) and registers an RPC endpoint on the Arduino Router (`unix:///var/run/arduino-router.sock`). 

Any App Lab Python script—or microcontroller sketch—can poll the live controller state using `Bridge.call("xbox_controller_state", {})` at ~20 Hz without needing direct hardware permissions.

### Repository Structure

```text
xbox_controller_brick/
├── bricks/
│   └── xbox_controller_brick/   # Custom Brick service & RPC provider
├── python/
│   └── main.py                  # Reference App Lab Python client polling controller state
├── sketch/                      # Arduino MCU (STM32) sketch
├── app.yaml                     # App Lab application & Brick manifest
├── docker-compose.yaml          # Container device/volume mappings (e.g., /dev/input)
└── xbox_controller_brick.zip    # Packaged Brick archive for distribution
```

---

## 🛠️ Prerequisites

* **Hardware:** Arduino UNO Q (or compatible Q-series board)
* **Controller:** Bluetooth-enabled Xbox Controller (Xbox One S / Series X|S) or wired USB Xbox controller
* **Software:** Arduino App Lab IDE / `arduino-app-cli`

---

## 🚀 Setup & Installation

### 1. Connect the Xbox Controller
Connect your controller to the Arduino UNO Q via USB, or pair it via Bluetooth using `bluetoothctl` on the board's shell:

```bash
bluetoothctl
power on
agent on
default-agent
scan on
# Put your Xbox controller into pairing mode, then pair and trust its MAC address:
pair <CONTROLLER_MAC_ADDRESS>
trust <CONTROLLER_MAC_ADDRESS>
connect <CONTROLLER_MAC_ADDRESS>
```

### 2. Run as an App or Add as a Brick
* **Run the Demo App:** Clone this repository into your Arduino App Lab workspace and run `xbox_controller_brick` to see live controller state output in the console.
* **Use in Your Own App:** Copy `bricks/xbox_controller_brick` (or extract `xbox_controller_brick.zip`) into your project's `bricks/` folder and declare it in your `app.yaml` and `docker-compose.yaml`.

---

## 💻 Usage (`python/main.py` Framework)

Your `python/main.py` connects to the Arduino Router socket and polls the `xbox_controller_state` RPC method every `50ms` (`0.05s`):

```python
import os
import time

os.environ["APP_SOCKET"] = "unix:///var/run/arduino-router.sock"

from arduino.app_utils import App, Bridge
from arduino.router_bridge import RpcError

bridge = Bridge()

def loop():
    try:
        # Request the latest Xbox controller state from the Brick over RPC
        xbox_controller_state = bridge.call("xbox_controller_state", {}, timeout=3)
        print("state", xbox_controller_state)

    except RpcError as rpc_err:
        print(f"[Main Loop] Router rejected execution. Code {rpc_err.code}: {rpc_err.message}")
    except TimeoutError:
        print("[Main Loop] Network processing timed out waiting for server process.")
    except Exception as e:
        print(f"[Main Loop] RPC Call failed: {e}")

    time.sleep(0.05)

App.run(user_loop=loop)
```

---

## 🔌 RPC API Reference

### `xbox_controller_state`
* **Parameters:** `{}` (empty dictionary)
* **Timeout:** Recommended `3` seconds
* **Returns:** Dictionary/JSON object representing the current state of buttons, triggers, and thumbsticks.

---

## ⚙️ Configuration Details

* **`docker-compose.yaml`**: Maps host input devices (such as `/dev/input`) and the Arduino Router socket (`/var/run/arduino-router.sock`) so the Brick service can read gamepad events and register RPC methods.
* **`app.yaml`**: Registers `xbox_controller_brick` as a Brick dependency so App Lab launches the background service alongside `python/main.py`.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome in [fmorton/ArduinoApps](https://github.com).

