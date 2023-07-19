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
 

def toggle_gate_off_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/gate/on", 0)
   

def toggle_dynamics_on_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/dyn/on", 1)
    time.sleep(1)
    on = True
    return on

def toggle_dynamics_off_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/dyn/on", 0)
    

def channel_link_on(mixer, channel1, channel2):
    mixer.send(f"/config/chlink/{channel1}-{channel2}/on", 1)
 

def channel_link_off(mixer, channel1, channel2):
    mixer.send(f"/config/chlink/{channel1}-{channel2}/on", 0)

def aux_link_on(mixer, aux1, aux2):
    mixer.send(f"/config/auxlink/{aux1}-{aux2}/on", 1)

def aux_link_off(mixer, aux1, aux2):
    mixer.send(f"/config/auxlink/{aux1}-{aux2}/on", 0)

def fx_link_on(mixer, fx1, fx2):
    mixer.send(f"/config/fxlink/{fx1}-{fx2}/on", 1)

def fx_link_off(mixer, fx1, fx2):
    mixer.send(f"/config/fxlink/{fx1}-{fx2}/on", 0)

def group_selection_mute_on(mixer, group):
    mixer.send(f"/config/mute/{group}/on", 1)

def group_selection_mute_off(mixer, group):
    mixer.send(f"/config/mute/{group}/on", 0)


def generate_random_threshold_values(count, lower_bound=-60, upper_bound=10):
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def mtx_link_on(mixer, mtx_number):
    # mtx link On
    mixer.send(f"/config/mtxlink/{mtx_number}/on", 1)
    print(mixer.query(f"/config/mtxlink/{mtx_number}/on"))

def mtx_link_off(mixer, mtx_number):
    # mtx link Off
    mixer.send(f"/config/mtxlink/{mtx_number}/on", 0)
    print(mixer.query(f"/config/mtxlink/{mtx_number}/on"))

def link_config_hadly_on(mixer, link_number):
    # link config hadly On/ Sets Delay & HA link
    mixer.send(f"/config/linkcfg/hadly/on", 1)
    print(mixer.query(f"/config/mtxlink/{link_number}/on"))

def link_config_hadly_off(mixer, link_number):
    # link config hadly Off
    mixer.send(f"/config/linkcfg/hadly/on", 0)
    print(mixer.query(f"/config/mtxlink/{link_number}/on"))

def link_config_eq_on(mixer, link_number):
    # link config EQ On/ Sets EQ link
    mixer.send(f"/config/linkcfg/eq/on", 1)
    print(mixer.query(f"/config/linkcfg/{link_number}/on"))

def link_config_eq_off(mixer, link_number):
    # link config EQ Off/ Removes EQ link
    mixer.send(f"/config/linkcfg/eq/on", 0)
    print(mixer.query(f"/config/linkcfg/{link_number}/on"))

def link_config_dynamics_on(mixer, link_number):
    # link config dynamics On
    mixer.send(f"/config/linkcfg/dyn/on", 1)
    print(mixer.query(f"/config/linkcfg/dyn/on"))

def link_config_dynamics_off(mixer, link_number):
    # link config dynamics Off
    mixer.send(f"/config/linkcfg/dyn/on", 0)
    print(mixer.query(f"/config/linkcfg/dyn/on"))


def link_config_fdr_mute_on(mixer):
    # link config FDR Mute On
    mixer.send("/config/linkcfg/fdrmute/on", 1)
    print(mixer.query("/config/linkcfg/fdrmute/on"))

def link_config_fdr_mute_off(mixer):
    # link config FDR Mute Off
    mixer.send("/config/linkcfg/fdrmute/on", 0)
    print(mixer.query("/config/linkcfg/fdrmute/on"))

def config_mono_mode_lr_plus_m(mixer):
    # Mono Mode LR+M
    mixer.send("/config/mono/mode", 1)
    print(mixer.query("/config/mono/mode"))

def config_mono_mode_lcr(mixer):
    # Mono Mode LCR
    mixer.send("/config/mono/mode", 0)
    print(mixer.query("/config/mono/mode"))

