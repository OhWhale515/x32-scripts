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







# Channel Link CH1-CH2 On
mixer.send("/config/chlink/1-2/on", 1)
print(mixer.query("/config/chlink/1-2/on"))
time.sleep(1)
# Channel Link CH1-CH2 Off
mixer.send("/config/chlink/1-2/on", 0)
print(mixer.query("/config/chlink/1-2/on"))
time.sleep(1)
# AUX Link AUX1-AUX2 On
mixer.send("/config/auxlink/1-2/on", 1)
print(mixer.query("/config/auxlink/1-2/on"))
time.sleep(1)

# AUX Link AUX1-AUX2 Off
mixer.send("/config/auxlink/1-2/on", 0)
print(mixer.query("/config/auxlink/1-2/on"))
time.sleep(1)

# FX Link FX1-FX2 On
mixer.send("/config/fxlink/1-2/on", 1)
print(mixer.query("/config/fxlink/1-2/on"))
time.sleep(1) 

# FX Link FX1-FX2 Off
mixer.send("/config/fxlink/1-2/on", 0)
print(mixer.query("/config/fxlink/1-2/on"))
time.sleep(1)

# Group Selection Mute On
mixer.send("/config/mute/1/on", 1)
print(mixer.query("/config/mute/1/on"))
time.sleep(1) 

# Group Selection Mute Off
mixer.send("/config/mute/1/on", 0)
print(mixer.query("/config/mute/1/on"))
time.sleep(1)

# mtx link  On
mixer.send("/config/mtxlink/1/on", 1)
print(mixer.query("/config/mtxlink/1/on"))
time.sleep(1)

# mtx link  Off
mixer.send("/config/mtxlink/1/on", 0)
print(mixer.query("/config/mtxlink/1/on"))
time.sleep(1)

# link config hadly On/ Sets Delay & HA link
mixer.send("/config/linkcfg/hadly/on", 1)
print(mixer.query("/config/mtxlink/1/on"))
time.sleep(1)

# link config hadly Off
mixer.send("/config/linkcfg/hadly/on", 0)
print(mixer.query("/config/mtxlink/1/on"))
time.sleep(1)

# link config EQ On/ Sets EQ link
mixer.send("/config/linkcfg/eq/on", 1)
print(mixer.query("/config/linkcfg/1/on"))
time.sleep(1)

# link config EQ Off/ Removes EQ link
mixer.send("/config/linkcfg/eq/on", 0)
print(mixer.query("/config/linkcfg/eq/on"))
time.sleep(1)

# link config dynamics On
mixer.send("/config/linkcfg/dyn/on", 1)
print(mixer.query("/config/linkcfg/dyn/on"))
time.sleep(1)

# link config dynamics Off
mixer.send("/config/linkcfg/dyn/on", 0)
print(mixer.query("/config/linkcfg/dyn/on"))
time.sleep(1)

# link config FDR Mute On
mixer.send("/config/linkcfg/fdrmute/on", 1)
print(mixer.query("/config/linkcfg/fdrmute/on"))
time.sleep(1)

# link config FDR Mute Off
mixer.send("/config/linkcfg/fdrmute/on", 0)
print(mixer.query("/config/linkcfg/fdrmute/on"))
time.sleep(1)

# Mono Mode LR+M 
mixer.send("/config/mono/mode", 1)
print(mixer.query("/config/mono/mode"))
time.sleep(1)

# Mono Mode LCR 
mixer.send("/config/mono/mode", 0)
print(mixer.query("/config/mono/mode"))
time.sleep(1)

# Mono Mode Link On
mixer.send("/config/mono/link", 1)
print(mixer.query("/config/mono/link"))
time.sleep(1)

# Mono Mode Link Off
mixer.send("/config/mono/link", 0)
print(mixer.query("/config/mono/link"))
time.sleep(1)

# Mono Mode Link On
mixer.send("/config/mono/link", 1)
print(mixer.query("/config/mono/link"))
time.sleep(1)

