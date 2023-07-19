import xair_api
import time
import math

kind_id = "X32"
ip = "192.168.1.247"

mixer = xair_api.connect(kind_id, ip=ip)
mixer.__enter__()

# Validate Connection
print(mixer.validate_connection())


#Simulate Channel EQ TEST
def simulate_channel_eq(mixer, channel_id):
    mixer.send(f"/ch/{channel_id}/eq/on", 1)  # Turn on Channel EQ
    time.sleep(1)

    eq_types = [0, 1, 2, 3, 4, 5]  # EQ Types: LCUT, LShv, PEQ, VEQ, HShv, HCut
    for eq_type in eq_types:
        mixer.send(f"/ch/{channel_id}/eq/1/type", eq_type)  # Set EQ type
        time.sleep(1)

    # Simulate EQ frequency adjustments
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(f"/ch/{channel_id}/eq/1/f", str(val))
        time.sleep(0.1)

    # Simulate EQ gain adjustments
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(f"/ch/{channel_id}/eq/1/g", str(val))
        time.sleep(0.1)

    # Simulate EQ Q adjustments
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(f"/ch/{channel_id}/eq/1/q", str(val))
        time.sleep(0.1)

    mixer.send(f"/ch/{channel_id}/eq/on", 0)  # Turn off Channel EQ
    time.sleep(1)
# Usage: Replace 'YOUR_MIXER_OBJECT' with the actual mixer object and 'YOUR_CHANNEL_ID' with the desired channel ID.

#Simulate Channel Mix and Pan TEST
def simulate_channel_mix_and_pan(mixer, channel_id):
    mixer.send(f"/ch/{channel_id}/mix/on", 1)  # Turn on Channel Mix
    time.sleep(1)

    mixer.send(f"/ch/{channel_id}/mix/pan", 0.0)  # Set initial pan to center
    time.sleep(1)

    # Simulate pan adjustments
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(f"/ch/{channel_id}/mix/pan", str(val))
        time.sleep(0.1)

    mixer.send(f"/ch/{channel_id}/mix/on", 0)  # Turn off Channel Mix
    time.sleep(1)


# Usage: Replace 'YOUR_MIXER_OBJECT' with the actual mixer object and 'YOUR_CHANNEL_ID' with the desired channel ID.
# For example, if you want to test channel 1, use simulate_channel_mix_and_pan(YOUR_MIXER_OBJECT, 1).
simulate_channel_mix_and_pan(YOUR_MIXER_OBJECT, YOUR_CHANNEL_ID)


#Simulate DCA and Mute TEST 
def simulate_dca_and_mute(mixer, channel_id):
    mixer.send(f"/ch/{channel_id}/grp/dca", 1)  # Set DCA to 1 for Channel
    time.sleep(1)

    mixer.send(f"/ch/{channel_id}/grp/mute", 1)  # Mute the Group for Channel
    time.sleep(1)

    mixer.send(f"/ch/{channel_id}/grp/dca", 0)  # Unassign DCA for Channel
    time.sleep(1)

    mixer.send(f"/ch/{channel_id}/grp/mute", 0)  # Unmute the Group for Channel
    time.sleep(1)


# Usage: Replace 'YOUR_MIXER_OBJECT' with the actual mixer object and 'YOUR_CHANNEL_ID' with the desired channel ID.
# For example, if you want to test channel 1, use simulate_dca_and_mute(YOUR_MIXER_OBJECT, 1).
simulate_dca_and_mute(YOUR_MIXER_OBJECT, YOUR_CHANNEL_ID)