def config_mono_link_on(mixer):
    # Mono Mode Link On
    mixer.send("/config/mono/link", 1)
    print(mixer.query("/config/mono/link"))

def config_mono_link_off(mixer):
    # Mono Mode Link Off
    mixer.send("/config/mono/link", 0)
    print(mixer.query("/config/mono/link"))

def config_solo_level(mixer, level):
    # Solo dB Level
    mixer.send("/config/solo/level", level)
    print(mixer.query("/config/solo/level"))

def generate_random_solo_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random solo levels between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]


def config_solo_source_off(mixer):
    # Solo Source Options Off
    mixer.send("/config/solo/source", 0)
    print(mixer.query("/config/solo/source"))

def config_solo_source_lr(mixer):
    # Solo Source Option LR
    mixer.send("/config/solo/source", 1)
    print(mixer.query("/config/solo/source"))

def config_solo_source_lr_c(mixer):
    # Solo Source Option LR+C
    mixer.send("/config/solo/source", 2)
    print(mixer.query("/config/solo/source"))

def config_solo_source_lrpfl(mixer):
    # Solo Source Option LRPFL
    mixer.send("/config/solo/source", 3)
    print(mixer.query("/config/solo/source"))

def config_solo_source_lrafl(mixer):
    # Solo Source Option LRAFL
    mixer.send("/config/solo/source", 4)
    print(mixer.query("/config/solo/source"))

def config_solo_source_aux56(mixer):
    # Solo Source Option AUX56
    mixer.send("/config/solo/source", 5)
    print(mixer.query("/config/solo/source"))

def config_solo_source_aux78(mixer):
    # Solo Source Option AUX78
    mixer.send("/config/solo/source", 6)
    print(mixer.query("/config/solo/source"))

def config_solo_sourcetrim(mixer, level):
    # Solo Source Trim dB Level
    mixer.send("/config/solo/sourcetrim", level)
    print(mixer.query("/config/solo/sourcetrim"))

def generate_random_sourcetrim_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random solo source trim levels between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_solo_chmode_pfl(mixer):
    # Solo Channel Mode PFL
    mixer.send("/config/solo/chmode", 0)
    print(mixer.query("/config/solo/chmode"))

def config_solo_chmode_afl(mixer):
    # Solo Channel Mode AFL
    mixer.send("/config/solo/chmode", 1)
    print(mixer.query("/config/solo/chmode"))

def config_solo_busmode_pfl(mixer):
    # Solo Bus Mode PFL
    mixer.send("/config/solo/busmode", 0)
    print(mixer.query("/config/solo/busmode"))

def config_solo_busmode_afl(mixer):
    # Solo Bus Mode AFL
    mixer.send("/config/solo/busmode", 1)
    print(mixer.query("/config/solo/busmode"))

def config_solo_dcamode_pfl(mixer):
    # Solo DCA Mode PFL
    mixer.send("/config/solo/dcamode", 0)
    print(mixer.query("/config/solo/dcamode"))

def config_solo_dcamode_afl(mixer):
    # Solo DCA Mode AFL
    mixer.send("/config/solo/dcamode", 1)
    print(mixer.query("/config/solo/dcamode"))

def config_solo_exclusive_on(mixer):
    # Solo Exclusive Mode On
    mixer.send("/config/solo/exclusive", 0)
    print(mixer.query("/config/solo/exclusive"))

def config_solo_exclusive_off(mixer):
    # Solo Exclusive Mode Off
    mixer.send("/config/solo/exclusive", 1)
    print(mixer.query("/config/solo/exclusive"))

def config_solo_followsel_on(mixer):
    # Solo Follow Select Mode On
    mixer.send("/config/solo/followsel", 0)
    print(mixer.query("/config/solo/followsel"))

def config_solo_followsel_off(mixer):
    # Solo Follow Select Mode Off
    mixer.send("/config/solo/followsel", 1)
    print(mixer.query("/config/solo/followsel"))

def config_solo_followsolo_on(mixer):
    # Solo Follow Solo Mode On
    mixer.send("/config/solo/followsolo", 0)
    print(mixer.query("/config/solo/followsolo"))

