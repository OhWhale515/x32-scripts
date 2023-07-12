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