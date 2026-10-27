# app.py
import sys
import signal
import atexit
import threading
from flask import Flask, jsonify

from joystick_helper import Joystick
from detect_joystick import disconnect_active_gamepads

app = Flask(__name__)

# Initialize as None. It stays uninitialized until /joystick/start is hit.
js = None
init_lock = threading.Lock()

# -------------------------------------------------------------------------
# Container Shutdown Cleanup Hook
def shutdown_cleaner(*args):
    """Executes automatically when the Flask app process terminates."""
    print("Stopping active gamepad links...")
    try:
        disconnect_active_gamepads()
    except Exception as e:
        print(f"Error during cleanup: {e}")
    # Don't call sys.exit(0) inside the signal handlers manually if you can avoid it;
    # let Flask complete its standard shutdown sequence organically.

atexit.register(shutdown_cleaner)
signal.signal(signal.SIGTERM, shutdown_cleaner)
signal.signal(signal.SIGINT, shutdown_cleaner)

# ----------------------------------------------------
# Joystick Lifecycle Initialization Control
# ----------------------------------------------------
@app.route("/joystick/start", methods=["POST", "GET"])
def start_joystick():
    global js
    with init_lock:
        if js is not None:
            return jsonify({"status": "already_initialized", "name": js.name}), 200
        
        print("🤖 Remote Trigger: Initializing Joystick Fallback and Detection Subsystem...")
        try:
            # Instantiate the joystick object
            js = Joystick()
            
            # Explicitly trigger open() here on the main thread so that if it fails 
            # (e.g. PermissionError on /dev/input/eventX), it catches it immediately 
            # and returns a 500 error instead of silently crashing the background thread.
            js.open()
            
            # Start background event reader loop
            threading.Thread(target=js.loop, daemon=True).start()
            return jsonify({"status": "success", "name": js.name}), 200
        except Exception as e:
            print(f"❌ Dynamic initialization failed: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

# ----------------------------------------------------
# Joystick API Routes (Safe with structural global fallback)
# ----------------------------------------------------
@app.route("/joystick/state")
def js_state():
    if not js: return jsonify({"error": "Joystick not initialized. Call /joystick/start first."}), 503
    return jsonify(js.get_state())

@app.route("/joystick/name")
def js_name():
    if not js: return jsonify({"name": "Not Connected"}), 503
    return jsonify({"name": js.name})

@app.route("/joystick/num_axes")
def js_num_axes():
    if not js: return jsonify({"num_axes": 0}), 503
    return jsonify({"num_axes": js.get_num_axes()})

@app.route("/joystick/num_buttons")
def js_num_buttons():
    if not js: return jsonify({"num_buttons": 0}), 503
    return jsonify({"num_buttons": js.get_num_buttons()})

@app.route("/joystick/axis_map")
def js_axis_map():
    if not js: return jsonify({"axis_map": []}), 503
    return jsonify({"axis_map": js.get_axis_map()})

@app.route("/joystick/button_map")
def js_button_map():
    if not js: return jsonify({"button_map": []}), 503
    return jsonify({"button_map": js.get_button_map()})

@app.route("/joystick/axes")
def js_axes():
    if not js: return jsonify({}), 503
    return jsonify(js.get_axis_values())

@app.route("/joystick/buttons")
def js_buttons():
    if not js: return jsonify({}), 503
    return jsonify(js.get_button_values())

@app.route("/joystick/axis_range/<int:code>")
def js_axis_range(code):
    if not js:
        return jsonify({"error": "Joystick not initialized"}), 503

    # FORCE FLUSH: This skips Python's print buffer and forces Docker to display it
    # print(f"--- DEBUG: Looking for axis {code} ---", flush=True)
    # print("Available keys in axis_ranges:", list(js.axis_ranges.keys()), flush=True)
    # print("Full axis_ranges content:", js.axis_ranges, flush=True)

    # Check both integer and string
    rng = js.get_axis_range(code) or js.get_axis_range(str(code))
    
    if rng is None:
        return jsonify({"error": f"Axis code {code} not found"}), 404

    axis_min, axis_max, fuzz, flat = rng
    return jsonify({
        "axis_code": code, 
        "range": {
            "min": axis_min,
            "max": axis_max,
            "fuzz": fuzz,
            "flat": flat
        }
    })

@app.route("/joystick/axis_ranges")
def js_axis_ranges():
    if not js:
        return jsonify({"axis_ranges": {}}), 503
    
    formatted_ranges = {}
    for code, rng in js.get_axis_ranges().items():
        axis_min, axis_max, fuzz, flat = rng
        formatted_ranges[code] = {
            "min": axis_min,
            "max": axis_max,
            "fuzz": fuzz,
            "flat": flat
        }
        
    return jsonify({"axis_ranges": formatted_ranges})