# Solo dB Level
mixer.send("/config/solo/level", 10.0)
print(mixer.query("/config/solo/level"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/solo/level", str(val))
    on = ~on
time.sleep(1)

# Solo dB Level
mixer.send("/config/solo/level", 10.0)
print(mixer.query("/config/solo/level"))
time.sleep(1)

# Solo Source Options Off
mixer.send("/config/solo/source", 0)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option LR
mixer.send("/config/solo/source", 1)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option LR+C
mixer.send("/config/solo/source", 2)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option LRPFL
mixer.send("/config/solo/source", 3)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option LRAFL
mixer.send("/config/solo/source", 4)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option AUX56
mixer.send("/config/solo/source", 5)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Option AUX78
mixer.send("/config/solo/source", 6)
print(mixer.query("/config/solo/source"))
time.sleep(1)

# Solo Source Trim dB Level
mixer.send("/config/solo/sourcetrim", 10.0)
print(mixer.query("/config/solo/sourcetrim"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/solo/sourcetrim", str(val))
    on = ~on
time.sleep(1) 

# Solo Channel Mode PFL
mixer.send("/config/solo/chmode", 0)
print(mixer.query("/config/solo/chmode"))
time.sleep(1)

# Solo Channel Mode AFL
mixer.send("/config/solo/chmode", 1)
print(mixer.query("/config/solo/chmode"))
time.sleep(1)

# Solo Bus Mode PFL
mixer.send("/config/solo/chmode", 0)
print(mixer.query("/config/solo/chmode"))
time.sleep(1)

# Solo Bus Mode AFL
mixer.send("/config/solo/busmode", 1)
print(mixer.query("/config/solo/busmode"))
time.sleep(1)

# Solo DCA Mode PFL
mixer.send("/config/solo/dcamode", 0)
print(mixer.query("/config/solo/dcamode"))
time.sleep(1)

# Solo DCA Mode AFL
mixer.send("/config/solo/dcamode", 1)
print(mixer.query("/config/solo/dcamode"))
time.sleep(1)

# Solo Exclusive Mode On
mixer.send("/config/solo/exclusive", 0)
print(mixer.query("/config/solo/exclusive"))
time.sleep(1)

# Solo Exclusive Mode Off
mixer.send("/config/solo/exclusive", 1)
print(mixer.query("/config/solo/exclusive"))
time.sleep(1)

# Solo Follow Select Mode On
mixer.send("/config/solo/followsel", 0)
print(mixer.query("/config/solo/followsel"))
time.sleep(1)

# Solo Follow Select  Mode Off
mixer.send("/config/solo/followsel", 1)
print(mixer.query("/config/solo/followsel"))
time.sleep(1)

# Solo Follow Solo Mode On
mixer.send("/config/solo/followsolo", 0)
print(mixer.query("/config/solo/followsolo"))
time.sleep(1)

# Solo Follow Solo Mode Off
mixer.send("/config/solo/followsolo", 1)
print(mixer.query("/config/solo/followsolo"))
time.sleep(1)

# Solo DimAtt dB Level
mixer.send("/config/solo/dimatt", 10.0)
print(mixer.query("/config/solo/dimatt"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/solo/dimatt", str(val))
    on = ~on
time.sleep(1)

# Solo Dim Mode On
mixer.send("/config/solo/dim", 0)
print(mixer.query("/config/solo/dim"))
time.sleep(1)

# Solo Dim Mode Off
mixer.send("/config/solo/dim", 1)
print(mixer.query("/config/solo/dim"))
time.sleep(1)

# Solo Mono Mode On
mixer.send("/config/solo/mono", 0)
print(mixer.query("/config/solo/mono"))
time.sleep(1)

# Solo Mono Mode Off
mixer.send("/config/solo/mono", 1)
print(mixer.query("/config/solo/mono"))
time.sleep(1)

# Solo Delay Mode On
mixer.send("/config/solo/delay", 0)
print(mixer.query("/config/solo/delay"))
time.sleep(1)

# Solo Delay Mode Off
mixer.send("/config/solo/delay", 1)
print(mixer.query("/config/solo/delay"))
time.sleep(1)

# Solo Delay Time ms Level
mixer.send("/config/solo/delaytime", 10.0)
print(mixer.query("/config/solo/delaytime"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/solo/delaytime", str(val))
    on = ~on
time.sleep(1)

# Solo Master Control Mode On
mixer.send("/config/solo/masterctrl", 0)
print(mixer.query("/config/solo/masterctrl"))
time.sleep(1)

# Solo Master Control Mode Off
mixer.send("/config/solo/masterctrl", 1)
print(mixer.query("/config/solo/masterctrl"))
time.sleep(1)

# Solo Mute Mode On
mixer.send("/config/solo/mute", 0)
print(mixer.query("/config/solo/mute"))
time.sleep(1)

# Solo Mute Mode Off
mixer.send("/config/solo/mute", 1)
print(mixer.query("/config/solo/mute"))
time.sleep(1)

# Solo dimpfl Mode On
mixer.send("/config/solo/dimpfl", 0)
print(mixer.query("/config/solo/dimpfl"))
time.sleep(1)

# Solo dimpfl Mode Off
mixer.send("/config/solo/dimpfl", 1)
print(mixer.query("/config/solo/dimpfl"))
time.sleep(1)

# Talk Mode On
mixer.send("/config/talk/enable", 0)
print(mixer.query("/config/talk/enable"))
time.sleep(1)

# Talk Mode Off
mixer.send("/config/talk/enable", 1)
print(mixer.query("/config/talk/enable"))
time.sleep(1)

# Talk Source INT
mixer.send("/config/talk/source", 0)
print(mixer.query("/config/talk/source"))
time.sleep(1)

# Talk Source ENT
mixer.send("/config/talk/source", 1)
print(mixer.query("/config/talk/source"))
time.sleep(1)

# Talk dB Level A
mixer.send("/config/A/level", 10.0)
print(mixer.query("/config/A/level"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/A/level", str(val))
    on = ~on
time.sleep(1)

# Talk dB Level B
mixer.send("/config/B/level", 10.0)
print(mixer.query("/config/B/level"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/B/level", str(val))
    on = ~on
time.sleep(1)

# Talk Latch A On
mixer.send("/config/talk/A/latch", 0)
print(mixer.query("/config/talk/A/latch"))
time.sleep(1)

# Talk Latch A Off
mixer.send("/config/talk/A/latch", 1)
print(mixer.query("/config/talk/A/latch"))
time.sleep(1)

# Talk Latch B On
mixer.send("/config/talk/B/latch", 0)
print(mixer.query("/config/talk/B/latch"))
time.sleep(1)

# Talk Latch B Off
mixer.send("/config/talk/B/latch", 1)
print(mixer.query("/config/talk/B/latch"))
time.sleep(1)

# Talk Dim A On
mixer.send("/config/talk/A/dim", 0)
print(mixer.query("/config/talk/A/dim"))
time.sleep(1)

# Talk Dim A Off
mixer.send("/config/talk/A/dim", 1)
print(mixer.query("/config/talk/A/dim"))
time.sleep(1)

# Talk Dim B On
mixer.send("/config/talk/B/dim", 0)
print(mixer.query("/config/talk/B/dim"))
time.sleep(1)

# Talk Dim B Off
mixer.send("/config/talk/B/dim", 1)
print(mixer.query("/config/talk/B/dim"))
time.sleep(1)

# Talk Dest Mapping A
mixer.send("/config/talk/A/destmap", 0)
print(mixer.query("/config/talk/A/destmap"))
for i in range(100):
    val = random.uniform(0, 10)
    mixer.send("/config/talk/A/destmap", str(val))
    on = ~on
time.sleep(1)

# Talk Dest Mapping B
mixer.send("/config/talk/A/destmap", 1)
print(mixer.query("/config/talk/B/destmap"))
for i in range(100):
    val = random.uniform(0, 10)
    mixer.send("/config/talk/B/destmap", str(val))
    on = ~on
time.sleep(1)

# Osc dB Level
mixer.send("/config/osc/level", 1)
print(mixer.query("/config/osc/level"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/osc/level", str(val))
    on = ~on
time.sleep(1)

# Osc f1 Hertz Level
mixer.send("/config/osc/f1", 1)
print(mixer.query("/config/osc/f1"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/osc/f1", str(val))
    on = ~on
time.sleep(1)

# Osc f2 Hertz Level
mixer.send("/config/osc/f2", 1)
print(mixer.query("/config/osc/f2"))
for i in range(100):
    val = random.uniform(-60, 10)
    mixer.send("/config/osc/f2", str(val))
    on = ~on
time.sleep(1)

# OSC fsel Configuration
mixer.send("/config/osc/fsel", 0)
print(mixer.query("/config/osc/fsel"))
time.sleep(1)

# OSC SINE Type Configuration 
mixer.send("/config/talk/osc/type", 0)
print(mixer.query("/config/talk/osc/type"))
time.sleep(1)

# OSC PINK Type Configuration 
mixer.send("/config/talk/osc/type", 1)
print(mixer.query("/config/talk/osc/type"))
time.sleep(1)

# OSC WHITE Type Configuration 
mixer.send("/config/talk/osc/type", 2)
print(mixer.query("/config/talk/osc/type"))
time.sleep(1)

# OSC Mix Bus 1 Destination Configuration (MixBus 1-16)
mixer.send("/config/osc/dest", 0)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

# OSC Left Destination Configuration 
mixer.send("/config/osc/dest", 17)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

# OSC Right Destination Configuration 
mixer.send("/config/osc/dest", 18)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

# OSC Left+Right Destination Configuration 
mixer.send("/config/osc/dest", 19)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

# OSC M/C Destination Configuration 
mixer.send("/config/osc/dest", 20)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

# OSC Matrix 1 Destination Configuration (Matrix1-6) 
mixer.send("/config/osc/dest", 21)
print(mixer.query("/config/osc/dest"))
time.sleep(1)

#User Route Outs OUTPUTS 01-48 CONFIGURATIONS
# User Route OFF Outs
mixer.send("/config/userrout/out/01", 0)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Local In 1-32 int 1-32
mixer.send("/config/userrout/out/01", 1)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# AES50-A 1-48 int 33-80
mixer.send("/config/userrout/out/01", 33)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# AES50-B 1-48 int 81-128
mixer.send("/config/userrout/out/01", 81)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Card In 1-32 int 129-160
mixer.send("/config/userrout/out/01", 129)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Aux In 1-6 int 161-166
mixer.send("/config/userrout/out/01", 161)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# TB Internal 
mixer.send("/config/userrout/out/01", 167)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# TB External 
mixer.send("/config/userrout/out/01", 168)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Outputs 1-16 int 169-184 
mixer.send("/config/userrout/out/01", 169)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# P16 1-16 int 185-200 
mixer.send("/config/userrout/out/01", 185)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# AUX 1-6 int 201-206 
mixer.send("/config/userrout/out/01", 201)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Monitor Left
mixer.send("/config/userrout/out/01", 207)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

# Monitor Right
mixer.send("/config/userrout/out/01", 208)
print(mixer.query("/config/userrout/out/01"))
time.sleep(1)

#User Route Outs INPUTS 01-32 CONFIGURATIONS
# User Route OFF Outs
mixer.send("/config/userrout/in/01", 0)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# Local In 1-32 int 1-32
mixer.send("/config/userrout/in/01", 1)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# AES50-A 1-48 int 33-80
mixer.send("/config/userrout/in/01", 33)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# AES50-B 1-48 int 81-128
mixer.send("/config/userrout/in/01", 81)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# Card In 1-32 int 129-160
mixer.send("/config/userrout/in/01", 129)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# Aux In 1-6 int 161-166
mixer.send("/config/userrout/in/01", 161)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# TB Internal 
mixer.send("/config/userrout/in/01", 167)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# TB External 
mixer.send("/config/userrout/in/01", 168)
print(mixer.query("/config/userrout/in/01"))
time.sleep(1)

# Route Switch Record
mixer.send("/config/routing/routswitch", 0)
print(mixer.query("/config/routing/routswitch"))
time.sleep(1)

# Route Switch Playback
mixer.send("/config/routing/routswitch", 1)
print(mixer.query("/config/routing/routswitch"))
time.sleep(1)

# Input Routing 1-32
# AN1-8
mixer.send("/config/routing/IN/1-8", 0)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# AN9-16
mixer.send("/config/routing/IN/1-8", 1)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# AN17-24
mixer.send("/config/routing/IN/1-8", 2)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# AN25-32
mixer.send("/config/routing/IN/1-8", 3)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A1-8
mixer.send("/config/routing/IN/1-8", 4)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A9-16
mixer.send("/config/routing/IN/1-8", 5)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A17-24
mixer.send("/config/routing/IN/1-8", 6)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A25-32
mixer.send("/config/routing/IN/1-8", 7)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A33-40
mixer.send("/config/routing/IN/1-8", 8)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# A41-48
mixer.send("/config/routing/IN/1-8", 9)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B1-8
mixer.send("/config/routing/IN/1-8", 10)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B9-16
mixer.send("/config/routing/IN/1-8", 11)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B17-24
mixer.send("/config/routing/IN/1-8", 12)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B25-32
mixer.send("/config/routing/IN/1-8", 13)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B33-40
mixer.send("/config/routing/IN/1-8", 14)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# B41-48
mixer.send("/config/routing/IN/1-8", 15)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# CARD 1-8
mixer.send("/config/routing/IN/1-8", 16)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# CARD 9-16
mixer.send("/config/routing/IN/1-8", 17)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# CARD 17-24
mixer.send("/config/routing/IN/1-8", 18)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# CARD 25-32
mixer.send("/config/routing/IN/1-8", 19)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# UIN 1-8
mixer.send("/config/routing/IN/1-8", 20)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# UIN 9-16
mixer.send("/config/routing/IN/1-8", 21)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# UIN 17-24
mixer.send("/config/routing/IN/1-8", 22)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# UIN 25-32
mixer.send("/config/routing/IN/1-8", 23)
print(mixer.query("/config/routing/IN/1-8"))
time.sleep(1)

# AUX Routing Configurations
# AUX1-4
mixer.send("/config/routing/IN/AUX", 0)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# AN1-2
mixer.send("/config/routing/IN/AUX", 1)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# AN1-4
mixer.send("/config/routing/IN/AUX", 2)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# AN1-6
mixer.send("/config/routing/IN/AUX", 3)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# A1-2
mixer.send("/config/routing/IN/AUX", 4)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# A1-4
mixer.send("/config/routing/IN/AUX", 5)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# A1-6
mixer.send("/config/routing/IN/AUX", 6)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# B1-2
mixer.send("/config/routing/IN/AUX", 7)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# B1-4
mixer.send("/config/routing/IN/AUX", 8)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# B1-6
mixer.send("/config/routing/IN/AUX", 9)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# CARD1-2
mixer.send("/config/routing/IN/AUX", 10)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# CARD1-4
mixer.send("/config/routing/IN/AUX", 11)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# CARD1-6
mixer.send("/config/routing/IN/AUX", 12)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)


# UIN1-2
mixer.send("/config/routing/IN/AUX", 13)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# UIN1-4
mixer.send("/config/routing/IN/AUX", 14)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)

# UIN1-6
mixer.send("/config/routing/IN/AUX", 15)
print(mixer.query("/config/routing/IN/AUX"))
time.sleep(1)



# AES50-A Routing 1-48
# AN1-8
mixer.send("/config/routing/AES50A/1-8", 0)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AN9-16
mixer.send("/config/routing/AES50A/1-8", 1)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AN17-24
mixer.send("/config/routing/AES50A/1-8", 2)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AN25-32
mixer.send("/config/routing/AES50A/1-8", 3)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A1-8
mixer.send("/config/routing/AES50A/1-8", 4)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A9-16
mixer.send("/config/routing/AES50A/1-8", 5)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A17-24
mixer.send("/config/routing/AES50A/1-8", 6)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A25-32
mixer.send("/config/routing/AES50A/1-8", 7)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A33-40
mixer.send("/config/routing/AES50A/1-8", 8)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# A41-48
mixer.send("/config/routing/AES50A/1-8", 9)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B1-8
mixer.send("/config/routing/AES50A/1-8", 10)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B9-16
mixer.send("/config/routing/AES50A/1-8", 11)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B17-24
mixer.send("/config/routing/AES50A/1-8", 12)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B25-32
mixer.send("/config/routing/AES50A/1-8", 13)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B33-40
mixer.send("/config/routing/AES50A/1-8", 14)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# B41-48
mixer.send("/config/routing/AES50A/1-8", 15)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# CARD 1-8
mixer.send("/config/routing/AES50A/1-8", 16)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# CARD 9-16
mixer.send("/config/routing/AES50A/1-8", 17)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# CARD 17-24
mixer.send("/config/routing/AES50A/1-8", 18)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# CARD 25-32
mixer.send("/config/routing/AES50A/1-8", 19)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# OUT1-8
mixer.send("/config/routing/AES50A/1-8", 20)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# OUT9-16
mixer.send("/config/routing/AES50A/1-8", 21)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# P16 1-8
mixer.send("/config/routing/AES50A/1-8", 22)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# P16 9-16
mixer.send("/config/routing/AES50A/1-8", 23)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AUX1-6/Mon
mixer.send("/config/routing/AES50A/1-8", 24)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AuxIN1-6/TB
mixer.send("/config/routing/AES50A/1-8", 25)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT1-8
mixer.send("/config/routing/AES50A/1-8", 26)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT9-16
mixer.send("/config/routing/AES50A/1-8", 27)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT17-24
mixer.send("/config/routing/AES50A/1-8", 28)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT25-32
mixer.send("/config/routing/AES50A/1-8", 29)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT33-40
mixer.send("/config/routing/AES50A/1-8", 30)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UOUT41-48
mixer.send("/config/routing/AES50A/1-8", 31)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UIN 1-8
mixer.send("/config/routing/AES50A/1-8", 32)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UIN 9-16
mixer.send("/config/routing/AES50A/1-8", 33)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UIN 17-24
mixer.send("/config/routing/AES50A/1-8", 34)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# UIN 25-32
mixer.send("/config/routing/AES50A/1-8", 35)
print(mixer.query("/config/routing/AES50A/1-8"))
time.sleep(1)

# AES50-B Routing 1-48
# AN1-8
mixer.send("/config/routing/AES50B/1-8", 0)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# AN9-16
mixer.send("/config/routing/AES50B/1-8", 1)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# AN17-24
mixer.send("/config/routing/AES50B/1-8", 2)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# AN25-32
mixer.send("/config/routing/AES50B/1-8", 3)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A1-8
mixer.send("/config/routing/AES50B/1-8", 4)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A9-16
mixer.send("/config/routing/AES50B/1-8", 5)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A17-24
mixer.send("/config/routing/AES50B/1-8", 6)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A25-32
mixer.send("/config/routing/AES50B/1-8", 7)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A33-40
mixer.send("/config/routing/AES50B/1-8", 8)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# A41-48
mixer.send("/config/routing/AES50B/1-8", 9)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B1-8
mixer.send("/config/routing/AES50B/1-8", 10)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B9-16
mixer.send("/config/routing/AES50B/1-8", 11)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B17-24
mixer.send("/config/routing/AES50B/1-8", 12)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B25-32
mixer.send("/config/routing/AES50B/1-8", 13)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B33-40
mixer.send("/config/routing/AES50B/1-8", 14)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# B41-48
mixer.send("/config/routing/AES50B/1-8", 15)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# CARD 1-8
mixer.send("/config/routing/AES50B/1-8", 16)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# CARD 9-16
mixer.send("/config/routing/AES50B/1-8", 17)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# CARD 17-24
mixer.send("/config/routing/AES50B/1-8", 18)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# CARD 25-32
mixer.send("/config/routing/AES50B/1-8", 19)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# OUT1-8
mixer.send("/config/routing/AES50B/1-8", 20)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# OUT9-16
mixer.send("/config/routing/AES50B/1-8", 21)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# P16 1-8
mixer.send("/config/routing/AES50B/1-8", 22)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# P16 9-16
mixer.send("/config/routing/AES50B/1-8", 23)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# AUX1-6/Mon
mixer.send("/config/routing/AES50B/1-8", 24)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# AuxIN1-6/TB
mixer.send("/config/routing/AES50B/1-8", 25)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT1-8
mixer.send("/config/routing/AES50B/1-8", 26)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT9-16
mixer.send("/config/routing/AES50B/1-8", 27)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT17-24
mixer.send("/config/routing/AES50B/1-8", 28)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT25-32
mixer.send("/config/routing/AES50B/1-8", 29)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT33-40
mixer.send("/config/routing/AES50B/1-8", 30)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UOUT41-48
mixer.send("/config/routing/AES50B/1-8", 31)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UIN 1-8
mixer.send("/config/routing/AES50B/1-8", 32)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UIN 9-16
mixer.send("/config/routing/AES50B/1-8", 33)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UIN 17-24
mixer.send("/config/routing/AES50B/1-8", 34)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)

# UIN 25-32
mixer.send("/config/routing/AES50B/1-8", 35)
print(mixer.query("/config/routing/AES50B/1-8"))
time.sleep(1)


# CARD Routing 1-32
# AN1-8
mixer.send("/config/routing/CARD/1-8", 0)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# AN9-16
mixer.send("/config/routing/CARD/1-8", 1)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# AN17-24
mixer.send("/config/routing/CARD/1-8", 2)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# AN25-32
mixer.send("/config/routing/CARD/1-8", 3)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A1-8
mixer.send("/config/routing/CARD/1-8", 4)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A9-16
mixer.send("/config/routing/CARD/1-8", 5)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A17-24
mixer.send("/config/routing/CARD/1-8", 6)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A25-32
mixer.send("/config/routing/CARD/1-8", 7)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A33-40
mixer.send("/config/routing/CARD/1-8", 8)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# A41-48
mixer.send("/config/routing/CARD/1-8", 9)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B1-8
mixer.send("/config/routing/CARD/1-8", 10)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B9-16
mixer.send("/config/routing/CARD/1-8", 11)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B17-24
mixer.send("/config/routing/CARD/1-8", 12)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B25-32
mixer.send("/config/routing/CARD/1-8", 13)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B33-40
mixer.send("/config/routing/CARD/1-8", 14)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# B41-48
mixer.send("/config/routing/CARD/1-8", 15)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# CARD 1-8
mixer.send("/config/routing/CARD/1-8", 16)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# CARD 9-16
mixer.send("/config/routing/CARD/1-8", 17)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# CARD 17-24
mixer.send("/config/routing/CARD/1-8", 18)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# CARD 25-32
mixer.send("/config/routing/CARD/1-8", 19)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# OUT1-8
mixer.send("/config/routing/CARD/1-8", 20)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# OUT9-16
mixer.send("/config/routing/CARD/1-8", 21)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# P16 1-8
mixer.send("/config/routing/CARD/1-8", 22)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# P16 9-16
mixer.send("/config/routing/CARD/1-8", 23)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# AUX1-6/Mon
mixer.send("/config/routing/CARD/1-8", 24)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# AuxIN1-6/TB
mixer.send("/config/routing/CARD/1-8", 25)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT1-8
mixer.send("/config/routing/CARD/1-8", 26)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT9-16
mixer.send("/config/routing/CARD/1-8", 27)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT17-24
mixer.send("/config/routing/CARD/1-8", 28)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT25-32
mixer.send("/config/routing/CARD/1-8", 29)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT33-40
mixer.send("/config/routing/CARD/1-8", 30)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UOUT41-48
mixer.send("/config/routing/CARD/1-8", 31)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UIN 1-8
mixer.send("/config/routing/CARD/1-8", 32)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UIN 9-16
mixer.send("/config/routing/CARD/1-8", 33)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UIN 17-24
mixer.send("/config/routing/CARD/1-8", 34)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)

# UIN 25-32
mixer.send("/config/routing/CARD/1-8", 35)
print(mixer.query("/config/routing/CARD/1-8"))
time.sleep(1)



# OUTPUT Routing 1-4 & 9-12
# AN1-4
mixer.send("/config/routing/OUT/1-4", 0)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# AN9-12
mixer.send("/config/routing/OUT/1-4", 1)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# AN17-20
mixer.send("/config/routing/OUT/1-4", 2)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# AN25-28
mixer.send("/config/routing/OUT/1-4", 3)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A1-4
mixer.send("/config/routing/OUT/1-4", 4)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A9-12
mixer.send("/config/routing/OUT/1-4", 5)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A17-20
mixer.send("/config/routing/OUT/1-4", 6)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A25-28
mixer.send("/config/routing/OUT/1-4", 7)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A33-36
mixer.send("/config/routing/OUT/1-4", 8)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# A41-44
mixer.send("/config/routing/OUT/1-4", 9)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B1-4
mixer.send("/config/routing/OUT/1-4", 10)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B9-12
mixer.send("/config/routing/OUT/1-4", 11)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B17-20
mixer.send("/config/routing/OUT/1-4", 12)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B25-28
mixer.send("/config/routing/OUT/1-4", 13)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B33-46
mixer.send("/config/routing/OUT/1-4", 14)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# B41-44
mixer.send("/config/routing/OUT/1-4", 15)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# CARD 1-4
mixer.send("/config/routing/OUT/1-4", 16)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# CARD 9-12
mixer.send("/config/routing/OUT/1-4", 17)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# CARD 17-20
mixer.send("/config/routing/OUT/1-4", 18)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# CARD 25-28
mixer.send("/config/routing/OUT/1-4", 19)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# OUT1-4
mixer.send("/config/routing/OUT/1-4", 20)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# OUT9-12
mixer.send("/config/routing/OUT/1-4", 21)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# P16 1-4
mixer.send("/config/routing/OUT/1-4", 22)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# P16 9-12
mixer.send("/config/routing/OUT/1-4", 23)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# AUX/CR
mixer.send("/config/routing/OUT/1-4", 24)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# AUX/TB
mixer.send("/config/routing/OUT/1-4", 25)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT1-4
mixer.send("/config/routing/OUT/1-4", 26)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT9-12
mixer.send("/config/routing/OUT/1-4", 27)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT17-20
mixer.send("/config/routing/OUT/1-4", 28)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT25-28
mixer.send("/config/routing/OUT/1-48", 29)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT33-36
mixer.send("/config/routing/OUT/1-4", 30)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UOUT41-44
mixer.send("/config/routing/OUT/1-4", 31)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UIN 1-4
mixer.send("/config/routing/OUT/1-4", 32)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UIN 9-12
mixer.send("/config/routing/OUT/1-4", 33)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UIN 17-20
mixer.send("/config/routing/OUT/1-4", 34)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)

# UIN 25-28
mixer.send("/config/routing/OUT/1-4", 35)
print(mixer.query("/config/routing/OUT/1-4"))
time.sleep(1)



# OUTPUT Routing 5-8 & 13-16
# AN5-8
mixer.send("/config/routing/OUT/5-8", 0)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# AN13-16
mixer.send("/config/routing/OUT/5-8", 1)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# AN21-24
mixer.send("/config/routing/OUT/5-8", 2)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# AN29-32
mixer.send("/config/routing/OUT/5-8", 3)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A5-8
mixer.send("/config/routing/OUT/5-8", 4)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A13-16
mixer.send("/config/routing/OUT/5-8", 5)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A21-24
mixer.send("/config/routing/OUT/5-8", 6)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A29-32
mixer.send("/config/routing/OUT/5-8", 7)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A37-40
mixer.send("/config/routing/OUT/5-8", 8)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# A45-48
mixer.send("/config/routing/OUT/5-8", 9)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B5-8
mixer.send("/config/routing/OUT/5-8", 10)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B13-16
mixer.send("/config/routing/OUT/5-8", 11)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B21-24
mixer.send("/config/routing/OUT/5-8", 12)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B29-32
mixer.send("/config/routing/OUT/5-8", 13)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B37-40
mixer.send("/config/routing/OUT/5-8", 14)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# B45-48
mixer.send("/config/routing/OUT/5-8", 15)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# CARD 5-8
mixer.send("/config/routing/OUT/5-8", 16)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# CARD 13-16
mixer.send("/config/routing/OUT/5-8", 17)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# CARD 21-24
mixer.send("/config/routing/OUT/5-8", 18)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# CARD 29-32
mixer.send("/config/routing/OUT/5-8", 19)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# OUT5-8
mixer.send("/config/routing/OUT/5-8", 20)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# OUT13-16
mixer.send("/config/routing/OUT/5-8", 21)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# P16 5-8
mixer.send("/config/routing/OUT/5-8", 22)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# P16 13-16
mixer.send("/config/routing/OUT/5-8", 23)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# AUX/CR
mixer.send("/config/routing/OUT/5-8", 24)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# AUX/TB
mixer.send("/config/routing/OUT/5-8", 25)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT5-8
mixer.send("/config/routing/OUT/5-8", 26)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT13-16
mixer.send("/config/routing/OUT/5-8", 27)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT21-24
mixer.send("/config/routing/OUT/5-8", 28)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT29-32
mixer.send("/config/routing/OUT/5-8", 29)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT37-40
mixer.send("/config/routing/OUT/5-8", 30)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UOUT45-48
mixer.send("/config/routing/OUT/5-8", 31)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UIN 5-8
mixer.send("/config/routing/OUT/5-8", 32)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UIN 13-16
mixer.send("/config/routing/OUT/5-8", 33)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UIN 21-24
mixer.send("/config/routing/OUT/5-8", 34)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)

# UIN 29-32
mixer.send("/config/routing/OUT/5-8", 35)
print(mixer.query("/config/routing/OUT/5-8"))
time.sleep(1)



# PLAY Routing 1-32
# AN1-8
mixer.send("/config/routing/PLAY/1-8", 0)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# AN9-16
mixer.send("/config/routing/PLAY/1-8", 1)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# AN17-24
mixer.send("/config/routing/PLAY/1-8", 2)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# AN25-32
mixer.send("/config/routing/PLAY/1-8", 3)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A1-8
mixer.send("/config/routing/PLAY/1-8", 4)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A9-16
mixer.send("/config/routing/PLAY/1-8", 5)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A17-24
mixer.send("/config/routing/PLAY/1-8", 6)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A25-32
mixer.send("/config/routing/PLAY/1-8", 7)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A33-40
mixer.send("/config/routing/PLAY/1-8", 8)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# A41-48
mixer.send("/config/routing/PLAY/1-8", 9)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B1-8
mixer.send("/config/routing/PLAY/1-8", 10)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B9-16
mixer.send("/config/routing/PLAY/1-8", 11)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B17-24
mixer.send("/config/routing/PLAY/1-8", 12)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B25-32
mixer.send("/config/routing/PLAY/1-8", 13)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B33-40
mixer.send("/config/routing/PLAY/1-8", 14)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# B41-48
mixer.send("/config/routing/PLAY/1-8", 15)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# CARD 1-8
mixer.send("/config/routing/PLAY/1-8", 16)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# CARD 9-16
mixer.send("/config/routing/PLAY/1-8", 17)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# CARD 17-24
mixer.send("/config/routing/PLAY/1-8", 18)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# CARD 25-32
mixer.send("/config/routing/PLAY/1-8", 19)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# UIN 1-8
mixer.send("/config/routing/PLAY/1-8", 20)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# UIN 9-16
mixer.send("/config/routing/PLAY/1-8", 21)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# UIN 17-24
mixer.send("/config/routing/PLAY/1-8", 22)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)

# UIN 25-32
mixer.send("/config/routing/PLAY/1-8", 23)
print(mixer.query("/config/routing/PLAY/1-8"))
time.sleep(1)



# PLAY AUX Routing Configurations
# AUX1-4
mixer.send("/config/routing/PLAY/AUX", 0)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# AN1-2
mixer.send("/config/routing/PLAY/AUX", 1)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# AN1-4
mixer.send("/config/routing/PLAY/AUX", 2)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# AN1-6
mixer.send("/config/routing/PLAY/AUX", 3)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# A1-2
mixer.send("/config/routing/PLAY/AUX", 4)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# A1-4
mixer.send("/config/routing/PLAY/AUX", 5)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# A1-6
mixer.send("/config/routing/PLAY/AUX", 6)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# B1-2
mixer.send("/config/routing/PLAY/AUX", 7)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# B1-4
mixer.send("/config/routing/PLAY/AUX", 8)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# B1-6
mixer.send("/config/routing/PLAY/AUX", 9)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# CARD1-2
mixer.send("/config/routing/PLAY/AUX", 10)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# CARD1-4
mixer.send("/config/routing/PLAY/AUX", 11)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# CARD1-6
mixer.send("/config/routing/PLAY/AUX", 12)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)


# UIN1-2
mixer.send("/config/routing/PLAY/AUX", 13)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# UIN1-4
mixer.send("/config/routing/PLAY/AUX", 14)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# UIN1-6
mixer.send("/config/routing/PLAY/AUX", 15)
print(mixer.query("/config/routing/PLAY/AUX"))
time.sleep(1)

# User Color Controls 
# User Color Control A OFF
mixer.send("/config/userctrl/A/color", 0)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A RED
mixer.send("/config/userctrl/A/color", 1)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A GREEN
mixer.send("/config/userctrl/A/color", 2)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A YELLOW
mixer.send("/config/userctrl/A/color", 3)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A BLUE
mixer.send("/config/userctrl/A/color", 4)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A MAGENTA 
mixer.send("/config/userctrl/A/color", 5)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A CYAN
mixer.send("/config/userctrl/A/color", 6)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A WHITE
mixer.send("/config/userctrl/A/color", 7)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A OFFi
mixer.send("/config/userctrl/A/color", 8)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A REDi
mixer.send("/config/userctrl/A/color", 9)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A GREENi
mixer.send("/config/userctrl/A/color", 10)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A YELLOWi
mixer.send("/config/userctrl/A/color", 11)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A BLUEi
mixer.send("/config/userctrl/A/color", 12)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A MAGENTAi 
mixer.send("/config/userctrl/A/color", 13)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A CYANi
mixer.send("/config/userctrl/A/color", 14)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Control A WHITEi
mixer.send("/config/userctrl/A/color", 15)
print(mixer.query("/config/userctrl/A/color"))
time.sleep(1)

# User Color Controls B 
# User Color Control B OFF
mixer.send("/config/userctrl/B/color", 0)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B RED
mixer.send("/config/userctrl/B/color", 1)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B GREEN
mixer.send("/config/userctrl/B/color", 2)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B YELLOW
mixer.send("/config/userctrl/B/color", 3)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B BLUE
mixer.send("/config/userctrl/B/color", 4)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B MAGENTA 
mixer.send("/config/userctrl/B/color", 5)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B CYAN
mixer.send("/config/userctrl/B/color", 6)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B WHITE
mixer.send("/config/userctrl/B/color", 7)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B OFFi
mixer.send("/config/userctrl/B/color", 8)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B REDi
mixer.send("/config/userctrl/B/color", 9)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B GREENi
mixer.send("/config/userctrl/B/color", 10)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B YELLOWi
mixer.send("/config/userctrl/B/color", 11)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B BLUEi
mixer.send("/config/userctrl/B/color", 12)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B MAGENTAi 
mixer.send("/config/userctrl/B/color", 13)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B CYANi
mixer.send("/config/userctrl/B/color", 14)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)

# User Color Control B WHITEi
mixer.send("/config/userctrl/B/color", 15)
print(mixer.query("/config/userctrl/B/color"))
time.sleep(1)



# User Color Controls C 
# User Color Control C OFF
mixer.send("/config/userctrl/C/color", 0)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C RED
mixer.send("/config/userctrl/C/color", 1)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C GREEN
mixer.send("/config/userctrl/C/color", 2)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C YELLOW
mixer.send("/config/userctrl/C/color", 3)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C BLUE
mixer.send("/config/userctrl/C/color", 4)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C MAGENTA 
mixer.send("/config/userctrl/C/color", 5)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C CYAN
mixer.send("/config/userctrl/C/color", 6)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C WHITE
mixer.send("/config/userctrl/C/color", 7)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C OFFi
mixer.send("/config/userctrl/C/color", 8)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C REDi
mixer.send("/config/userctrl/C/color", 9)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C GREENi
mixer.send("/config/userctrl/C/color", 10)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C YELLOWi
mixer.send("/config/userctrl/C/color", 11)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C BLUEi
mixer.send("/config/userctrl/C/color", 12)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C MAGENTAi 
mixer.send("/config/userctrl/C/color", 13)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C CYANi
mixer.send("/config/userctrl/C/color", 14)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User Color Control C WHITEi
mixer.send("/config/userctrl/C/color", 15)
print(mixer.query("/config/userctrl/C/color"))
time.sleep(1)

# User A Encoder Controls 1-4
# User A Fader Encoder Controls Not Assigned
mixer.send("/config/userctrl/A/enc/1", _)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/A/enc/1", F00)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/A/enc/1", F32)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/A/enc/1", F40)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/A/enc/1", F48)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls Main LR
mixer.send("/config/userctrl/A/enc/1", F70)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls Main M/C
mixer.send("/config/userctrl/A/enc/1", F71)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Fader Encoder Controls DCA 1-8
mixer.send("/config/userctrl/A/enc/1", F72)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/A/enc/1", P00)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/A/enc/1", P32)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/A/enc/1", P40)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/A/enc/1", P48)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls Main LR
mixer.send("/config/userctrl/A/enc/1", P70)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls Main M/C
mixer.send("/config/userctrl/A/enc/1", P71)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Pan Encoder Controls DCA 1-8
mixer.send("/config/userctrl/A/enc/1", B72)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls 00-31 Chl 01-32 MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S0000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls 32-39 AUX 01-08 MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S320000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls 40-47 FX rtn 1L to FX rtn 4R MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S4000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls 48-63 Matrix 1-6 MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S4800)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls Main LR MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S7000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls Main M/C MixBus 01-16 
mixer.send("/config/userctrl/A/enc/1", S7100)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S7200)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/A/enc/1", S7200)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Midi Control Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/A/enc/1", MC00000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Midi Note Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/A/enc/1", MN00000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Midi Program Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/A/enc/1", MP00000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Remote 1-8  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", 000)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Remote Jog  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", 008)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Fader  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", "D@")
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Gate Threshold  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DA)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Gate Range Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DB)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Gate Attack Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DC)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Gate Hold Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DD)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Gate Release Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DE)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Threshold Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DF)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Ratio Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DG)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Knee Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DH)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic MGain  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DI)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Attack Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DJ)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Hold Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DK)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl Dynamic Release Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", DL)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl X-Live! Locator (Marker Position)  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", U0)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl X-Live! Marker List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", U1)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)