def config_solo_followsolo_off(mixer):
    # Solo Follow Solo Mode Off
    mixer.send("/config/solo/followsolo", 1)
    print(mixer.query("/config/solo/followsolo"))
    
    
    
def config_solo_dimatt(mixer, level):
    # Solo DimAtt dB Level
    mixer.send("/config/solo/dimatt", level)
    print(mixer.query("/config/solo/dimatt"))

def generate_random_dimatt_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random solo dimatt levels between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_solo_dim_mode_on(mixer):
    # Solo Dim Mode On
    mixer.send("/config/solo/dim", 0)
    print(mixer.query("/config/solo/dim"))

def config_solo_dim_mode_off(mixer):
    # Solo Dim Mode Off
    mixer.send("/config/solo/dim", 1)
    print(mixer.query("/config/solo/dim"))

def config_solo_mono_mode_on(mixer):
    # Solo Mono Mode On
    mixer.send("/config/solo/mono", 0)
    print(mixer.query("/config/solo/mono"))

def config_solo_mono_mode_off(mixer):
    # Solo Mono Mode Off
    mixer.send("/config/solo/mono", 1)
    print(mixer.query("/config/solo/mono"))

def config_solo_delay_mode_on(mixer):
    # Solo Delay Mode On
    mixer.send("/config/solo/delay", 0)
    print(mixer.query("/config/solo/delay"))

def config_solo_delay_mode_off(mixer):
    # Solo Delay Mode Off
    mixer.send("/config/solo/delay", 1)
    print(mixer.query("/config/solo/delay"))

def config_solo_delay_time(mixer, time_ms):
    # Solo Delay Time ms Level
    mixer.send("/config/solo/delaytime", time_ms)
    print(mixer.query("/config/solo/delaytime"))

def generate_random_delay_time_values(count, lower_bound=-60, upper_bound=10):
    # Generate random solo delay time levels between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_solo_master_control_mode_on(mixer):
    # Solo Master Control Mode On
    mixer.send("/config/solo/masterctrl", 0)
    print(mixer.query("/config/solo/masterctrl"))

def config_solo_master_control_mode_off(mixer):
    # Solo Master Control Mode Off
    mixer.send("/config/solo/masterctrl", 1)
    print(mixer.query("/config/solo/masterctrl"))

def config_solo_mute_mode_on(mixer):
    # Solo Mute Mode On
    mixer.send("/config/solo/mute", 0)
    print(mixer.query("/config/solo/mute"))

def config_solo_mute_mode_off(mixer):
    # Solo Mute Mode Off
    mixer.send("/config/solo/mute", 1)
    print(mixer.query("/config/solo/mute"))

def config_solo_dimpfl_mode_on(mixer):
    # Solo dimpfl Mode On
    mixer.send("/config/solo/dimpfl", 0)
    print(mixer.query("/config/solo/dimpfl"))

def config_solo_dimpfl_mode_off(mixer):
    # Solo dimpfl Mode Off
    mixer.send("/config/solo/dimpfl", 1)
    print(mixer.query("/config/solo/dimpfl"))

def config_talk_mode_on(mixer):
    # Talk Mode On
    mixer.send("/config/talk/enable", 0)
    print(mixer.query("/config/talk/enable"))

def config_talk_mode_off(mixer):
    # Talk Mode Off
    mixer.send("/config/talk/enable", 1)
    print(mixer.query("/config/talk/enable"))
    
    
    
def config_talk_source_int(mixer):
    # Talk Source INT
    mixer.send("/config/talk/source", 0)
    print(mixer.query("/config/talk/source"))

def config_talk_source_ent(mixer):
    # Talk Source ENT
    mixer.send("/config/talk/source", 1)
    print(mixer.query("/config/talk/source"))

def config_talk_level_a(mixer, level):
    # Talk dB Level A
    mixer.send("/config/A/level", level)
    print(mixer.query("/config/A/level"))

