import time
import xair_api
import random

kind_id = "X32"
ip = "192.168.1.247"

mixer = xair_api.connect(kind_id, ip=ip)
mixer.__enter__()

print(mixer.validate_connection())
def toggle_gate_on_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/gate/on", 1)
    time.sleep(1)
    on = True
    return on

def set_gate_threshold(mixer, channel, threshold):
    mixer.send(f"/ch/{channel:02}/gate/thr", threshold)
    time.sleep(1)

def toggle_gate_off_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/gate/on", 0)
    time.sleep(1)

def toggle_dynamics_on_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/dyn/on", 1)
    time.sleep(1)
    on = True
    return on

def toggle_dynamics_off_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/dyn/on", 0)
    time.sleep(1)

def channel_link_on(mixer, channel1, channel2):
    mixer.send(f"/config/chlink/{channel1}-{channel2}/on", 1)
    time.sleep(1)

def channel_link_off(mixer, channel1, channel2):
    mixer.send(f"/config/chlink/{channel1}-{channel2}/on", 0)
    time.sleep(1)

def aux_link_on(mixer, aux1, aux2):
    mixer.send(f"/config/auxlink/{aux1}-{aux2}/on", 1)
    time.sleep(1)

def aux_link_off(mixer, aux1, aux2):
    mixer.send(f"/config/auxlink/{aux1}-{aux2}/on", 0)
    time.sleep(1)

def fx_link_on(mixer, fx1, fx2):
    mixer.send(f"/config/fxlink/{fx1}-{fx2}/on", 1)
    time.sleep(1)

def fx_link_off(mixer, fx1, fx2):
    mixer.send(f"/config/fxlink/{fx1}-{fx2}/on", 0)
    time.sleep(1)

def group_selection_mute_on(mixer, group):
    mixer.send(f"/config/mute/{group}/on", 1)
    time.sleep(1)

def group_selection_mute_off(mixer, group):
    mixer.send(f"/config/mute/{group}/on", 0)
    time.sleep(1)

def generate_random_threshold_values(count, lower_bound=-60, upper_bound=10):
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]



