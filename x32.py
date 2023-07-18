import random
import time

def toggle_gate_on_channel(mixer, channel):
    # Toggle GATE on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/gate/on", 1)
    print(mixer.query(f"/ch/{channel:02}/gate/on"))
    time.sleep(1)
    on = True
    return on

def set_gate_threshold(mixer, channel, threshold):
    # Set GATE threshold on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/gate/thr", threshold)
    print(mixer.query(f"/ch/{channel:02}/gate/on"))
    time.sleep(1)

def toggle_gate_off_channel(mixer, channel):
    # Toggle GATE off on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/gate/on", 0)
    print(mixer.query(f"/ch/{channel:02}/gate/on"))
    time.sleep(1)

def toggle_dynamics_on_channel(mixer, channel):
    # Toggle DYNAMICS on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/dyn/on", 1)
    print(mixer.query(f"/ch/{channel:02}/dyn/on"))
    time.sleep(1)
    on = True
    return on

def toggle_dynamics_off_channel(mixer, channel):
    # Toggle DYNAMICS off on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/dyn/on", 0)
    print(mixer.query(f"/ch/{channel:02}/dyn/on"))
    time.sleep(1)

# Example usage:
channel = 1
mixer = YourMixerObject()  # Replace YourMixerObject with the actual mixer object you have

# Toggle GATE on channel 1
on_state = toggle_gate_on_channel(mixer, channel)

# Generate random GATE threshold values between -60 and 10
gate_threshold_values = [random.uniform(-60, 10) for _ in range(100)]

# Set GATE Threshold on channel 1 using the random values
for threshold in gate_threshold_values:
    set_gate_threshold(mixer, channel, threshold)
    on_state = ~on_state  # Toggle on/off state for the next iteration

# Toggle GATE off channel 1
toggle_gate_off_channel(mixer, channel)

# Toggle DYNAMICS on channel 1
on_state = toggle_dynamics_on_channel(mixer, channel)

# Generate random DYNAMICS threshold values between -60 and 10
dynamics_threshold_values = [random.uniform(-60, 10) for _ in range(100)]

# Set DYNAMICS Threshold on channel 1 using the random values
for threshold in dynamics_threshold_values:
    mixer.send(f"/ch/{channel:02}/dyn/thr", str(threshold))
    on_state = ~on_state  # Toggle on/off state for the next iteration

# Toggle DYNAMICS off channel 1
toggle_dynamics_off_channel(mixer, channel)

def toggle_eq_on_channel(mixer, channel):
    # Toggle EQ on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/eq/on", 1)
    print(mixer.query(f"/ch/{channel:02}/eq/on"))
    time.sleep(1)

def set_eq_band_type(mixer, channel, band, eq_type):
    # Set EQ type for a specific band on the specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/eq/{band}/{eq_type}", 1)

def toggle_eq_off_channel(mixer, channel):
    # Toggle EQ off on specified channel (1 or more)
    mixer.send(f"/ch/{channel:02}/eq/on", 0)
    print(mixer.query(f"/ch/{channel:02}/eq/on"))
    time.sleep(1)
    
    