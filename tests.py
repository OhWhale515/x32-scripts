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


def set_channel_mix_on_off(mixer, channel_id, mix_on):
    control_path = f"/ch/{channel_id:02}/mix/01/on"
    mixer.send(control_path, mix_on)
    print(mixer.query(control_path))
    time.sleep(1)

def set_channel_mix_level(mixer, channel_id, level):
    control_path = f"/ch/{channel_id:02}/mix/01/level"
    mixer.send(control_path, level)
    print(mixer.query(control_path))
    time.sleep(1)

def set_channel_mix_pan(mixer, channel_id, pan):
    control_path = f"/ch/{channel_id:02}/mix/01/pan"
    mixer.send(control_path, pan)
    print(mixer.query(control_path))
    time.sleep(1)

def set_channel_mix_type(mixer, channel_id, mix_type):
    control_path = f"/ch/{channel_id:02}/mix/01/type"
    mixer.send(control_path, mix_type)
    print(mixer.query(control_path))
    time.sleep(1)

def set_auxin_mix_on_off(mixer, auxin_id, mix_on):
    control_path = f"/auxin/{auxin_id:02}/mix/on"
    mixer.send(control_path, mix_on)
    print(mixer.query(control_path))
    time.sleep(1)

def set_auxin_mix_level(mixer, auxin_id, level):
    control_path = f"/auxin/{auxin_id:02}/mix/fader"
    mixer.send(control_path, level)
    print(mixer.query(control_path))
    time.sleep(1)

def set_auxin_mix_pan(mixer, auxin_id, pan):
    control_path = f"/auxin/{auxin_id:02}/mix/pan"
    mixer.send(control_path, pan)
    print(mixer.query(control_path))
    time.sleep(1)

def set_auxin_mix_type(mixer, auxin_id, mix_type):
    control_path = f"/auxin/{auxin_id:02}/mix/01/type"
    mixer.send(control_path, mix_type)
    print(mixer.query(control_path))
    time.sleep(1)

def set_fx_return_channel_mix_pan_follow(mixer, fxrtn_id, pan_follow):
    pan_follow_map = {"OFF": 0, "ON": 130}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/panFollow"
    mixer.send(control_path, pan_follow_map[pan_follow])
    print(mixer.query(control_path))
    time.sleep(1)

def set_fx_return_channel_grp_dca(mixer, fxrtn_id, dca_value):
    control_path = f"/fxrtn/{fxrtn_id:02}/grp/dca"
    mixer.send(control_path, dca_value)
    print(mixer.query(control_path))
    time.sleep(1)

def set_fx_return_channel_grp_mute(mixer, fxrtn_id, mute_value):
    control_path = f"/fxrtn/{fxrtn_id:02}/grp/mute"
    mixer.send(control_path, mute_value)
    print(mixer.query(control_path))
    time.sleep(1)

def test_script(mixer):
    # Test Channel Mix On/Off
    for channel_id in range(1, 17):
        set_channel_mix_on_off(mixer, channel_id, 1)  # Turn on Mix for all channels
        set_channel_mix_on_off(mixer, channel_id, 0)  # Turn off Mix for all channels

    # Test Channel Mix Level
    for channel_id in range(1, 17):
        level = random.uniform(-60, 10)
        set_channel_mix_level(mixer, channel_id, str(level))

    # Test Channel Mix Pan
    for channel_id in range(1, 17):
        pan = random.uniform(-100, 100)
        set_channel_mix_pan(mixer, channel_id, str(pan))

    # Test Channel Mix Type
    for channel_id in range(1, 17):
        mix_type = random.randint(0, 5)
        set_channel_mix_type(mixer, channel_id, mix_type)

    # Test Auxin Mix On/Off
    for auxin_id in range(1, 9):
        set_auxin_mix_on_off(mixer, auxin_id, 1)  # Turn on Mix for all auxin channels
        set_auxin_mix_on_off(mixer, auxin_id, 0)  # Turn off Mix for all auxin channels

    # Test Auxin Mix Level
    for auxin_id in range(1, 9):
        level = random.uniform(0, 1)
        set_auxin_mix_level(mixer, auxin_id, str(level))

    # Test Auxin Mix Pan
    for auxin_id in range(1, 9):
        pan = random.uniform(-100, 100)
        set_auxin_mix_pan(mixer, auxin_id, str(pan))

    # Test Auxin Mix Type
    for auxin_id in range(1, 9):
        mix_type = random.randint(0, 5)
        set_auxin_mix_type(mixer, auxin_id, mix_type)

    # Test FX Return Mix Pan Follow
    for fxrtn_id in range(1, 9):
        set_fx_return_channel_mix_pan_follow(mixer, fxrtn_id, "ON")  # Pan follow is ON for all FX Returns
        set_fx_return_channel_mix_pan_follow(mixer, fxrtn_id, "OFF")  # Pan follow is OFF for all FX Returns


# Test FX Return DCA
    for fxrtn_id in range(1, 9):
        dca_value = random.randint(0, 255)
        set_fx_return_channel_grp_dca(mixer, fxrtn_id, dca_value)

    # Test FX Return Mute
    for fxrtn_id in range(1, 9):
        mute_value = random.randint(0, 63)
        set_fx_return_channel_grp_mute(mixer, fxrtn_id, mute_value)

# Test FX Return EQ Settings
    for fxrtn_id in range(1, 9):
        eq_on = random.randint(0, 1)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/eq/on", eq_on)
        for eq_band in range(1, 5):
            eq_type = random.randint(0, 5)
            eq_f = random.uniform(20.0, 20000.0)
            eq_g = random.uniform(-15.0, 15.0)
            eq_q = random.uniform(10.0, 72.0)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/type", eq_type)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/f", eq_f)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/g", eq_g)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/q", eq_q)
            print(f"FX Return {fxrtn_id} EQ Band {eq_band} settings:")
            print(mixer.query(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/type"))
            print(mixer.query(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/f"))
            print(mixer.query(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/g"))
            print(mixer.query(f"/fxrtn/{fxrtn_id:02}/eq/{eq_band}/q"))
            time.sleep(1)

# Test FX Return Mix Settings
    for fxrtn_id in range(1, 9):
        mix_on = random.randint(0, 1)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/on", mix_on)
        mix_fader = random.uniform(0.0, 1.0)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/fader", mix_fader)
        mix_st = random.randint(0, 1)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/st", mix_st)
        mix_pan = random.uniform(-100.0, 100.0)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/pan", mix_pan)
        mix_mono = random.randint(0, 1)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/mono", mix_mono)
        mix_mlevel = random.uniform(-90.0, 10.0)
        mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/mlevel", mix_mlevel)

        for mix_bus in range(1, 17):
            mix_bus_on = random.randint(0, 1)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/{mix_bus:02}/on", mix_bus_on)
            mix_bus_level = random.uniform(-90.0, 10.0)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/{mix_bus:02}/level", mix_bus_level)
            mix_bus_pan = random.uniform(-100.0, 100.0)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/{mix_bus:02}/pan", mix_bus_pan)
            mix_bus_type = random.randint(0, 5)
            mixer.send(f"/fxrtn/{fxrtn_id:02}/mix/{mix_bus:02}/type", mix_bus_type)
            time.sleep(1)

    print("Test script completed!")

test_script(mixer)