def generate_random_talk_level_values(count, lower_bound=-60, upper_bound=10):
    # Generate random talk dB level values between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_talk_level_b(mixer, level):
    # Talk dB Level B
    mixer.send("/config/B/level", level)
    print(mixer.query("/config/B/level"))

def config_talk_latch_a_on(mixer):
    # Talk Latch A On
    mixer.send("/config/talk/A/latch", 0)
    print(mixer.query("/config/talk/A/latch"))

def config_talk_latch_a_off(mixer):
    # Talk Latch A Off
    mixer.send("/config/talk/A/latch", 1)
    print(mixer.query("/config/talk/A/latch"))

def config_talk_latch_b_on(mixer):
    # Talk Latch B On
    mixer.send("/config/talk/B/latch", 0)
    print(mixer.query("/config/talk/B/latch"))

def config_talk_latch_b_off(mixer):
    # Talk Latch B Off
    mixer.send("/config/talk/B/latch", 1)
    print(mixer.query("/config/talk/B/latch"))

def config_talk_dim_a_on(mixer):
    # Talk Dim A On
    mixer.send("/config/talk/A/dim", 0)
    print(mixer.query("/config/talk/A/dim"))

def config_talk_dim_a_off(mixer):
    # Talk Dim A Off
    mixer.send("/config/talk/A/dim", 1)
    print(mixer.query("/config/talk/A/dim"))

def config_talk_dim_b_on(mixer):
    # Talk Dim B On
    mixer.send("/config/talk/B/dim", 0)
    print(mixer.query("/config/talk/B/dim"))

def config_talk_dim_b_off(mixer):
    # Talk Dim B Off
    mixer.send("/config/talk/B/dim", 1)
    print(mixer.query("/config/talk/B/dim"))

def config_talk_dest_mapping_a(mixer, value):
    # Talk Dest Mapping A
    mixer.send("/config/talk/A/destmap", value)
    print(mixer.query("/config/talk/A/destmap"))

def generate_random_talk_dest_mapping_values(count, lower_bound=0, upper_bound=10):
    # Generate random talk dest mapping values between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_talk_dest_mapping_b(mixer, value):
    # Talk Dest Mapping B
    mixer.send("/config/talk/B/destmap", value)
    print(mixer.query("/config/talk/B/destmap"))
    


def config_osc_db_level(mixer, level):
    # Osc dB Level
    mixer.send("/config/osc/level", level)
    print(mixer.query("/config/osc/level"))

def generate_random_osc_db_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random OSC dB level values between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_osc_f1_hertz_level(mixer, level):
    # Osc f1 Hertz Level
    mixer.send("/config/osc/f1", level)
    print(mixer.query("/config/osc/f1"))

def generate_random_osc_f1_hertz_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random OSC f1 Hertz level values between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_osc_f2_hertz_level(mixer, level):
    # Osc f2 Hertz Level
    mixer.send("/config/osc/f2", level)
    print(mixer.query("/config/osc/f2"))

def generate_random_osc_f2_hertz_levels(count, lower_bound=-60, upper_bound=10):
    # Generate random OSC f2 Hertz level values between specified lower and upper bounds
    return [random.uniform(lower_bound, upper_bound) for _ in range(count)]

def config_osc_fsel_configuration(mixer, value):
    # OSC fsel Configuration
    mixer.send("/config/osc/fsel", value)
    print(mixer.query("/config/osc/fsel"))

def config_osc_type_configuration(mixer, osc_type):
    # Osc Type Configuration (0: SINE, 1: PINK, 2: WHITE)
    mixer.send("/config/talk/osc/type", osc_type)
    print(mixer.query("/config/talk/osc/type"))

def config_osc_destination_configuration(mixer, dest):
    # OSC Destination Configuration (0-16: MixBus 1-16, 17: Left, 18: Right, 19: Left+Right, 20: M/C, 21: Matrix1-6)
    mixer.send("/config/osc/dest", dest)
    print(mixer.query("/config/osc/dest"))
    
    
    