# User A Selected Chl X-Live! Session List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/A/enc/1", U2)
print(mixer.query("/config/userctrl/A/enc/1"))
time.sleep(1)



# User B Encoder Controls 1-4
# User B Fader Encoder Controls Not Assigned
mixer.send("/config/userctrl/B/enc/1", _)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/B/enc/1", F00)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/B/enc/1", F32)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/B/enc/1", F40)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/B/enc/1", F48)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls Main LR
mixer.send("/config/userctrl/B/enc/1", F70)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls Main M/C
mixer.send("/config/userctrl/B/enc/1", F71)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Fader Encoder Controls DCA 1-8
mixer.send("/config/userctrl/B/enc/1", F72)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/B/enc/1", P00)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/B/enc/1", P32)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/B/enc/1", P40)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/B/enc/1", P48)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls Main LR
mixer.send("/config/userctrl/B/enc/1", P70)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls Main M/C
mixer.send("/config/userctrl/B/enc/1", P71)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Pan Encoder Controls DCA 1-8
mixer.send("/config/userctrl/B/enc/1", B72)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls 00-31 Chl 01-32 MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S0000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls 32-39 AUX 01-08 MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S320000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls 40-47 FX rtn 1L to FX rtn 4R MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S4000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls 48-63 Matrix 1-6 MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S4800)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls Main LR MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S7000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls Main M/C MixBus 01-16 
mixer.send("/config/userctrl/B/enc/1", S7100)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S7200)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/B/enc/1", S7200)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Midi Control Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/B/enc/1", MC00000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Midi Note Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/B/enc/1", MN00000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Midi Program Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/B/enc/1", MP00000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Remote 1-8  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", 000)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Remote Jog  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", 008)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Fader  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", "D@")
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Gate Threshold  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DA)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Gate Range Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DB)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Gate Attack Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DC)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Gate Hold Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DD)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Gate Release Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DE)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Threshold Encoder Controls 
mixer.send("/config/userctrl/BA/enc/1", DF)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Ratio Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DG)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Knee Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DH)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic MGain  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DI)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Attack Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DJ)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Hold Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DK)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl Dynamic Release Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", DL)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl X-Live! Locator (Marker Position)  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", U0)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl X-Live! Marker List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", U1)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)

