import xair_api
import time
import math

kind_id = "X32"
ip = "192.168.1.247"

mixer = xair_api.connect(kind_id, ip=ip)
mixer.__enter__()

# Validate Connection
print(mixer.validate_connection())

# Set Channel Names
for channel in range(1, 33):
    mixer.strip[channel].config.name = f"Channel {channel}"

# Enable Channel Mix
for channel in range(1, 33):
    mixer.strip[channel].mix.on = True

# Query Channel Mix On/Off Status
print(mixer.query("/ch/01/mix/on"))

# Set Channel Mix On/Off Status
mixer.send("/ch/01/mix/on", 0)  # Turn off
time.sleep(1)
mixer.send("/ch/01/mix/on", 1)  # Turn on
time.sleep(1)

# Query Channel Mix On/Off Status
print(mixer.query("/ch/01/mix/on"))

# Query Channel Mix Filter
print(mixer.query("/ch/01/mix/filter"))

# Set Channel Mix Fader Levels
for channel in range(1, 33):
    mixer.send(f"/ch/{channel:02d}/mix/fader", "-20.0")  # Set fader level to -20.0 dB

# Mute/Unmute Channel Mix
for channel in range(1, 33):
    mixer.send(f"/ch/{channel:02d}/mix/on", 0)  # Mute channels
time.sleep(1)
for channel in range(1, 33):
    mixer.send(f"/ch/{channel:02d}/mix/on", 1)  # Unmute channels
time.sleep(1)

# Query Channel Mix Fader Levels
for channel in range(1, 33):
    print(mixer.query(f"/ch/{channel:02d}/mix/fader"))

# Multi-Track Recording Control
mixer.send("/record", 1)  # Start recording
time.sleep(5)  # Recording for 5 seconds
mixer.send("/record", 0)  # Stop recording

# DAW Integration - Set Track Volume
mixer.send("/dca/1/fader", "-10.0")  # Set DCA track 1 volume to -10.0 dB

# DAW Integration - Set Track Mute/Unmute
mixer.send("/mute/1", 1)  # Mute track 1
time.sleep(1)
mixer.send("/mute/1", 0)  # Unmute track 1
time.sleep(1)

# Generate wave formation for fader values
channels = range(1, 33)  # Channels to control in the wave formation
duration = 20  # Duration of the wave movement in seconds
frequency = 8.5  # Frequency of the wave in Hz
start_val = -40.0  # Starting fader value
end_val = -40.0  # Ending fader value

start_time = time.time()
while time.time() - start_time < duration:
    elapsed_time = time.time() - start_time
    t = elapsed_time * frequency * 2 * math.pi
    for channel in channels:
        val = (math.sin(t) + 1) * (end_val - start_val) / 2 + start_val
        mixer.send(f"/ch/{channel:02d}/mix/fader", str(val))
    time.sleep(0.05)  # Sleep for a short interval between fader updates

# Clean up: Reset values
mixer.send("/ch/01/mix/on", 1)  # Turn on channel 1
for channel in range(1, 33):
    mixer.strip[channel].config.name = ""  # Reset channel names
    mixer.strip[channel].mix.on = False  # Turn off channel mix