def config_userrout_out(mixer, output):
    """
    Configures the User Route Output.

    Args:
        mixer: The mixer object.
        output (int): The output number to configure.

    Output Numbers:
        0: User Route OFF Outs
        1-32: Local In 1-32 int 1-32
        33-80: AES50-A 1-48 int 33-80
        81-128: AES50-B 1-48 int 81-128
        129-160: Card In 1-32 int 129-160
        161-166: Aux In 1-6 int 161-166
        167: TB Internal
        168: TB External
        169-184: Outputs 1-16 int 169-184
        185-200: P16 1-16 int 185-200
        201-206: AUX 1-6 int 201-206
        207: Monitor Left
        208: Monitor Right
    """
    mixer.send("/config/userrout/out/01", output)
    print(mixer.query("/config/userrout/out/01"))


def config_userrout_in(mixer, input_num):
    """
    Configures the User Route Input.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: User Route OFF Ins
        1-32: Local In 1-32 int 1-32
        33-80: AES50-A 1-48 int 33-80
        81-128: AES50-B 1-48 int 81-128
        129-160: Card In 1-32 int 129-160
        161-166: Aux In 1-6 int 161-166
        167: TB Internal
        168: TB External
    """
    mixer.send("/config/userrout/in/01", input_num)
    print(mixer.query("/config/userrout/in/01"))

def config_routing_routswitch(mixer, route_switch):
    """
    Configures the Route Switch.

    Args:
        mixer: The mixer object.
        route_switch (int): The route switch value (0 for Record, 1 for Playback).
    """
    mixer.send("/config/routing/routswitch", route_switch)
    print(mixer.query("/config/routing/routswitch"))


def config_routing_input_1_32(mixer, input_num):
    """
    Configures the Input Routing for 1-32 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN1-8
        1: AN9-16
        2: AN17-24
        3: AN25-32
        4: A1-8
        5: A9-16
        6: A17-24
        7: A25-32
        8: A33-40
        9: A41-48
        10: B1-8
        11: B9-16
        12: B17-24
        13: B25-32
        14: B33-40
        15: B41-48
        16: CARD 1-8
        17: CARD 9-16
        18: CARD 17-24
        19: CARD 25-32
        20: UIN 1-8
        21: UIN 9-16
        22: UIN 17-24
        23: UIN 25-32
    """
    mixer.send(f"/config/routing/IN/1-8", input_num)
    print(mixer.query(f"/config/routing/IN/1-8"))

def config_routing_aux(mixer, input_num):
    """
    Configures the AUX Routing Configurations.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AUX1-4
        1: AN1-2
        2: AN1-4
        3: AN1-6
        4: A1-2
        5: A1-4
        6: A1-6
        7: B1-2
        8: B1-4
        9: B1-6
        10: CARD1-2
        11: CARD1-4
        12: CARD1-6
        13: UIN1-2
        14: UIN1-4
        15: UIN1-6
    """
    mixer.send(f"/config/routing/IN/AUX", input_num)
    print(mixer.query(f"/config/routing/IN/AUX"))



def config_routing_aes50a_1_48(mixer, input_num):
    """
    Configures the AES50-A Routing for 1-48 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN1-8
        1: AN9-16
        2: AN17-24
        3: AN25-32
        4: A1-8
        5: A9-16
        6: A17-24
        7: A25-32
        8: A33-40
        9: A41-48
        10: B1-8
        11: B9-16
        12: B17-24
        13: B25-32
        14: B33-40
        15: B41-48
        16: CARD 1-8
        17: CARD 9-16
        18: CARD 17-24
        19: CARD 25-32
        20: OUT1-8
        21: OUT9-16
        22: P16 1-8
        23: P16 9-16
        24: AUX1-6/Mon
        25: AuxIN1-6/TB
        26: UOUT1-8
        27: UOUT9-16
        28: UOUT17-24
        29: UOUT25-32
        30: UOUT33-40
        31: UOUT41-48
        32: UIN 1-8
        33: UIN 9-16
        34: UIN 17-24
        35: UIN 25-32
    """
    mixer.send(f"/config/routing/AES50A/1-8", input_num)
    print(mixer.query(f"/config/routing/AES50A/1-8"))