# User B Selected Chl X-Live! Session List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/B/enc/1", U2)
print(mixer.query("/config/userctrl/B/enc/1"))
time.sleep(1)



# User C Encoder Controls 1-4
# User C Fader Encoder Controls Not Assigned
mixer.send("/config/userctrl/C/enc/1", _)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/C/enc/1", F00)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/C/enc/1", F32)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/C/enc/1", F40)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/C/enc/1", F48)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls Main LR
mixer.send("/config/userctrl/C/enc/1", F70)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls Main M/C
mixer.send("/config/userctrl/C/enc/1", F71)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Fader Encoder Controls DCA 1-8
mixer.send("/config/userctrl/C/enc/1", F72)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls 00-31 Chl 01-32
mixer.send("/config/userctrl/C/enc/1", P00)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls 32-39 AUX 01-08
mixer.send("/config/userctrl/C/enc/1", P32)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
mixer.send("/config/userctrl/C/enc/1", P40)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls 48-63 Matrix 1-6
mixer.send("/config/userctrl/C/enc/1", P48)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls Main LR
mixer.send("/config/userctrl/C/enc/1", P70)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls Main M/C
mixer.send("/config/userctrl/C/enc/1", P71)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Pan Encoder Controls DCA 1-8
mixer.send("/config/userctrl/C/enc/1", B72)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls 00-31 Chl 01-32 MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S0000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls 32-39 AUX 01-08 MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S320000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls 40-47 FX rtn 1L to FX rtn 4R MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S4000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls 48-63 Matrix 1-6 MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S4800)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls Main LR MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S7000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls Main M/C MixBus 01-16 
mixer.send("/config/userctrl/C/enc/1", S7100)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S7200)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Send Encoder Controls DCA 1-8 MixBus 01-16
mixer.send("/config/userctrl/C/enc/1", S7200)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Midi Control Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/C/enc/1", MC00000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Midi Note Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/C/enc/1", MN00000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Midi Program Change Encoder Controls Midi Chl 1-16 MidiValue 000-127
mixer.send("/config/userctrl/C/enc/1", MP00000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Remote 1-8  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", 000)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Remote Jog  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", 008)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Fader  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", "D@")
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Gate Threshold  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DA)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Gate Range Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DB)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Gate Attack Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DC)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Gate Hold Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DD)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Gate Release Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DE)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Threshold Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DF)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Ratio Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DG)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Knee Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DH)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic MGain  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DI)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Attack Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DJ)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Hold Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DK)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl Dynamic Release Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", DL)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl X-Live! Locator (Marker Position)  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", U0)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl X-Live! Marker List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", U1)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)

