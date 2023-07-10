import time
import xair_api
import random

kind_id = "X32"
ip = "192.168.1.247"

mixer = xair_api.connect(kind_id, ip=ip)
mixer.__enter__()

print(mixer.validate_connection())

mixer.send("/ch/01/mix/on", 0)
print(mixer.query("/ch/01/mix/on"))
time.sleep(1)
mixer.send("/ch/01/mix/on", 1)
print(mixer.query("/ch/01/mix/on"))
time.sleep(1)
print(mixer.query("/ch/01/mix/on"))
time.sleep(1)
pass

def query_mixer(mixer, query):
    print(mixer.query(query))

# Define the set_eq_type function to set the EQ type
def set_eq_type(mixer, channel, eq_band, eq_type):
    mixer.send(f"/ch/{channel:02d}/eq/{eq_band}/type", eq_type)  # Set EQ type
    print(mixer.query(f"/ch/{channel:02d}/eq/{eq_band}/type"))  # Print the EQ type of the specified channel and EQ band
    time.sleep(1)  # Delay for 1 second

on = True
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/ch/06/mix/fader", str(val))
    on = ~on

mixer.send("/ch/01/mix/on", 1)
print(mixer.query("/ch/01/mix/on"))
mixer.send("/ch/01/mix/on", 0)
print(mixer.query("/ch/01/mix/on"))

# Toggle GATE on channel 1
mixer.send("/ch/01/gate/on", 1)
print(mixer.query("/ch/01/gate/on"))
time.sleep(1)

for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/ch/01/gate/thr", str(val))
    on = ~on

# GATE Threshold on channel 1
mixer.send("/ch/01/gate/thr", 0.500)
print(mixer.query("/ch/01/gate/on"))
time.sleep(1)
mixer.send("/ch/01/gate/thr", -1.000)
print(mixer.query("/ch/01/gate/on"))
time.sleep(1)
mixer.send("/ch/01/gate/thr", 0.000)
print(mixer.query("/ch/01/gate/on"))
time.sleep(1)

# Toggle GATE off channel 1
mixer.send("/ch/01/gate/on", 0)
print(mixer.query("/ch/01/gate/on"))
time.sleep(1)
pass

# Toggle DYNAMICS on channel 1
mixer.send("/ch/01/dyn/on", 1)
print(mixer.query("/ch/01/dyn/on"))
time.sleep(1)

for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/ch/01/dyn/thr", str(val))
    on = ~on

# Toggle DYNAMICS off channel 1
mixer.send("/ch/01/dyn/on", 0)
print(mixer.query("/ch/01/dyn/on"))
time.sleep(1)
pass

# Toggle EQ on channel 1
mixer.send("/ch/01/eq/on", 1)
print(mixer.query("/ch/01/eq/on"))
time.sleep(1)

# Set EQ type on channel 1, EQ band 2 to LCut
mixer.send("/ch/01/eq/2/5", 1)

# Set EQ type on channel 2, EQ band 2 to HCut
mixer.send("/ch/01/eq/4/0", 2)


# Toggle EQ off channel 1
mixer.send("/ch/01/eq/on", 0)
print(mixer.query("/ch/01/eq/on"))
time.sleep(1)
pass