# User C Selected Chl X-Live! Session List (Nav)  Encoder Controls 
mixer.send("/config/userctrl/C/enc/1", U2)
print(mixer.query("/config/userctrl/C/enc/1"))
time.sleep(1)



# User Button Controls 5-12
# User A Jump to "Channel" Page Button Controls chl 01-32 Home
mixer.send("/config/userctrl/A/btn/5", P0000)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Config
mixer.send("/config/userctrl/A/btn/5", P0001)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Gate
mixer.send("/config/userctrl/A/btn/5", P0002)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Dynamics
mixer.send("/config/userctrl/A/btn/5", P0003)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 EQ
mixer.send("/config/userctrl/A/btn/5", P0004)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Mix
mixer.send("/config/userctrl/A/btn/5", P0005)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Main
mixer.send("/config/userctrl/A/btn/5", P0006)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls chl 01-32 Send to Faders
mixer.send("/config/userctrl/A/btn/5", P000S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Home
mixer.send("/config/userctrl/A/btn/5", P0000)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Config
mixer.send("/config/userctrl/A/btn/5", P0001)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Gate
mixer.send("/config/userctrl/A/btn/5", P3202)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Dynamics
mixer.send("/config/userctrl/A/btn/5", P3203)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 EQ
mixer.send("/config/userctrl/A/btn/5", P3204)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Mix
mixer.send("/config/userctrl/A/btn/5", P3205)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Main
mixer.send("/config/userctrl/A/btn/5", P3206)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Aux 01-08 Send to Faders
mixer.send("/config/userctrl/A/btn/5", P320S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Home
mixer.send("/config/userctrl/A/btn/5", P4000)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Config
mixer.send("/config/userctrl/A/btn/5", P4001)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Gate
mixer.send("/config/userctrl/A/btn/5", P4002)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Dynamics
mixer.send("/config/userctrl/A/btn/5", P4003)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R EQ
mixer.send("/config/userctrl/A/btn/5", P4004)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Mix
mixer.send("/config/userctrl/A/btn/5", P4005)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Main
mixer.send("/config/userctrl/A/btn/5", P4006)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls FX rtn 1L-4R Send to Faders
mixer.send("/config/userctrl/A/btn/5", P400S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Home
mixer.send("/config/userctrl/A/btn/5", P4800)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Config
mixer.send("/config/userctrl/A/btn/5", P4801)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Gate
mixer.send("/config/userctrl/A/btn/5", P4802)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Dynamics
mixer.send("/config/userctrl/A/btn/5", P4803)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 EQ
mixer.send("/config/userctrl/A/btn/5", P4804)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Mix
mixer.send("/config/userctrl/A/btn/5", P4805)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Main
mixer.send("/config/userctrl/A/btn/5", P4806)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls MixBus 01-16 Send to Faders
mixer.send("/config/userctrl/A/btn/5", P480S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Home
mixer.send("/config/userctrl/A/btn/5", P6400)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Config
mixer.send("/config/userctrl/A/btn/5", P6401)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Gate
mixer.send("/config/userctrl/A/btn/5", P6402)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Dynamics
mixer.send("/config/userctrl/A/btn/5", P6403)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 EQ
mixer.send("/config/userctrl/A/btn/5", P6404)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Mix
mixer.send("/config/userctrl/A/btn/5", P6405)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Main
mixer.send("/config/userctrl/A/btn/5", P6406)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Matrix 1-6 Send to Faders
mixer.send("/config/userctrl/A/btn/5", P640S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Home
mixer.send("/config/userctrl/A/btn/5", P7000)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Config
mixer.send("/config/userctrl/A/btn/5", P7001)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Gate
mixer.send("/config/userctrl/A/btn/5", P7002)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Dynamics
mixer.send("/config/userctrl/A/btn/5", P7003)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR EQ
mixer.send("/config/userctrl/A/btn/5", P7004)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Mix
mixer.send("/config/userctrl/A/btn/5", P7005)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Main
mixer.send("/config/userctrl/A/btn/5", P7006)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main LR Send to Faders
mixer.send("/config/userctrl/A/btn/5", P700S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Home
mixer.send("/config/userctrl/A/btn/5", P7100)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Config
mixer.send("/config/userctrl/A/btn/5", P7101)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Gate
mixer.send("/config/userctrl/A/btn/5", P7102)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Dynamics
mixer.send("/config/userctrl/A/btn/5", P7103)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C EQ
mixer.send("/config/userctrl/A/btn/5", P7104)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Mix
mixer.send("/config/userctrl/A/btn/5", P7105)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Main
mixer.send("/config/userctrl/A/btn/5", P7106)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Channel" Page Button Controls Main M/C Send to Faders
mixer.send("/config/userctrl/A/btn/5", P710S)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "Meter" Page Button Controls Channel
mixer.send("/config/userctrl/A/btn/5", P10)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Meter" Page Button Controls MixBus
mixer.send("/config/userctrl/A/btn/5", P11)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Meter" Page Button Controls Aux/FX
mixer.send("/config/userctrl/A/btn/5", P12)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Meter" Page Button Controls In/Out
mixer.send("/config/userctrl/A/btn/5", P13)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Meter" Page Button Controls RTA
mixer.send("/config/userctrl/A/btn/5", P14)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "Route" Page Button Controls Home
mixer.send("/config/userctrl/A/btn/5", P20)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls Analog Out
mixer.send("/config/userctrl/A/btn/5", P21)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls AUX Out
mixer.send("/config/userctrl/A/btn/5", P22)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls P16OUT
mixer.send("/config/userctrl/A/btn/5", P23)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls CARDOUT
mixer.send("/config/userctrl/A/btn/5", P24)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls AES AO OUT
mixer.send("/config/userctrl/A/btn/5", P25)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls AES BO OUT
mixer.send("/config/userctrl/A/btn/5", P26)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "Route" Page Button Controls XLROUT
mixer.send("/config/userctrl/A/btn/5", P27)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "FX" Page Button Controls Layer OFF Home
mixer.send("/config/userctrl/A/btn/5", P0050)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX1
mixer.send("/config/userctrl/A/btn/5", P0051)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX2
mixer.send("/config/userctrl/A/btn/5", P0052)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX3
mixer.send("/config/userctrl/A/btn/5", P0053)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX4
mixer.send("/config/userctrl/A/btn/5", P0054)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX5
mixer.send("/config/userctrl/A/btn/5", P0055)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX6
mixer.send("/config/userctrl/A/btn/5", P0056)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX7
mixer.send("/config/userctrl/A/btn/5", P0057)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer OFF FX8
mixer.send("/config/userctrl/A/btn/5", P0058)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "FX" Page Button Controls Layer 01 Home
mixer.send("/config/userctrl/A/btn/5", P0150)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX1
mixer.send("/config/userctrl/A/btn/5", P0151)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX2
mixer.send("/config/userctrl/A/btn/5", P0152)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX3
mixer.send("/config/userctrl/A/btn/5", P0153)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX4
mixer.send("/config/userctrl/A/btn/5", P0154)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX5
mixer.send("/config/userctrl/A/btn/5", P0155)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX6
mixer.send("/config/userctrl/A/btn/5", P0156)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX7
mixer.send("/config/userctrl/A/btn/5", P0157)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 01 FX8
mixer.send("/config/userctrl/A/btn/5", P0158)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "FX" Page Button Controls Layer 02 Home
mixer.send("/config/userctrl/A/btn/5", P0250)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX1
mixer.send("/config/userctrl/A/btn/5", P0251)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX2
mixer.send("/config/userctrl/A/btn/5", P0252)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX3
mixer.send("/config/userctrl/A/btn/5", P0253)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX4
mixer.send("/config/userctrl/A/btn/5", P0254)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX5
mixer.send("/config/userctrl/A/btn/5", P0255)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX6
mixer.send("/config/userctrl/A/btn/5", P0256)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX7
mixer.send("/config/userctrl/A/btn/5", P0257)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 02 FX8
mixer.send("/config/userctrl/A/btn/5", P02258)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "FX" Page Button Controls Layer 03 Home
mixer.send("/config/userctrl/A/btn/5", P0350)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX1
mixer.send("/config/userctrl/A/btn/5", P0351)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX2
mixer.send("/config/userctrl/A/btn/5", P0352)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX3
mixer.send("/config/userctrl/A/btn/5", P0353)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX4
mixer.send("/config/userctrl/A/btn/5", P0354)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX5
mixer.send("/config/userctrl/A/btn/5", P0355)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX6
mixer.send("/config/userctrl/A/btn/5", P0356)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX7
mixer.send("/config/userctrl/A/btn/5", P0357)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 03 FX8
mixer.send("/config/userctrl/A/btn/5", P0358)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


# User A Jump to "FX" Page Button Controls Layer 04 Home
mixer.send("/config/userctrl/A/btn/5", P0450)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX1
mixer.send("/config/userctrl/A/btn/5", P0451)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX2
mixer.send("/config/userctrl/A/btn/5", P0452)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX3
mixer.send("/config/userctrl/A/btn/5", P0453)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX4
mixer.send("/config/userctrl/A/btn/5", P0454)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX5
mixer.send("/config/userctrl/A/btn/5", P0455)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX6
mixer.send("/config/userctrl/A/btn/5", P0456)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX7
mixer.send("/config/userctrl/A/btn/5", P0457)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)

# User A Jump to "FX" Page Button Controls Layer 04 FX8
mixer.send("/config/userctrl/A/btn/5", P0458)
print(mixer.query("/config/userctrl/A/btn/5"))
time.sleep(1)


#