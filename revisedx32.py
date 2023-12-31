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
    
    on = True
    return on

def set_gate_threshold(mixer, channel, threshold):
    mixer.send(f"/ch/{channel:02}/gate/thr", threshold)
 

def toggle_gate_off_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/gate/on", 0)
   

def toggle_dynamics_on_channel(mixer, channel):
    mixer.send(f"/ch/{channel:02}/dyn/on", 1)
    
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



def config_routing_card_1_32(mixer, input_num):
    """
    Configures the CARD Routing for 1-32 inputs.

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
    mixer.send(f"/config/routing/CARD/1-8", input_num)
    print(mixer.query(f"/config/routing/CARD/1-8"))


def config_routing_out_1_4(mixer, input_num):
    """
    Configures the OUTPUT Routing for 1-4 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN1-4
        1: AN9-12
        2: AN17-20
        3: AN25-28
        4: A1-4
        5: A9-12
        6: A17-20
        7: A25-28
        8: A33-36
        9: A41-44
        10: B1-4
        11: B9-12
        12: B17-20
        13: B25-28
        14: B33-46
        15: B41-44
        16: CARD 1-4
        17: CARD 9-12
        18: CARD 17-20
        19: CARD 25-28
        20: OUT1-4
        21: OUT9-12
        22: P16 1-4
        23: P16 9-12
        24: AUX/CR
        25: AUX/TB
        26: UOUT1-4
        27: UOUT9-12
        28: UOUT17-20
        29: UOUT25-28
        30: UOUT33-36
        31: UOUT41-44
        32: UIN 1-4
        33: UIN 9-12
        34: UIN 17-20
        35: UIN 25-28
    """
    mixer.send(f"/config/routing/OUT/1-4", input_num)
    print(mixer.query(f"/config/routing/OUT/1-4"))


def config_routing_out_9_12(mixer, input_num):
    """
    Configures the OUTPUT Routing for 9-12 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN1-4
        1: AN9-12
        2: AN17-20
        3: AN25-28
        4: A1-4
        5: A9-12
        6: A17-20
        7: A25-28
        8: A33-36
        9: A41-44
        10: B1-4
        11: B9-12
        12: B17-20
        13: B25-28
        14: B33-46
        15: B41-44
        16: CARD 1-4
        17: CARD 9-12
        18: CARD 17-20
        19: CARD 25-28
        20: OUT1-4
        21: OUT9-12
        22: P16 1-4
        23: P16 9-12
        24: AUX/CR
        25: AUX/TB
        26: UOUT1-4
        27: UOUT9-12
        28: UOUT17-20
        29: UOUT25-28
        30: UOUT33-36
        31: UOUT41-44
        32: UIN 1-4
        33: UIN 9-12
        34: UIN 17-20
        35: UIN 25-28
    """
    mixer.send(f"/config/routing/OUT/9-12", input_num)
    print(mixer.query(f"/config/routing/OUT/9-12"))



def config_routing_out_5_8(mixer, input_num):
    """
    Configures the OUTPUT Routing for 5-8 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN5-8
        1: AN13-16
        2: AN21-24
        3: AN29-32
        4: A5-8
        5: A13-16
        6: A21-24
        7: A29-32
        8: A37-40
        9: A45-48
        10: B5-8
        11: B13-16
        12: B21-24
        13: B29-32
        14: B37-40
        15: B45-48
        16: CARD 5-8
        17: CARD 13-16
        18: CARD 21-24
        19: CARD 29-32
        20: OUT5-8
        21: OUT13-16
        22: P16 5-8
        23: P16 13-16
        24: AUX/CR
        25: AUX/TB
        26: UOUT5-8
        27: UOUT13-16
        28: UOUT21-24
        29: UOUT29-32
        30: UOUT37-40
        31: UOUT45-48
        32: UIN 5-8
        33: UIN 13-16
        34: UIN 21-24
        35: UIN 29-32
    """
    mixer.send(f"/config/routing/OUT/5-8", input_num)
    print(mixer.query(f"/config/routing/OUT/5-8"))


def config_routing_out_13_16(mixer, input_num):
    """
    Configures the OUTPUT Routing for 13-16 inputs.

    Args:
        mixer: The mixer object.
        input_num (int): The input number to configure.

    Input Numbers:
        0: AN5-8
        1: AN13-16
        2: AN21-24
        3: AN29-32
        4: A5-8
        5: A13-16
        6: A21-24
        7: A29-32
        8: A37-40
        9: A45-48
        10: B5-8
        11: B13-16
        12: B21-24
        13: B29-32
        14: B37-40
        15: B45-48
        16: CARD 5-8
        17: CARD 13-16
        18: CARD 21-24
        19: CARD 29-32
        20: OUT5-8
        21: OUT13-16
        22: P16 5-8
        23: P16 13-16
        24: AUX/CR
        25: AUX/TB
        26: UOUT5-8
        27: UOUT13-16
        28: UOUT21-24
        29: UOUT29-32
        30: UOUT37-40
        31: UOUT45-48
        32: UIN 5-8
        33: UIN 13-16
        34: UIN 21-24
        35: UIN 29-32
    """
    mixer.send(f"/config/routing/OUT/13-16", input_num)
    print(mixer.query(f"/config/routing/OUT/13-16"))



def play_routing_1_8(mixer, input_num):
    """
    Configures the PLAY Routing for 1-8 inputs.

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
    mixer.send("/config/routing/PLAY/1-8", input_num)
    print(mixer.query("/config/routing/PLAY/1-8"))


def play_aux_routing(mixer, input_num):
    """
    Configures the PLAY AUX Routing.

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
    mixer.send("/config/routing/PLAY/AUX", input_num)
    print(mixer.query("/config/routing/PLAY/AUX"))



def user_color_control(mixer, control_type, color_code):
    """
    Configures the User Color Control for A, B, or C.

    Args:
        mixer: The mixer object.
        control_type (str): 'A', 'B', or 'C' for the respective control.
        color_code (int): The color code to set the color.

    Color Codes:
        0: OFF
        1: RED
        2: GREEN
        3: YELLOW
        4: BLUE
        5: MAGENTA
        6: CYAN
        7: WHITE
        8: OFFi
        9: REDi
        10: GREENi
        11: YELLOWi
        12: BLUEi
        13: MAGENTAi
        14: CYANi
        15: WHITEi
    """
    control_path = f"/config/userctrl/{control_type}/color"
    mixer.send(control_path, color_code)
    print(mixer.query(control_path))


def user_a_encoder_control(mixer, control_type, control_code):
    """
    Configures the User A Encoder Controls 1-4.

    Args:
        mixer: The mixer object.
        control_type (str): The type of control (F: Fader, P: Pan, S: Send).
        control_code (str): The control code to configure.

    Control Codes:
        F00: Fader Encoder Controls Not Assigned
        F32: Fader Encoder Controls 32-39 AUX 01-08
        F40: Fader Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
        F48: Fader Encoder Controls 48-63 Matrix 1-6
        F70: Fader Encoder Controls Main LR
        F71: Fader Encoder Controls Main M/C
        F72: Fader Encoder Controls DCA 1-8
        P00: Pan Encoder Controls 00-31 Chl 01-32
        P32: Pan Encoder Controls 32-39 AUX 01-08
        P40: Pan Encoder Controls 40-47 FX rtn 1L to FX rtn 4R
        P48: Pan Encoder Controls 48-63 Matrix 1-6
        P70: Pan Encoder Controls Main LR
        P71: Pan Encoder Controls Main M/C
        P72: Pan Encoder Controls DCA 1-8
        S0000: Send Encoder Controls 00-31 Chl 01-32 MixBus 01-16
        S320000: Send Encoder Controls 32-39 AUX 01-08 MixBus 01-16
        S4000: Send Encoder Controls 40-47 FX rtn 1L to FX rtn 4R MixBus 01-16
        S4800: Send Encoder Controls 48-63 Matrix 1-6 MixBus 01-16
        S7000: Send Encoder Controls Main LR MixBus 01-16
        S7100: Send Encoder Controls Main M/C MixBus 01-16
        S7200: Send Encoder Controls DCA 1-8 MixBus 01-16
    """
    control_path = f"/config/userctrl/A/enc/1"
    mixer.send(control_path, control_type + control_code)
    print(mixer.query(control_path))


def user_a_midi_control_change_encoder(mixer, midi_channel, midi_value):
    """
    Configures the User A Midi Control Change Encoder Controls.

    Args:
        mixer: The mixer object.
        midi_channel (int): Midi channel (1-16).
        midi_value (int): Midi value (000-127).
    """
    control_code = f"MC{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/A/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_midi_note_encoder(mixer, midi_channel, midi_value):
    """
    Configures the User A Midi Note Encoder Controls.

    Args:
        mixer: The mixer object.
        midi_channel (int): Midi channel (1-16).
        midi_value (int): Midi value (000-127).
    """
    control_code = f"MN{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/A/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_midi_program_change_encoder(mixer, midi_channel, midi_value):
    """
    Configures the User A Midi Program Change Encoder Controls.

    Args:
        mixer: The mixer object.
        midi_channel (int): Midi channel (1-16).
        midi_value (int): Midi value (000-127).
    """
    control_code = f"MP{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/A/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_selected_chl_encoder(mixer, encoder_code):
    """
    Configures the User A Selected Chl Encoder Controls.

    Args:
        mixer: The mixer object.
        encoder_code (str): The encoder control code to configure.
    """
    control_path = "/config/userctrl/A/enc/1"
    mixer.send(control_path, encoder_code)
    print(mixer.query(control_path))


def user_b_fader_encoder_not_assigned(mixer):
    control_code = "_"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_fader_encoder_channels(mixer, channel_number):
    control_code = f"F{channel_number:02d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_fader_encoder_aux(mixer, aux_number):
    control_code = f"F{aux_number:02d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_send_encoder_channels(mixer, channel_number, mix_bus_number):
    control_code = f"S{channel_number:02d}{mix_bus_number:04d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_midi_control_change_encoder(mixer, midi_channel, midi_value):
    control_code = f"MC{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_midi_note_encoder(mixer, midi_channel, midi_value):
    control_code = f"MN{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_midi_program_change_encoder(mixer, midi_channel, midi_value):
    control_code = f"MP{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_b_selected_chl_encoder(mixer, encoder_code):
    control_path = "/config/userctrl/B/enc/1"
    mixer.send(control_path, encoder_code)
    print(mixer.query(control_path))


def user_c_fader_encoder_not_assigned(mixer):
    control_code = "_"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_fader_encoder_channels(mixer, channel_number):
    control_code = f"F{channel_number:02d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_fader_encoder_aux(mixer, aux_number):
    control_code = f"F{aux_number:02d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_send_encoder_channels(mixer, channel_number, mix_bus_number):
    control_code = f"S{channel_number:02d}{mix_bus_number:04d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))



def user_c_midi_control_change_encoder(mixer, midi_channel, midi_value):
    control_code = f"MC{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_midi_note_encoder(mixer, midi_channel, midi_value):
    control_code = f"MN{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_midi_program_change_encoder(mixer, midi_channel, midi_value):
    control_code = f"MP{midi_channel:02d}{midi_value:03d}"
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_c_remote_encoder(mixer, remote_code):
    control_path = "/config/userctrl/C/enc/1"
    mixer.send(control_path, remote_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_home(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_config(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_gate(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_dynamics(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_eq(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_mix(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_main(mixer, channel_number):
    control_code = f"P{channel_number:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_channel_page_send_to_faders(mixer, channel_number):
    control_code = f"P{channel_number:04d}S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_home(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_config(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_gate(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_dynamics(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_eq(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_mix(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_main(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_aux_page_send_to_faders(mixer, aux_number):
    control_code = f"P{aux_number + 3200:04d}S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_home(mixer):
    control_code = "P4000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_config(mixer):
    control_code = "P4001"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_gate(mixer):
    control_code = "P4002"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_dynamics(mixer):
    control_code = "P4003"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_eq(mixer):
    control_code = "P4004"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_mix(mixer):
    control_code = "P4005"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_main(mixer):
    control_code = "P4006"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_return_send_to_faders(mixer):
    control_code = "P400S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_home(mixer):
    control_code = "P4800"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_config(mixer):
    control_code = "P4801"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_gate(mixer):
    control_code = "P4802"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_dynamics(mixer):
    control_code = "P4803"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_eq(mixer):
    control_code = "P4804"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_mix(mixer):
    control_code = "P4805"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_main(mixer):
    control_code = "P4806"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mixbus_send_to_faders(mixer):
    control_code = "P480S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_home(mixer):
    control_code = "P6400"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_config(mixer):
    control_code = "P6401"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_gate(mixer):
    control_code = "P6402"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_dynamics(mixer):
    control_code = "P6403"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_eq(mixer):
    control_code = "P6404"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_mix(mixer):
    control_code = "P6405"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_main(mixer):
    control_code = "P6406"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_matrix_send_to_faders(mixer):
    control_code = "P640S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_home(mixer):
    control_code = "P7000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_config(mixer):
    control_code = "P7001"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_gate(mixer):
    control_code = "P7002"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_dynamics(mixer):
    control_code = "P7003"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_eq(mixer):
    control_code = "P7004"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_mix(mixer):
    control_code = "P7005"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_main(mixer):
    control_code = "P7006"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_lr_send_to_faders(mixer):
    control_code = "P700S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_home(mixer):
    control_code = "P7100"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_config(mixer):
    control_code = "P7101"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_gate(mixer):
    control_code = "P7102"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_dynamics(mixer):
    control_code = "P7103"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_eq(mixer):
    control_code = "P7104"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_mix(mixer):
    control_code = "P7105"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_main(mixer):
    control_code = "P7106"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_main_mc_send_to_faders(mixer):
    control_code = "P710S"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_meter_channel(mixer):
    control_code = "P10"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_meter_mixbus(mixer):
    control_code = "P11"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_meter_aux_fx(mixer):
    control_code = "P12"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_meter_in_out(mixer):
    control_code = "P13"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_meter_rta(mixer):
    control_code = "P14"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_home(mixer):
    control_code = "P20"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_analog_out(mixer):
    control_code = "P21"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_aux_out(mixer):
    control_code = "P22"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_p16_out(mixer):
    control_code = "P23"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_card_out(mixer):
    control_code = "P24"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_aes_ao_out(mixer):
    control_code = "P25"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_aes_bo_out(mixer):
    control_code = "P26"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_route_xlr_out(mixer):
    control_code = "P27"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_global(mixer):
    control_code = "P30"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_conf(mixer):
    control_code = "P31"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_remote(mixer):
    control_code = "P32"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_network(mixer):
    control_code = "P33"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_names(mixer):
    control_code = "P34"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_preamps(mixer):
    control_code = "P35"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_setup_card(mixer):
    control_code = "P36"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_library_channel(mixer):
    control_code = "P40"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_library_effect(mixer):
    control_code = "P41"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_library_route(mixer):
    control_code = "P42"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_home(mixer):
    control_code = "P0050"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx1(mixer):
    control_code = "P0051"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx2(mixer):
    control_code = "P0052"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx3(mixer):
    control_code = "P0053"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx4(mixer):
    control_code = "P0054"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx5(mixer):
    control_code = "P0055"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx6(mixer):
    control_code = "P0056"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx7(mixer):
    control_code = "P0057"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_off_fx8(mixer):
    control_code = "P0058"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))

def user_a_jump_to_fx_layer_01_home(mixer):
    control_code = "P0150"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx1(mixer):
    control_code = "P0151"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx2(mixer):
    control_code = "P0152"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx3(mixer):
    control_code = "P0153"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx4(mixer):
    control_code = "P0154"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx5(mixer):
    control_code = "P0155"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx6(mixer):
    control_code = "P0156"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx7(mixer):
    control_code = "P0157"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_01_fx8(mixer):
    control_code = "P0158"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_fx_layer_02_home(mixer):
    control_code = "P0250"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))
# Continue with the rest of the functions for Layers 02 to 04.

def user_a_jump_to_monitor_page(mixer):
    control_code = "P60"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_monitor_talk_a(mixer):
    control_code = "P61"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_monitor_talk_b(mixer):
    control_code = "P62"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_monitor_osc(mixer):
    control_code = "P63"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_home(mixer):
    control_code = "P70"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_config(mixer):
    control_code = "P71"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_home(mixer):
    control_code = "P80"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_scenes(mixer):
    control_code = "P81"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_bit(mixer):
    control_code = "P82"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_parsafe(mixer):
    control_code = "P83"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_chnsafe(mixer):
    control_code = "P84"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_midi(mixer):
    control_code = "P85"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_assign_home(mixer):
    control_code = "P90"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_assign_set_a(mixer):
    control_code = "P91"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_assign_set_b(mixer):
    control_code = "P92"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_assign_set_c(mixer):
    control_code = "P93"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_channel_01_32(mixer):
    control_code = "O00"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_aux_01_08(mixer):
    control_code = "O32"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_fx_rtn_1l_to_fx_rtn_4r(mixer):
    control_code = "O40"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_mixbus_01_16(mixer):
    control_code = "O48"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_matrix_1_6(mixer):
    control_code = "O64"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_main_lr(mixer):
    control_code = "O70"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_main_mc(mixer):
    control_code = "O71"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_dca_1_8(mixer):
    control_code = "O72"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_mutes_mute_group_1_6(mixer):
    control_code = "O80"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_inserts_channel_01_32(mixer):
    control_code = "I00"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


# Rest of the "Inserts" Page Button Controls functions...


def user_a_jump_to_effect_button_effect_1_8_params_00_63(mixer):
    control_code = "X000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_midi_toggle_control_change_channel_number_value(mixer):
    control_code = "Mc01000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_midi_toggle_note_channel_number_value(mixer):
    control_code = "Mn01000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_f1_f8(mixer):
    control_code = "R000"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))

def user_a_jump_to_remote_mrk_rtz(mixer):
    control_code = "R023"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_cycle(mixer):
    control_code = "R024"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_scrub(mixer):
    control_code = "R025"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_ndg_shut(mixer):
    control_code = "R026"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_drop_in(mixer):
    control_code = "R027"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_rep_out(mixer):
    control_code = "R028"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_cli_off(mixer):
    control_code = "R029"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_read(mixer):
    control_code = "R030"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_write(mixer):
    control_code = "R031"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_touch(mixer):
    control_code = "R032"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_trim(mixer):
    control_code = "R033"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_remote_latch(mixer):
    control_code = "R034"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_cue_recall_prev(mixer):
    control_code = "S900"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_cue_recall_next(mixer):
    control_code = "S901"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_cue_recall_undo(mixer):
    control_code = "S902"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_cue_recall_go(mixer):
    control_code = "S903"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_scene_recall_cue_number(mixer):
    control_code = "S400"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_snippet_number(mixer):
    control_code = "S200"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_stop(mixer):
    control_code = "T0"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_play(mixer):
    control_code = "T1"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_record(mixer):
    control_code = "T2"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_pause(mixer):
    control_code = "T3"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_play_stop(mixer):
    control_code = "T4"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_play_pause(mixer):
    control_code = "T5"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_rec_stop(mixer):
    control_code = "T6"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_rec_pause(mixer):
    control_code = "T7"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_prev_track(mixer):
    control_code = "T8"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_usb_recorder_next_track(mixer):
    control_code = "T9"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_stop(mixer):
    control_code = "U00"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_play(mixer):
    control_code = "U01"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_record(mixer):
    control_code = "U02"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_pause(mixer):
    control_code = "U03"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_play_stop(mixer):
    control_code = "U04"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_play_pause(mixer):
    control_code = "U05"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_add_marker(mixer):
    control_code = "U06"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_prev_marker(mixer):
    control_code = "U07"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_next_marker(mixer):
    control_code = "U08"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_play_marker(mixer):
    control_code = "U09"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_select_marker(mixer):
    control_code = "U10"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_select_session(mixer):
    control_code = "U11"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_sd_recorder_usb_playback(mixer):
    control_code = "U12"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))

def user_a_jump_to_sd_recorder_chn_routing(mixer):
    control_code = "U13"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_automix_enable_x_axis(mixer):
    control_code = "A0"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def user_a_jump_to_automix_enable_y_axis(mixer):
    control_code = "A1"
    control_path = "/config/userctrl/A/btn/5"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def set_tape_gain_left(mixer, gain_value):
    control_path = "/config/tape/gainL"
    mixer.send(control_path, gain_value)
    print(mixer.query(control_path))


def set_tape_gain_right(mixer, gain_value):
    control_path = "/config/tape/gainR"
    mixer.send(control_path, gain_value)
    print(mixer.query(control_path))


def set_tape_autoplay_off(mixer):
    control_code = "OFF"
    control_path = "/config/tape/autoplay"
    mixer.send(control_path, control_code)
    print(mixer.query(control_path))


def set_mix_enable_off(mixer, mix_number):
    control_path = f"/config/amixenable/{mix_number}"
    mixer.send(control_path, 0)
    print(mixer.query(control_path))


def set_mix_enable_on(mixer, mix_number):
    control_path = f"/config/amixenable/{mix_number}"
    mixer.send(control_path, 1)
    print(mixer.query(control_path))


def set_dp48_scope_group_name(mixer, scope_group_name):
    control_path = "/config/dp48/scope"
    mixer.send(control_path, 0)
    print(mixer.query(control_path))


def set_dp48_scope_group_assign(mixer, scope_group_assign):
    control_path = "/config/dp48/scope"
    mixer.send(control_path, 1)
    print(mixer.query(control_path))


def set_dp48_scope_chan_level(mixer, scope_chan_level):
    control_path = "/config/dp48/scope"
    mixer.send(control_path, 2)
    print(mixer.query(control_path))


def set_dp48_scope_chan_pan(mixer, scope_chan_pan):
    control_path = "/config/dp48/scope"
    mixer.send(control_path, 3)
    print(mixer.query(control_path))


def set_dp48_broadcast_no_op(mixer, broadcast_no_op):
    control_path = "/config/dp48/broadcast"
    mixer.send(control_path, 0)
    print(mixer.query(control_path))


def set_dp48_broadcast_scope_tbv(mixer, broadcast_scope_tbv):
    control_path = "/config/dp48/broadcast"
    mixer.send(control_path, 1)
    print(mixer.query(control_path))


def set_dp48_assign_group_off(mixer, channel_number):
    control_path = f"/config/dp48/assign/{channel_number:02}"
    mixer.send(control_path, 0)
    print(mixer.query(control_path))


def set_dp48_assign_group(mixer, channel_number, group_number):
    control_path = f"/config/dp48/assign/{channel_number:02}"
    mixer.send(control_path, group_number)
    print(mixer.query(control_path))


def set_dp48_group_name(mixer, group_number, group_name):
    control_path = f"/config/dp48/grpname/{group_number:02}"
    mixer.send(control_path, group_name)
    print(mixer.query(control_path))


def set_channel_name(mixer, channel_id, name):
    control_path = f"/ch/{channel_id:02}/config/name"
    mixer.send(control_path, name)
    print(mixer.query(control_path))


def set_channel_icon(mixer, channel_id, icon_id):
    control_path = f"/ch/{channel_id:02}/config/icon"
    mixer.send(control_path, icon_id)
    print(mixer.query(control_path))


def set_channel_color(mixer, channel_id, color_id):
    control_path = f"/ch/{channel_id:02}/config/color"
    mixer.send(control_path, color_id)
    print(mixer.query(control_path))


def set_channel_source(mixer, channel_id, source_id):
    control_path = f"/ch/{channel_id:02}/config/source"
    mixer.send(control_path, source_id)
    print(mixer.query(control_path))


def set_delay_on(mixer, channel_id, delay_on):
    control_path = f"/ch/{channel_id:02}/delay/on"
    mixer.send(control_path, delay_on)
    print(mixer.query(control_path))
    

def set_delay_time(mixer, channel_id, delay_time):
    control_path = f"/ch/{channel_id:02}/delay/time"
    mixer.send(control_path, delay_time)
    print(mixer.query(control_path))
    

def set_preamp_trim(mixer, channel_id, trim_value):
    control_path = f"/ch/{channel_id:02}/preamp/trim"
    mixer.send(control_path, trim_value)
    print(mixer.query(control_path))
    

def set_preamp_invert(mixer, channel_id, invert_on):
    control_path = f"/ch/{channel_id:02}/preamp/invert"
    mixer.send(control_path, invert_on)
    print(mixer.query(control_path))
    

def set_preamp_phantom_power(mixer, channel_id, phantom_power_on):
    control_path = f"/ch/{channel_id:02}/preamp/hpon"
    mixer.send(control_path, phantom_power_on)
    print(mixer.query(control_path))
    

def set_preamp_hpf(mixer, channel_id, hpf_value):
    control_path = f"/ch/{channel_id:02}/preamp/hpf"
    mixer.send(control_path, hpf_value)
    print(mixer.query(control_path))
    

def set_gate_on(mixer, channel_id, gate_on):
    control_path = f"/ch/{channel_id:02}/gate/on"
    mixer.send(control_path, gate_on)
    print(mixer.query(control_path))
    

def set_gate_mode(mixer, channel_id, gate_mode):
    control_path = f"/ch/{channel_id:02}/gate/mode"
    mixer.send(control_path, gate_mode)
    print(mixer.query(control_path))
    

def set_gate_threshold(mixer, channel_id, threshold):
    control_path = f"/ch/{channel_id:02}/gate/thr"
    mixer.send(control_path, threshold)
    print(mixer.query(control_path))
    

def set_gate_range(mixer, channel_id, gate_range):
    control_path = f"/ch/{channel_id:02}/gate/range"
    mixer.send(control_path, gate_range)
    print(mixer.query(control_path))
    

def set_gate_attack(mixer, channel_id, gate_attack):
    control_path = f"/ch/{channel_id:02}/gate/attack"
    mixer.send(control_path, gate_attack)
    print(mixer.query(control_path))
    

def set_gate_hold(mixer, channel_id, gate_hold):
    control_path = f"/ch/{channel_id:02}/gate/hold"
    mixer.send(control_path, gate_hold)
    print(mixer.query(control_path))
    

def set_gate_release(mixer, channel_id, gate_release):
    control_path = f"/ch/{channel_id:02}/gate/release"
    mixer.send(control_path, gate_release)
    print(mixer.query(control_path))
    


def set_gate_source(mixer, channel_id, gate_source):
    control_path = f"/ch/{channel_id:02}/gate/keysrc"
    mixer.send(control_path, gate_source)
    print(mixer.query(control_path))
    

def set_gate_filter_on(mixer, channel_id, filter_on):
    control_path = f"/ch/{channel_id:02}/gate/filter/on"
    mixer.send(control_path, filter_on)
    print(mixer.query(control_path))
    

def set_gate_filter_type(mixer, channel_id, filter_type):
    control_path = f"/ch/{channel_id:02}/gate/filter/type"
    mixer.send(control_path, filter_type)
    print(mixer.query(control_path))
    

def set_gate_filter_hertz(mixer, channel_id, filter_hertz):
    control_path = f"/ch/{channel_id:02}/gate/filter/f"
    mixer.send(control_path, filter_hertz)
    print(mixer.query(control_path))
    


def set_dynamic_mode_on(mixer, channel_id, dynamic_on):
    control_path = f"/ch/{channel_id:02}/dyn/on"
    mixer.send(control_path, dynamic_on)
    print(mixer.query(control_path))
    

def set_dynamic_mode(mixer, channel_id, dynamic_mode):
    control_path = f"/ch/{channel_id:02}/dyn/mode"
    mixer.send(control_path, dynamic_mode)
    print(mixer.query(control_path))
    

def set_dynamic_detection(mixer, channel_id, dynamic_detection):
    control_path = f"/ch/{channel_id:02}/dyn/det"
    mixer.send(control_path, dynamic_detection)
    print(mixer.query(control_path))
    

def set_dynamic_envelope(mixer, channel_id, dynamic_envelope):
    control_path = f"/ch/{channel_id:02}/dyn/env"
    mixer.send(control_path, dynamic_envelope)
    print(mixer.query(control_path))
    

def set_dynamic_threshold(mixer, channel_id, threshold):
    control_path = f"/ch/{channel_id:02}/dyn/thr"
    mixer.send(control_path, threshold)
    print(mixer.query(control_path))
    

def set_dynamic_ratio(mixer, channel_id, ratio):
    control_path = f"/ch/{channel_id:02}/dyn/ratio"
    mixer.send(control_path, ratio)
    print(mixer.query(control_path))
    


def set_dynamic_knee(mixer, channel_id, knee):
    control_path = f"/ch/{channel_id:02}/dyn/knee"
    mixer.send(control_path, knee)
    print(mixer.query(control_path))
    

def set_dynamic_mgain(mixer, channel_id, mgain):
    control_path = f"/ch/{channel_id:02}/dyn/mgain"
    mixer.send(control_path, mgain)
    print(mixer.query(control_path))
    

def set_dynamic_attack(mixer, channel_id, attack):
    control_path = f"/ch/{channel_id:02}/dyn/attack"
    mixer.send(control_path, attack)
    print(mixer.query(control_path))
    

def set_dynamic_hold(mixer, channel_id, hold):
    control_path = f"/ch/{channel_id:02}/dyn/hold"
    mixer.send(control_path, hold)
    print(mixer.query(control_path))
    

def set_dynamic_release(mixer, channel_id, release):
    control_path = f"/ch/{channel_id:02}/dyn/release"
    mixer.send(control_path, release)
    print(mixer.query(control_path))
    

def set_dynamic_position(mixer, channel_id, position):
    control_path = f"/ch/{channel_id:02}/dyn/pos"
    mixer.send(control_path, position)
    print(mixer.query(control_path))
    

def set_dynamic_key_source(mixer, channel_id, key_source):
    control_path = f"/ch/{channel_id:02}/dyn/keysrc"
    mixer.send(control_path, key_source)
    print(mixer.query(control_path))
    

def set_dynamic_mix(mixer, channel_id, mix_percent):
    control_path = f"/ch/{channel_id:02}/dyn/mix"
    mixer.send(control_path, mix_percent)
    print(mixer.query(control_path))
    

def set_dynamic_auto(mixer, channel_id, dynamic_auto):
    control_path = f"/ch/{channel_id:02}/dyn/auto"
    mixer.send(control_path, dynamic_auto)
    print(mixer.query(control_path))
    

def set_dynamic_filter_on(mixer, channel_id, dynamic_filter_on):
    control_path = f"/ch/{channel_id:02}/dyn/filter/on"
    mixer.send(control_path, dynamic_filter_on)
    print(mixer.query(control_path))
    


def set_channel_dynamic_type(mixer, channel_id, dynamic_type):
    control_path = f"/ch/{channel_id:02}/dyn/filter/type"
    mixer.send(control_path, dynamic_type)
    print(mixer.query(control_path))
    

def set_dynamic_filter_hertz(mixer, channel_id, dynamic_filter_hertz):
    control_path = f"/ch/{channel_id:02}/dyn/filter/f"
    mixer.send(control_path, dynamic_filter_hertz)
    print(mixer.query(control_path))
    

def set_channel_insert_on(mixer, channel_id, insert_on):
    control_path = f"/ch/{channel_id:02}/insert/on"
    mixer.send(control_path, insert_on)
    print(mixer.query(control_path))
    

def set_channel_insert_position(mixer, channel_id, insert_position):
    control_path = f"/ch/{channel_id:02}/insert/pos"
    mixer.send(control_path, insert_position)
    print(mixer.query(control_path))
    

def set_channel_insert_sel(mixer, channel_id, insert_sel):
    control_path = f"/ch/{channel_id:02}/insert/sel"
    mixer.send(control_path, insert_sel)
    print(mixer.query(control_path))
    


def set_channel_eq_on(mixer, channel_id, eq_on):
    control_path = f"/ch/{channel_id:02}/eq/on"
    mixer.send(control_path, eq_on)
    print(mixer.query(control_path))
    

def set_channel_eq_type(mixer, channel_id, eq_band, eq_type):
    control_path = f"/ch/{channel_id:02}/eq/{eq_band}/type"
    mixer.send(control_path, eq_type)
    print(mixer.query(control_path))
    

def set_channel_eq_hertz(mixer, channel_id, eq_band, eq_hertz):
    control_path = f"/ch/{channel_id:02}/eq/{eq_band}/f"
    mixer.send(control_path, eq_hertz)
    print(mixer.query(control_path))
    

def set_channel_eq_db(mixer, channel_id, eq_band, eq_db):
    control_path = f"/ch/{channel_id:02}/eq/{eq_band}/g"
    mixer.send(control_path, eq_db)
    print(mixer.query(control_path))
    

def set_channel_eq_q(mixer, channel_id, eq_band, eq_q):
    control_path = f"/ch/{channel_id:02}/eq/{eq_band}/q"
    mixer.send(control_path, eq_q)
    print(mixer.query(control_path))
    

def set_channel_mix_on(mixer, channel_id, mix_on):
    control_path = f"/ch/{channel_id:02}/mix/on"
    mixer.send(control_path, mix_on)
    print(mixer.query(control_path))
    

def set_channel_mix_fader(mixer, channel_id, mix_fader):
    control_path = f"/ch/{channel_id:02}/mix/fader"
    mixer.send(control_path, mix_fader)
    print(mixer.query(control_path))
    

def set_channel_mix_stereo_link(mixer, channel_id, mix_stereo_link):
    control_path = f"/ch/{channel_id:02}/mix/st"
    mixer.send(control_path, mix_stereo_link)
    print(mixer.query(control_path))
    

def set_channel_mix_pan(mixer, channel_id, mix_pan):
    control_path = f"/ch/{channel_id:02}/mix/pan"
    mixer.send(control_path, mix_pan)
    print(mixer.query(control_path))
    

def set_channel_mix_mono(mixer, channel_id, mix_mono):
    control_path = f"/ch/{channel_id:02}/mix/mono"
    mixer.send(control_path, mix_mono)
    print(mixer.query(control_path))
    

def set_channel_mix_mlevel(mixer, channel_id, mix_mlevel):
    control_path = f"/ch/{channel_id:02}/mix/mlevel"
    mixer.send(control_path, mix_mlevel)
    print(mixer.query(control_path))
    

def set_channel_mix_on(mixer, channel_id, mix_on):
    control_path = f"/ch/{channel_id:02}/mix/{mix_on}/on"
    mixer.send(control_path, 1 if mix_on else 0)
    print(mixer.query(control_path))
    

def set_channel_mix_level(mixer, channel_id, mix_level):
    control_path = f"/ch/{channel_id:02}/mix/{mix_level}/level"
    mixer.send(control_path, 10.0)
    print(mixer.query(control_path))
    
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(control_path, str(val))
        on = ~on
    

def set_channel_mix_pan(mixer, channel_id, mix_pan):
    control_path = f"/ch/{channel_id:02}/mix/{mix_pan}/pan"
    mixer.send(control_path, 10.0)
    print(mixer.query(control_path))
    
    for i in range(100):
        val = random.uniform(-60, 10)
        mixer.send(control_path, str(val))
        on = ~on
    


def set_channel_mix_type(mixer, channel_id, mix_id, mix_type):
    control_path = f"/ch/{channel_id:02}/mix/{mix_id:02}/type"
    mixer.send(control_path, mix_type)
    print(mixer.query(control_path))
    
    

def set_channel_mix_pan_follow(mixer, channel_id, mix_id, pan_follow):
    control_path = f"/ch/{channel_id:02}/mix/{mix_id:02}/panFollow"
    mixer.send(control_path, pan_follow)
    print(mixer.query(control_path))
    

def set_channel_grp_dca(mixer, channel_id, dca_value):
    control_path = f"/ch/{channel_id:02}/grp/dca"
    mixer.send(control_path, dca_value)
    print(mixer.query(control_path))
    

def set_channel_grp_mute(mixer, channel_id, mute_value):
    control_path = f"/ch/{channel_id:02}/grp/mute"
    mixer.send(control_path, mute_value)
    print(mixer.query(control_path))
    

def set_channel_automix_group(mixer, channel_id, group_type):
    control_path = f"/ch/{channel_id:02}/automix/group"
    mixer.send(control_path, group_type)
    print(mixer.query(control_path))
    

def set_channel_automix_weight(mixer, channel_id, weight_value):
    control_path = f"/ch/{channel_id:02}/automix/weight"
    mixer.send(control_path, weight_value)
    print(mixer.query(control_path))
    
    
    
def set_aux_input_name(mixer, aux_id, name):
    control_path = f"/auxin/{aux_id:02}/config/name"
    mixer.send(control_path, name)
    print(mixer.query(control_path))
    

def set_aux_input_icon(mixer, aux_id, icon):
    control_path = f"/auxin/{aux_id:02}/config/icon"
    mixer.send(control_path, icon)
    print(mixer.query(control_path))
    

def set_aux_input_color(mixer, aux_id, color):
    color_map = {
        "OFF": 0, "RD": 1, "GN": 2, "YE": 3, "BL": 4, "MG": 5, "CY": 6, "WH": 7,
        "OFFi": 8, "RDi": 9, "GNi": 10, "YEi": 11, "BLi": 12, "MGi": 13, "CYi": 14, "WHi": 15
    }
    control_path = f"/auxin/{aux_id:02}/config/color"
    mixer.send(control_path, color_map[color])
    print(mixer.query(control_path))
    

def set_aux_input_source(mixer, aux_id, source):
    control_path = f"/auxin/{aux_id:02}/config/source"
    mixer.send(control_path, source)
    print(mixer.query(control_path))
    
    
    
def set_aux_input_preamp_trim(mixer, aux_id, trim_db):
    control_path = f"/auxin/{aux_id:02}/preamp/trim"
    mixer.send(control_path, trim_db)
    print(mixer.query(control_path))
    

def set_aux_input_preamp_invert(mixer, aux_id, invert):
    invert_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/preamp/invert"
    mixer.send(control_path, invert_map[invert])
    print(mixer.query(control_path))
    

def set_aux_input_eq_on_off(mixer, aux_id, eq_on):
    eq_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/eq/on"
    mixer.send(control_path, eq_on_map[eq_on])
    print(mixer.query(control_path))
    

def set_aux_input_eq_type(mixer, aux_id, eq_band, eq_type):
    eq_type_map = {"LCut": 0, "LShv": 1, "PEQ": 2, "VEQ": 3, "HShv": 4, "HCut": 5}
    control_path = f"/auxin/{aux_id:02}/eq/{eq_band}/type"
    mixer.send(control_path, eq_type_map[eq_type])
    print(mixer.query(control_path))
    

def set_aux_input_eq_frequency(mixer, aux_id, eq_band, frequency_hz):
    control_path = f"/auxin/{aux_id:02}/eq/{eq_band}/f"
    mixer.send(control_path, frequency_hz)
    print(mixer.query(control_path))
    

def set_aux_input_eq_gain(mixer, aux_id, eq_band, gain_db):
    control_path = f"/auxin/{aux_id:02}/eq/{eq_band}/g"
    mixer.send(control_path, gain_db)
    print(mixer.query(control_path))
    

def set_aux_input_eq_q(mixer, aux_id, eq_band, q_value):
    control_path = f"/auxin/{aux_id:02}/eq/{eq_band}/q"
    mixer.send(control_path, q_value)
    print(mixer.query(control_path))
    
    
    
def set_aux_input_mix_on_off(mixer, aux_id, mix_on):
    mix_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/mix/on"
    mixer.send(control_path, mix_on_map[mix_on])
    print(mixer.query(control_path))
    

def set_aux_input_mix_fader(mixer, aux_id, fader_level):
    control_path = f"/auxin/{aux_id:02}/mix/fader"
    mixer.send(control_path, fader_level)
    print(mixer.query(control_path))
    

def set_aux_input_mix_stereo_link(mixer, aux_id, stereo_link):
    stereo_link_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/mix/st"
    mixer.send(control_path, stereo_link_map[stereo_link])
    print(mixer.query(control_path))
    

def set_aux_input_mix_pan(mixer, aux_id, pan_value):
    control_path = f"/auxin/{aux_id:02}/mix/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))
    

def set_aux_input_mix_mono(mixer, aux_id, mono):
    mono_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/mix/mono"
    mixer.send(control_path, mono_map[mono])
    print(mixer.query(control_path))
    

def set_aux_input_mix_master_level(mixer, aux_id, level):
    control_path = f"/auxin/{aux_id:02}/mix/mlevel"
    mixer.send(control_path, level)
    print(mixer.query(control_path))
    

def set_aux_input_mix_channel_on_off(mixer, aux_id, channel_num, channel_on):
    channel_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/on"
    mixer.send(control_path, channel_on_map[channel_on])
    print(mixer.query(control_path))
    

def set_aux_input_mix_channel_level(mixer, aux_id, channel_num, channel_level):
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/level"
    mixer.send(control_path, channel_level)
    print(mixer.query(control_path))
    

def set_aux_input_mix_channel_pan(mixer, aux_id, channel_num, pan_value):
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))
    

def set_aux_input_mix_channel_type(mixer, aux_id, channel_num, channel_type):
    channel_type_map = {
        "IN/LC": 0, "<-EQ": 1, "EQ->": 2, "PRE": 3, "POST": 4, "GRP": 5
    }
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/type"
    mixer.send(control_path, channel_type_map[channel_type])
    print(mixer.query(control_path))
    
    
    
def set_aux_input_mix_channel_pan(mixer, aux_id, channel_num, pan_value):
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))
    

def set_aux_input_mix_channel_type(mixer, aux_id, channel_num, channel_type):
    channel_type_map = {
        "IN/LC": 0, "<-EQ": 1, "EQ->": 2, "PRE": 3, "POST": 4, "GRP": 5
    }
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/type"
    mixer.send(control_path, channel_type_map[channel_type])
    print(mixer.query(control_path))
    
    
    
def set_aux_input_mix_channel_pan_follow(mixer, aux_id, channel_num, pan_follow):
    pan_follow_map = {"OFF": 0, "ON": 129}
    control_path = f"/auxin/{aux_id:02}/mix/{channel_num:02}/panFollow"
    mixer.send(control_path, pan_follow_map[pan_follow])
    print(mixer.query(control_path))
    

def set_aux_input_grp_dca(mixer, aux_id, dca_value):
    control_path = f"/auxin/{aux_id:02}/grp/dca"
    mixer.send(control_path, dca_value)
    print(mixer.query(control_path))
    

def set_aux_input_grp_mute(mixer, aux_id, mute_value):
    control_path = f"/auxin/{aux_id:02}/grp/mute"
    mixer.send(control_path, mute_value)
    print(mixer.query(control_path))



def set_fx_return_channel_mix_on(mixer, fxrtn_id, mix_on):
    mix_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/on"
    mixer.send(control_path, mix_on_map[mix_on])
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_fader(mixer, fxrtn_id, fader_level):
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/fader"
    mixer.send(control_path, fader_level)
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_st(mixer, fxrtn_id, st_on):
    st_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/st"
    mixer.send(control_path, st_on_map[st_on])
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_pan(mixer, fxrtn_id, pan_level):
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/pan"
    mixer.send(control_path, pan_level)
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_mono(mixer, fxrtn_id, mono_on):
    mono_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/mono"
    mixer.send(control_path, mono_on_map[mono_on])
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_mlevel(mixer, fxrtn_id, mlevel_level):
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/mlevel"
    mixer.send(control_path, mlevel_level)
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_channel_on(mixer, fxrtn_id, channel_num, channel_on):
    channel_on_map = {"OFF": 0, "ON": 1}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/{channel_num:02}/on"
    mixer.send(control_path, channel_on_map[channel_on])
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_channel_level(mixer, fxrtn_id, channel_num, channel_level):
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/{channel_num:02}/level"
    mixer.send(control_path, channel_level)
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_channel_pan(mixer, fxrtn_id, channel_num, channel_pan):
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/{channel_num:02}/pan"
    mixer.send(control_path, channel_pan)
    print(mixer.query(control_path))
    

def set_fx_return_channel_mix_channel_type(mixer, fxrtn_id, channel_num, channel_type):
    channel_type_map = {"IN/LC": 0, "<-EQ": 1, "EQ->": 2, "PRE": 3, "POST": 4, "GRP": 5}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/{channel_num:02}/type"
    mixer.send(control_path, channel_type_map[channel_type])
    print(mixer.query(control_path))
    
    
    
def set_fx_return_channel_mix_pan_follow(mixer, fxrtn_id, pan_follow):
    pan_follow_map = {"OFF": 0, "ON": 130}
    control_path = f"/fxrtn/{fxrtn_id:02}/mix/panFollow"
    mixer.send(control_path, pan_follow_map[pan_follow])
    print(mixer.query(control_path))
    

def set_fx_return_channel_grp_dca(mixer, fxrtn_id, dca_value):
    control_path = f"/fxrtn/{fxrtn_id:02}/grp/dca"
    mixer.send(control_path, dca_value)
    print(mixer.query(control_path))
    

def set_fx_return_channel_grp_mute(mixer, fxrtn_id, mute_value):
    control_path = f"/fxrtn/{fxrtn_id:02}/grp/mute"
    mixer.send(control_path, mute_value)
    print(mixer.query(control_path))
    
    
def set_bus_channel_name(mixer, bus_id, name):
    control_path = f"/bus/{bus_id:02}/config/name"
    mixer.send(control_path, name)
    print(mixer.query(control_path))

def set_bus_channel_icon(mixer, bus_id, icon):
    control_path = f"/bus/{bus_id:02}/config/icon"
    mixer.send(control_path, icon)
    print(mixer.query(control_path))

def set_bus_channel_color(mixer, bus_id, color):
    color_map = {"OFF": 0, "RD": 1, "GN": 2, "YE": 3, "BL": 4, "MG": 5, "CY": 6, "WH": 7,
                 "OFFi": 8, "RDi": 9, "GNi": 10, "YEi": 11, "BLi": 12, "MGi": 13, "CYi": 14, "WHi": 15}
    control_path = f"/bus/{bus_id:02}/config/color"
    mixer.send(control_path, color_map[color])
    print(mixer.query(control_path))
    
    
def set_bus_dyn_mix(mixer, bus_id, mix):
    control_path = f"/bus/{bus_id:02}/dyn/mix"
    mixer.send(control_path, mix)
    print(mixer.query(control_path))

def set_bus_dyn_auto(mixer, bus_id, auto):
    control_path = f"/bus/{bus_id:02}/dyn/auto"
    mixer.send(control_path, auto)
    print(mixer.query(control_path))

def set_bus_dyn_filter_on(mixer, bus_id, on):
    control_path = f"/bus/{bus_id:02}/dyn/filter/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_bus_dyn_filter_type(mixer, bus_id, filter_type):
    filter_map = {
        "LC6": 0, "LC12": 1, "HC6": 2, "HC12": 3, "1.0": 4, "2.0": 5, "3.0": 6, "5.0": 7, "10.0": 8
    }
    control_path = f"/bus/{bus_id:02}/dyn/filter/type"
    mixer.send(control_path, filter_map[filter_type])
    print(mixer.query(control_path))

def set_bus_dyn_filter_f(mixer, bus_id, freq):
    control_path = f"/bus/{bus_id:02}/dyn/filter/f"
    mixer.send(control_path, freq)
    print(mixer.query(control_path))

def set_bus_insert_on(mixer, bus_id, on):
    control_path = f"/bus/{bus_id:02}/insert/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_bus_insert_pos(mixer, bus_id, pos):
    control_path = f"/bus/{bus_id:02}/insert/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_bus_insert_sel(mixer, bus_id, sel):
    control_path = f"/bus/{bus_id:02}/insert/sel"
    mixer.send(control_path, sel)
    print(mixer.query(control_path))

def set_bus_eq_on(mixer, bus_id, on):
    control_path = f"/bus/{bus_id:02}/eq/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_bus_eq_type(mixer, bus_id, eq_band, eq_type):
    eq_map = {"LCut": 0, "LShv": 1, "PEQ": 2, "VEQ": 3, "HShv": 4, "HCut": 5}
    control_path = f"/bus/{bus_id:02}/eq/{eq_band}/type"
    mixer.send(control_path, eq_map[eq_type])
    print(mixer.query(control_path))

def set_bus_eq_f(mixer, bus_id, eq_band, freq):
    control_path = f"/bus/{bus_id:02}/eq/{eq_band}/f"
    mixer.send(control_path, freq)
    print(mixer.query(control_path))

def set_bus_eq_g(mixer, bus_id, eq_band, gain):
    control_path = f"/bus/{bus_id:02}/eq/{eq_band}/g"
    mixer.send(control_path, gain)
    print(mixer.query(control_path))

def set_bus_eq_q(mixer, bus_id, eq_band, q):
    control_path = f"/bus/{bus_id:02}/eq/{eq_band}/q"
    mixer.send(control_path, q)
    print(mixer.query(control_path))


def set_bus_mix_on(mixer, bus_id, on):
    control_path = f"/bus/{bus_id:02}/mix/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_bus_mix_fader(mixer, bus_id, fader_level):
    control_path = f"/bus/{bus_id:02}/mix/fader"
    mixer.send(control_path, fader_level)
    print(mixer.query(control_path))

def set_bus_mix_st(mixer, bus_id, st):
    control_path = f"/bus/{bus_id:02}/mix/st"
    mixer.send(control_path, st)
    print(mixer.query(control_path))

def set_bus_mix_pan(mixer, bus_id, pan_level):
    control_path = f"/bus/{bus_id:02}/mix/pan"
    mixer.send(control_path, pan_level)
    print(mixer.query(control_path))

def set_bus_mix_mono(mixer, bus_id, mono):
    control_path = f"/bus/{bus_id:02}/mix/mono"
    mixer.send(control_path, mono)
    print(mixer.query(control_path))

def set_bus_mix_mlevel(mixer, bus_id, mlevel):
    control_path = f"/bus/{bus_id:02}/mix/mlevel"
    mixer.send(control_path, mlevel)
    print(mixer.query(control_path))

def set_bus_mix_on_by_index(mixer, bus_id, mix_index, on):
    control_path = f"/bus/{bus_id:02}/mix/{mix_index:02}/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_bus_mix_level_by_index(mixer, bus_id, mix_index, level):
    control_path = f"/bus/{bus_id:02}/mix/{mix_index:02}/level"
    mixer.send(control_path, level)
    print(mixer.query(control_path))

def set_bus_mix_pan_by_index(mixer, bus_id, mix_index, pan):
    control_path = f"/bus/{bus_id:02}/mix/{mix_index:02}/pan"
    mixer.send(control_path, pan)
    print(mixer.query(control_path))

def set_bus_mix_type_by_index(mixer, bus_id, mix_index, mix_type):
    mix_type_map = {"IN/LC": 0, "<-EQ": 1, "EQ->": 2, "PRE": 3, "POST": 4}
    control_path = f"/bus/{bus_id:02}/mix/{mix_index:02}/type"
    mixer.send(control_path, mix_type_map[mix_type])
    print(mixer.query(control_path))

def set_bus_mix_pan_follow_by_index(mixer, bus_id, mix_index, pan_follow):
    control_path = f"/bus/{bus_id:02}/mix/{mix_index:02}/panFollow"
    mixer.send(control_path, pan_follow)
    print(mixer.query(control_path))

def set_bus_grp_dca(mixer, bus_id, dca_level):
    control_path = f"/bus/{bus_id:02}/grp/dca"
    mixer.send(control_path, dca_level)
    print(mixer.query(control_path))

def set_bus_grp_mute(mixer, bus_id, mute_level):
    control_path = f"/bus/{bus_id:02}/grp/mute"
    mixer.send(control_path, mute_level)
    print(mixer.query(control_path))


def set_mtx_config_name(mixer, mtx_id, name):
    control_path = f"/mtx/{mtx_id:02}/config/name"
    mixer.send(control_path, name)
    print(mixer.query(control_path))

def set_mtx_config_icon(mixer, mtx_id, icon):
    control_path = f"/mtx/{mtx_id:02}/config/icon"
    mixer.send(control_path, icon)
    print(mixer.query(control_path))

def set_mtx_config_color(mixer, mtx_id, color):
    control_path = f"/mtx/{mtx_id:02}/config/color"
    mixer.send(control_path, color)
    print(mixer.query(control_path))

def set_mtx_config_preamp_invert(mixer, mtx_id, invert):
    control_path = f"/mtx/{mtx_id:02}/config/preamp/invert"
    mixer.send(control_path, invert)
    print(mixer.query(control_path))

def set_mtx_dyn_on(mixer, mtx_id, on):
    control_path = f"/mtx/{mtx_id:02}/dyn/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_mtx_dyn_mode(mixer, mtx_id, mode):
    control_path = f"/mtx/{mtx_id:02}/dyn/mode"
    mixer.send(control_path, mode)
    print(mixer.query(control_path))

def set_mtx_dyn_det(mixer, mtx_id, det):
    control_path = f"/mtx/{mtx_id:02}/dyn/det"
    mixer.send(control_path, det)
    print(mixer.query(control_path))

def set_mtx_dyn_env(mixer, mtx_id, env):
    control_path = f"/mtx/{mtx_id:02}/dyn/env"
    mixer.send(control_path, env)
    print(mixer.query(control_path))

def set_mtx_dyn_thr(mixer, mtx_id, thr):
    control_path = f"/mtx/{mtx_id:02}/dyn/thr"
    mixer.send(control_path, thr)
    print(mixer.query(control_path))

def set_mtx_dyn_ratio(mixer, mtx_id, ratio):
    ratio_map = {1.1: 0, 1.3: 1, 1.5: 2, 2.0: 3, 2.5: 4, 3.0: 5, 4.0: 6, 5.0: 7, 7.0: 8, 10: 9, 20: 10, 100: 11}
    control_path = f"/mtx/{mtx_id:02}/dyn/ratio"
    mixer.send(control_path, ratio_map[ratio])
    print(mixer.query(control_path))


def set_mtx_dyn_knee(mixer, mtx_id, knee):
    control_path = f"/mtx/{mtx_id:02}/dyn/knee"
    mixer.send(control_path, knee)
    print(mixer.query(control_path))

def set_mtx_dyn_mgain(mixer, mtx_id, mgain):
    control_path = f"/mtx/{mtx_id:02}/dyn/mgain"
    mixer.send(control_path, mgain)
    print(mixer.query(control_path))

def set_mtx_dyn_attack(mixer, mtx_id, attack):
    control_path = f"/mtx/{mtx_id:02}/dyn/attack"
    mixer.send(control_path, attack)
    print(mixer.query(control_path))

def set_mtx_dyn_hold(mixer, mtx_id, hold):
    control_path = f"/mtx/{mtx_id:02}/dyn/hold"
    mixer.send(control_path, hold)
    print(mixer.query(control_path))

def set_mtx_dyn_release(mixer, mtx_id, release):
    control_path = f"/mtx/{mtx_id:02}/dyn/release"
    mixer.send(control_path, release)
    print(mixer.query(control_path))

def set_mtx_dyn_pos(mixer, mtx_id, pos):
    control_path = f"/mtx/{mtx_id:02}/dyn/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_mtx_dyn_mix(mixer, mtx_id, mix):
    control_path = f"/mtx/{mtx_id:02}/dyn/mix"
    mixer.send(control_path, mix)
    print(mixer.query(control_path))

def set_mtx_dyn_auto(mixer, mtx_id, auto):
    control_path = f"/mtx/{mtx_id:02}/dyn/auto"
    mixer.send(control_path, auto)
    print(mixer.query(control_path))

def set_mtx_dyn_filter_on(mixer, mtx_id, on):
    control_path = f"/mtx/{mtx_id:02}/dyn/filter/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_mtx_dyn_filter_type(mixer, mtx_id, f_type):
    control_path = f"/mtx/{mtx_id:02}/dyn/filter/type"
    mixer.send(control_path, f_type)
    print(mixer.query(control_path))

def set_mtx_dyn_filter_f(mixer, mtx_id, f_value):
    control_path = f"/mtx/{mtx_id:02}/dyn/filter/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_mtx_insert_on(mixer, mtx_id, on):
    control_path = f"/mtx/{mtx_id:02}/insert/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_mtx_insert_pos(mixer, mtx_id, pos):
    control_path = f"/mtx/{mtx_id:02}/insert/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_mtx_insert_sel(mixer, mtx_id, sel):
    control_path = f"/mtx/{mtx_id:02}/insert/sel"
    mixer.send(control_path, sel)
    print(mixer.query(control_path))


def set_mtx_eq_on(mixer, mtx_id, eq_id, on):
    control_path = f"/mtx/{mtx_id:02}/eq/{eq_id}/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_mtx_eq_type(mixer, mtx_id, eq_id, eq_type):
    control_path = f"/mtx/{mtx_id:02}/eq/{eq_id}/type"
    mixer.send(control_path, eq_type)
    print(mixer.query(control_path))

def set_mtx_eq_f(mixer, mtx_id, eq_id, f_value):
    control_path = f"/mtx/{mtx_id:02}/eq/{eq_id}/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_mtx_eq_g(mixer, mtx_id, eq_id, g_value):
    control_path = f"/mtx/{mtx_id:02}/eq/{eq_id}/g"
    mixer.send(control_path, g_value)
    print(mixer.query(control_path))

def set_mtx_eq_q(mixer, mtx_id, eq_id, q_value):
    control_path = f"/mtx/{mtx_id:02}/eq/{eq_id}/q"
    mixer.send(control_path, q_value)
    print(mixer.query(control_path))

def set_mtx_mix_on(mixer, mtx_id, on):
    control_path = f"/mtx/{mtx_id:02}/mix/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_mtx_mix_fader(mixer, mtx_id, fader_value):
    control_path = f"/mtx/{mtx_id:02}/mix/fader"
    mixer.send(control_path, fader_value)
    print(mixer.query(control_path))


def set_main_stereo_dyn_on(mixer, on):
    control_path = "/main/st/dyn/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_dyn_mode(mixer, mode):
    control_path = "/main/st/dyn/mode"
    mixer.send(control_path, mode)
    print(mixer.query(control_path))

def set_main_stereo_dyn_det(mixer, det):
    control_path = "/main/st/dyn/det"
    mixer.send(control_path, det)
    print(mixer.query(control_path))

def set_main_stereo_dyn_env(mixer, env):
    control_path = "/main/st/dyn/env"
    mixer.send(control_path, env)
    print(mixer.query(control_path))

def set_main_stereo_dyn_thr(mixer, thr_value):
    control_path = "/main/st/dyn/thr"
    mixer.send(control_path, thr_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_ratio(mixer, ratio_value):
    control_path = "/main/st/dyn/ratio"
    mixer.send(control_path, ratio_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_knee(mixer, knee_value):
    control_path = "/main/st/dyn/knee"
    mixer.send(control_path, knee_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_mgain(mixer, mgain_value):
    control_path = "/main/st/dyn/mgain"
    mixer.send(control_path, mgain_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_attack(mixer, attack_value):
    control_path = "/main/st/dyn/attack"
    mixer.send(control_path, attack_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_hold(mixer, hold_value):
    control_path = "/main/st/dyn/hold"
    mixer.send(control_path, hold_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_release(mixer, release_value):
    control_path = "/main/st/dyn/release"
    mixer.send(control_path, release_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_pos(mixer, pos):
    control_path = "/main/st/dyn/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_main_stereo_dyn_mix(mixer, mix_value):
    control_path = "/main/st/dyn/mix"
    mixer.send(control_path, mix_value)
    print(mixer.query(control_path))

def set_main_stereo_dyn_auto(mixer, auto):
    control_path = "/main/st/dyn/auto"
    mixer.send(control_path, auto)
    print(mixer.query(control_path))

def set_main_stereo_dyn_filter_on(mixer, on):
    control_path = "/main/st/dyn/filter/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_dyn_filter_type(mixer, filter_type):
    control_path = "/main/st/dyn/filter/type"
    mixer.send(control_path, filter_type)
    print(mixer.query(control_path))

def set_main_stereo_dyn_filter_f(mixer, f_value):
    control_path = "/main/st/dyn/filter/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_main_stereo_insert_on(mixer, on):
    control_path = "/main/st/insert/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_insert_pos(mixer, pos):
    control_path = "/main/st/insert/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_main_stereo_insert_sel(mixer, sel):
    control_path = "/main/st/insert/sel"
    mixer.send(control_path, sel)
    print(mixer.query(control_path))


def set_main_stereo_eq_on(mixer, on):
    control_path = "/main/st/eq/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_eq_type(mixer, eq_num, eq_type):
    control_path = f"/main/st/eq/{eq_num}/type"
    mixer.send(control_path, eq_type)
    print(mixer.query(control_path))

def set_main_stereo_eq_f(mixer, eq_num, f_value):
    control_path = f"/main/st/eq/{eq_num}/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_main_stereo_eq_g(mixer, eq_num, g_value):
    control_path = f"/main/st/eq/{eq_num}/g"
    mixer.send(control_path, g_value)
    print(mixer.query(control_path))

def set_main_stereo_eq_q(mixer, eq_num, q_value):
    control_path = f"/main/st/eq/{eq_num}/q"
    mixer.send(control_path, q_value)
    print(mixer.query(control_path))

def set_main_stereo_mix_on(mixer, on):
    control_path = "/main/st/mix/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_mix_fader(mixer, fader_value):
    control_path = "/main/st/mix/fader"
    mixer.send(control_path, fader_value)
    print(mixer.query(control_path))

def set_main_stereo_mix_pan(mixer, pan_value):
    control_path = "/main/st/mix/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))

def set_main_stereo_mix_channel_on(mixer, channel_num, on):
    control_path = f"/main/st/mix/{channel_num}/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_stereo_mix_channel_level(mixer, channel_num, level_value):
    control_path = f"/main/st/mix/{channel_num}/level"
    mixer.send(control_path, level_value)
    print(mixer.query(control_path))

def set_main_stereo_mix_channel_pan(mixer, channel_num, pan_value):
    control_path = f"/main/st/mix/{channel_num}/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))

def set_main_stereo_mix_channel_type(mixer, channel_num, channel_type):
    control_path = f"/main/st/mix/{channel_num}/type"
    mixer.send(control_path, channel_type)
    print(mixer.query(control_path))

def set_main_stereo_mix_channel_pan_follow(mixer, channel_num, pan_follow):
    control_path = f"/main/st/mix/{channel_num}/panFollow"
    mixer.send(control_path, pan_follow)
    print(mixer.query(control_path))


def set_main_mono_dyn_on(mixer, on):
    control_path = "/main/m/dyn/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_mono_dyn_mode(mixer, mode):
    control_path = "/main/m/dyn/mode"
    mixer.send(control_path, mode)
    print(mixer.query(control_path))

def set_main_mono_dyn_det(mixer, det):
    control_path = "/main/m/dyn/det"
    mixer.send(control_path, det)
    print(mixer.query(control_path))

def set_main_mono_dyn_env(mixer, env):
    control_path = "/main/m/dyn/env"
    mixer.send(control_path, env)
    print(mixer.query(control_path))

def set_main_mono_dyn_thr(mixer, thr):
    control_path = "/main/m/dyn/thr"
    mixer.send(control_path, thr)
    print(mixer.query(control_path))

def set_main_mono_dyn_ratio(mixer, ratio):
    control_path = "/main/m/dyn/ratio"
    mixer.send(control_path, ratio)
    print(mixer.query(control_path))

def set_main_mono_dyn_knee(mixer, knee):
    control_path = "/main/m/dyn/knee"
    mixer.send(control_path, knee)
    print(mixer.query(control_path))

def set_main_mono_dyn_mgain(mixer, mgain):
    control_path = "/main/m/dyn/mgain"
    mixer.send(control_path, mgain)
    print(mixer.query(control_path))

def set_main_mono_dyn_attack(mixer, attack):
    control_path = "/main/m/dyn/attack"
    mixer.send(control_path, attack)
    print(mixer.query(control_path))

def set_main_mono_dyn_hold(mixer, hold):
    control_path = "/main/m/dyn/hold"
    mixer.send(control_path, hold)
    print(mixer.query(control_path))

def set_main_mono_dyn_release(mixer, release):
    control_path = "/main/m/dyn/release"
    mixer.send(control_path, release)
    print(mixer.query(control_path))

def set_main_mono_dyn_pos(mixer, pos):
    control_path = "/main/m/dyn/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_main_mono_dyn_mix(mixer, mix):
    control_path = "/main/m/dyn/mix"
    mixer.send(control_path, mix)
    print(mixer.query(control_path))

def set_main_mono_dyn_auto(mixer, auto):
    control_path = "/main/m/dyn/auto"
    mixer.send(control_path, auto)
    print(mixer.query(control_path))

def set_main_mono_dyn_filter_on(mixer, on):
    control_path = "/main/m/dyn/filter/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_mono_dyn_filter_type(mixer, filter_type):
    control_path = "/main/m/dyn/filter/type"
    mixer.send(control_path, filter_type)
    print(mixer.query(control_path))

def set_main_mono_dyn_filter_f(mixer, f_value):
    control_path = "/main/m/dyn/filter/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_main_mono_insert_on(mixer, on):
    control_path = "/main/m/insert/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_mono_insert_pos(mixer, pos):
    control_path = "/main/m/insert/pos"
    mixer.send(control_path, pos)
    print(mixer.query(control_path))

def set_main_mono_insert_sel(mixer, sel_value):
    control_path = "/main/m/insert/sel"
    mixer.send(control_path, sel_value)
    print(mixer.query(control_path))


def set_main_mono_eq_f(mixer, eq_num, f_value):
    control_path = f"/main/m/eq/{eq_num}/f"
    mixer.send(control_path, f_value)
    print(mixer.query(control_path))

def set_main_mono_eq_g(mixer, eq_num, g_value):
    control_path = f"/main/m/eq/{eq_num}/g"
    mixer.send(control_path, g_value)
    print(mixer.query(control_path))

def set_main_mono_eq_q(mixer, eq_num, q_value):
    control_path = f"/main/m/eq/{eq_num}/q"
    mixer.send(control_path, q_value)
    print(mixer.query(control_path))

def set_main_mono_mix_on(mixer, on):
    control_path = "/main/m/mix/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_mono_mix_fader(mixer, fader_value):
    control_path = "/main/m/mix/fader"
    mixer.send(control_path, fader_value)
    print(mixer.query(control_path))

def set_main_mono_mix_on(mixer, mix_num, on):
    control_path = f"/main/m/mix/{mix_num}/on"
    mixer.send(control_path, on)
    print(mixer.query(control_path))

def set_main_mono_mix_level(mixer, mix_num, level_value):
    control_path = f"/main/m/mix/{mix_num}/level"
    mixer.send(control_path, level_value)
    print(mixer.query(control_path))

def set_main_mono_mix_pan(mixer, mix_num, pan_value):
    control_path = f"/main/m/mix/{mix_num}/pan"
    mixer.send(control_path, pan_value)
    print(mixer.query(control_path))

def set_main_mono_mix_type(mixer, mix_num, type_value):
    control_path = f"/main/m/mix/{mix_num}/type"
    mixer.send(control_path, type_value)
    print(mixer.query(control_path))

def set_main_mono_mix_pan_follow(mixer, mix_num, follow_value):
    control_path = f"/main/m/mix/{mix_num}/panFollow"
    mixer.send(control_path, follow_value)
    print(mixer.query(control_path))


def set_dca_on(mixer, dca_num, on_value):
    control_path = f"/dca/{dca_num}/on"
    mixer.send(control_path, on_value)
    print(mixer.query(control_path))

def set_dca_fader(mixer, dca_num, fader_value):
    control_path = f"/dca/{dca_num}/fader"
    mixer.send(control_path, fader_value)
    print(mixer.query(control_path))

def set_dca_name(mixer, dca_num, name_value):
    control_path = f"/dca/{dca_num}/config/name"
    mixer.send(control_path, name_value)
    print(mixer.query(control_path))

def set_dca_icon(mixer, dca_num, icon_value):
    control_path = f"/dca/{dca_num}/config/icon"
    mixer.send(control_path, icon_value)
    print(mixer.query(control_path))

def set_dca_color(mixer, dca_num, color_value):
    control_path = f"/dca/{dca_num}/config/color"
    mixer.send(control_path, color_value)
    print(mixer.query(control_path))

def set_fx_type(mixer, fx_num, fx_type):
    control_path = f"/fx/{fx_num}/type"
    mixer.send(control_path, fx_type)
    print(mixer.query(control_path))

def set_fx_source_left(mixer, fx_num, source_value):
    control_path = f"/fx/{fx_num}/source/l"
    mixer.send(control_path, source_value)
    print(mixer.query(control_path))

def set_fx_source_right(mixer, fx_num, source_value):
    control_path = f"/fx/{fx_num}/source/r"
    mixer.send(control_path, source_value)
    print(mixer.query(control_path))

def set_fx_parameter(mixer, fx_num, param_num, param_value):
    control_path = f"/fx/{fx_num}/par/{param_num}"
    mixer.send(control_path, param_value)
    print(mixer.query(control_path))

def set_fx5_type(mixer, fx_type):
    control_path = "/fx/5/type"
    mixer.send(control_path, fx_type)
    print(mixer.query(control_path))

def set_fx6_type(mixer, fx_type):
    control_path = "/fx/6/type"
    mixer.send(control_path, fx_type)
    print(mixer.query(control_path))

def set_fx7_type(mixer, fx_type):
    control_path = "/fx/7/type"
    mixer.send(control_path, fx_type)
    print(mixer.query(control_path))

def set_fx8_type(mixer, fx_type):
    control_path = "/fx/8/type"
    mixer.send(control_path, fx_type)
    print(mixer.query(control_path))

def set_fx_parameter(mixer, fx_num, param_num, param_value):
    control_path = f"/fx/{fx_num}/par/{param_num}"
    mixer.send(control_path, param_value)
    print(mixer.query(control_path))

def set_p16_output_src(mixer, output_num, src_value):
    control_path = f"/outputs/p16/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_p16_output_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/p16/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))

def set_p16_output_invert(mixer, output_num, invert_value):
    control_path = f"/outputs/p16/{output_num}/invert"
    mixer.send(control_path, invert_value)
    print(mixer.query(control_path))

def set_p16_output_iq_group(mixer, output_num, group_value):
    control_path = f"/outputs/p16/{output_num}/iQ/group"
    mixer.send(control_path, group_value)
    print(mixer.query(control_path))

def set_p16_output_iq_speaker(mixer, output_num, speaker_value):
    control_path = f"/outputs/p16/{output_num}/iQ/speaker"
    mixer.send(control_path, speaker_value)
    print(mixer.query(control_path))


# Outputs Main [01...16]
def set_output_main_src(mixer, output_num, src_value):
    control_path = f"/outputs/main/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_output_main_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/main/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))

def set_output_main_invert(mixer, output_num, invert_value):
    control_path = f"/outputs/main/{output_num}/invert"
    mixer.send(control_path, invert_value)
    print(mixer.query(control_path))

def set_output_main_delay_on(mixer, output_num, delay_on_value):
    control_path = f"/outputs/main/{output_num}/delay/on"
    mixer.send(control_path, delay_on_value)
    print(mixer.query(control_path))

def set_output_main_delay_time(mixer, output_num, delay_time_value):
    control_path = f"/outputs/main/{output_num}/delay/time"
    mixer.send(control_path, delay_time_value)
    print(mixer.query(control_path))


# Outputs Aux [01...06]
def set_output_aux_src(mixer, output_num, src_value):
    control_path = f"/outputs/aux/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_output_aux_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/aux/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))

def set_output_aux_invert(mixer, output_num, invert_value):
    control_path = f"/outputs/aux/{output_num}/invert"
    mixer.send(control_path, invert_value)
    print(mixer.query(control_path))


# Outputs P16 [01...16]
def set_output_p16_src(mixer, output_num, src_value):
    control_path = f"/outputs/p16/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_output_p16_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/p16/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))

def set_output_p16_invert(mixer, output_num, invert_value):
    control_path = f"/outputs/p16/{output_num}/invert"
    mixer.send(control_path, invert_value)
    print(mixer.query(control_path))

def set_output_p16_iQ_group(mixer, output_num, iQ_group_value):
    control_path = f"/outputs/p16/{output_num}/iQ/group"
    mixer.send(control_path, iQ_group_value)
    print(mixer.query(control_path))

def set_output_p16_iQ_speaker(mixer, output_num, iQ_speaker_value):
    control_path = f"/outputs/p16/{output_num}/iQ/speaker"
    mixer.send(control_path, iQ_speaker_value)
    print(mixer.query(control_path))


# Outputs P16 [01...16] iQ speaker parameters
def set_output_p16_iQ_eq(mixer, output_num, eq_value):
    control_path = f"/outputs/p16/{output_num}/iQ/eq"
    mixer.send(control_path, eq_value)
    print(mixer.query(control_path))

def set_output_p16_iQ_model(mixer, output_num, model_value):
    control_path = f"/outputs/p16/{output_num}/iQ/model"
    mixer.send(control_path, model_value)
    print(mixer.query(control_path))


# Outputs AES [01...02] parameters
def set_output_aes_src(mixer, output_num, src_value):
    control_path = f"/outputs/aes/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_output_aes_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/aes/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))

def set_output_aes_invert(mixer, output_num, invert_value):
    control_path = f"/outputs/aes/{output_num}/invert"
    mixer.send(control_path, invert_value)
    print(mixer.query(control_path))


# Outputs REC [01...02] parameters
def set_output_rec_src(mixer, output_num, src_value):
    control_path = f"/outputs/rec/{output_num}/src"
    mixer.send(control_path, src_value)
    print(mixer.query(control_path))

def set_output_rec_pos(mixer, output_num, pos_value):
    control_path = f"/outputs/rec/{output_num}/pos"
    mixer.send(control_path, pos_value)
    print(mixer.query(control_path))


# Headamp gain parameters
def set_headamp_gain(mixer, headamp_index, gain_value):
    control_path = f"/headamp/{headamp_index}/gain"
    mixer.send(control_path, gain_value)
    print(mixer.query(control_path))

def set_headamp_phantom(mixer, headamp_index, phantom_value):
    control_path = f"/headamp/{headamp_index}/phantom"
    mixer.send(control_path, phantom_value)
    print(mixer.query(control_path))

# Get actual headamp used as source for a given input
def get_actual_headamp_for_input(mixer, input_index):
    control_path = f"/-ha/{input_index}/index"
    result = mixer.query(control_path)
    print(f"Input {input_index}: Actual headamp used = {result}")
    return result

# Insert FX L input to a channel
def set_insert_fx_left(mixer, fx_index, channel_index):
    control_path = f"/-insert/fx{fx_index}L"
    mixer.send(control_path, channel_index)
    print(mixer.query(control_path))

# Insert FX R input to a channel
def set_insert_fx_right(mixer, fx_index, channel_index):
    control_path = f"/-insert/fx{fx_index}R"
    mixer.send(control_path, channel_index)
    print(mixer.query(control_path))

# Insert Aux input to a channel
def set_insert_aux(mixer, aux_index, channel_index):
    control_path = f"/-insert/aux{aux_index}"
    mixer.send(control_path, channel_index)
    print(mixer.query(control_path))


# /showdump none Requests the X32/M32 to send all Cue, Scene, and Snippet related data.
def request_show_dump(mixer):
    control_path = "/showdump"
    mixer.send(control_path, "none")
    print(mixer.query(control_path))

# /‐show/prepos/current int Scene page cue, scene, or snippet slot highlighted line/index is <int> value.
def set_current_scene_slot(mixer, slot_value):
    control_path = "/‐show/prepos/current"
    mixer.send(control_path, slot_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/name string Name of the current show
def get_current_show_name(mixer):
    control_path = "/‐show/showfile/show/name"
    print(mixer.query(control_path))

# /‐show/showfile/show/inputs int Param safe page Scene safe parameters Input channels selection
def set_scene_safe_input_channels(mixer, param_safe_value):
    control_path = "/‐show/showfile/show/inputs"
    mixer.send(control_path, param_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/mxsends int Param safe page Scene safe parameters Input channels selection (16 bits bitmap)
def set_scene_safe_mx_sends(mixer, param_safe_value):
    control_path = "/‐show/showfile/show/mxsends"
    mixer.send(control_path, param_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/mxbuses int Param safe page Scene safe parameters Mix Buses selection
def set_scene_safe_mix_buses(mixer, param_safe_value):
    control_path = "/‐show/showfile/show/mxbuses"
    mixer.send(control_path, param_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/console int Param safe page Scene safe parameters Console selection (4 bits bitmap)
def set_scene_safe_console(mixer, param_safe_value):
    control_path = "/‐show/showfile/show/console"
    mixer.send(control_path, param_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/chan16 int Chan safe page Chanel safe parameters selection (16 bits bitmap)
def set_channel_safe_parameters(mixer, chan_safe_value):
    control_path = "/‐show/showfile/show/chan16"
    mixer.send(control_path, chan_safe_value)
    print(mixer.query(control_path))


# /‐show/showfile/show/chan32 int Chan safe page Chanel safe parameters selection (16 bits bitmap)
def set_channel_safe_parameters_32(mixer, chan_safe_value):
    control_path = "/‐show/showfile/show/chan32"
    mixer.send(control_path, chan_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/return int Chan safe page Return & Aux safe parameters selection (16 bits bitmap)
def set_return_aux_safe_parameters(mixer, return_aux_safe_value):
    control_path = "/‐show/showfile/show/return"
    mixer.send(control_path, return_aux_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/buses int Chan safe page Buses safe parameters selection (16 bits bitmap)
def set_buses_safe_parameters(mixer, buses_safe_value):
    control_path = "/‐show/showfile/show/buses"
    mixer.send(control_path, buses_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/lrmtxdca int Chan safe page Buses safe parameters selection (16 bits bitmap)
def set_lr_mtx_dca_safe_parameters(mixer, lr_mtx_dca_safe_value):
    control_path = "/‐show/showfile/show/lrmtxdca"
    mixer.send(control_path, lr_mtx_dca_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/show/effects int Chan safe page Effects Slots safe parameters selection (8 bits bitmap)
def set_effects_slots_safe_parameters(mixer, effects_safe_value):
    control_path = "/‐show/showfile/show/effects"
    mixer.send(control_path, effects_safe_value)
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/numb int Number of cue in the form xxx.x.x, saved at position [000‐099]
def get_cue_number(mixer, cue_position):
    control_path = f"/‐show/showfile/cue/{cue_position}/numb"
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/name string Name of cue at position [000‐099]
def get_cue_name(mixer, cue_position):
    control_path = f"/‐show/showfile/cue/{cue_position}/name"
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/skip int 0 (no Skip) or 1 (Skip) for cue at position [000‐099]
def set_cue_skip(mixer, cue_position, skip_value):
    control_path = f"/‐show/showfile/cue/{cue_position}/skip"
    mixer.send(control_path, skip_value)
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/scene int Associate Scene <int> with cue at position [000‐099]
def associate_scene_with_cue(mixer, cue_position, scene_value):
    control_path = f"/‐show/showfile/cue/{cue_position}/scene"
    mixer.send(control_path, scene_value)
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/bit int Associate Snippet <int> with cue at position [000‐099]
def associate_snippet_with_cue(mixer, cue_position, snippet_value):
    control_path = f"/‐show/showfile/cue/{cue_position}/bit"
    mixer.send(control_path, snippet_value)
    print(mixer.query(control_path))

# /‐show/showfile/cue/[000‐099]/miditype int Associate MIDI type <int> with cue at position [000‐099].
def associate_midi_type_with_cue(mixer, cue_position, midi_type_value):
    control_path = f"/‐show/showfile/cue/{cue_position}/miditype"
    mixer.send(control_path, midi_type_value)
    print(mixer.query(control_path))


# /‐show/showfile/scene/[000‐099]/name string Scene “Name” parameter for scene [000‐099]
def get_scene_name(mixer, scene_position):
    control_path = f"/‐show/showfile/scene/{scene_position}/name"
    print(mixer.query(control_path))

# /‐show/showfile/scene/[000‐099]/notes string Scene “Notes” parameter for scene [000‐099]
def get_scene_notes(mixer, scene_position):
    control_path = f"/‐show/showfile/scene/{scene_position}/notes"
    print(mixer.query(control_path))

# /‐show/showfile/scene/[000‐099]/safes %int Scene “Scene Safes” parameters selection for scene [000‐099]
def set_scene_safes(mixer, scene_position, safes_value):
    control_path = f"/‐show/showfile/scene/{scene_position}/safes"
    mixer.send(control_path, safes_value)
    print(mixer.query(control_path))

# /‐show/showfile/scene/[000‐099]/hasdata int Scene at position [000‐099] has valid data
def check_scene_data(mixer, scene_position):
    control_path = f"/‐show/showfile/scene/{scene_position}/hasdata"
    print(mixer.query(control_path))

# /‐show/showfile/snippet/[000‐099]/name string Snippet “Name” parameter for Snippet [000‐099]
def get_snippet_name(mixer, snippet_position):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/name"
    print(mixer.query(control_path))

# /‐show/showfile/snippet/[000‐099]/eventtyp %int Parameter Filters & Effects affected by snippet in the form of bitwise operation
def set_snippet_event_type(mixer, snippet_position, event_type_value):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/eventtyp"
    mixer.send(control_path, event_type_value)
    print(mixer.query(control_path))


# /‐show/showfile/snippet/[000‐099]/channels %int Channels affected by snippet in the form of bitwise operation
def set_snippet_channels(mixer, snippet_position, channels_value):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/channels"
    mixer.send(control_path, channels_value)
    print(mixer.query(control_path))

# /‐show/showfile/snippet/[000‐099]/auxbuses %int Returns and Buses affected by snippet in the form of bitwise operation
def set_snippet_aux_buses(mixer, snippet_position, aux_buses_value):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/auxbuses"
    mixer.send(control_path, aux_buses_value)
    print(mixer.query(control_path))

# /‐show/showfile/snippet/[000‐099]/maingrps %int Main/Matrix/Group affected by snippet in the form of bitwise operation
def set_snippet_main_groups(mixer, snippet_position, main_groups_value):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/maingrps"
    mixer.send(control_path, main_groups_value)
    print(mixer.query(control_path))

# /‐show/showfile/snippet/[000‐099]/hasdata int Snippet at position [000‐099] has valid data
def check_snippet_data(mixer, snippet_position):
    control_path = f"/‐show/showfile/snippet/{snippet_position}/hasdata"
    print(mixer.query(control_path))


# /‐libs/fx/[001‐100]/pos int The position of the effect preset number [001‐100]
def get_effect_preset_position(mixer, preset_number):
    control_path = f"/‐libs/fx/{preset_number:03d}/pos"
    print(mixer.query(control_path))

# /‐libs/fx/[001‐100]/name string Name of the effect preset
def get_effect_preset_name(mixer, preset_number):
    control_path = f"/‐libs/fx/{preset_number:03d}/name"
    print(mixer.query(control_path))

# /‐libs/fx/[001‐100]/type int Type of the effect preset
def get_effect_preset_type(mixer, preset_number):
    control_path = f"/‐libs/fx/{preset_number:03d}/type"
    print(mixer.query(control_path))

# /‐libs/fx/[001‐100]/flags %int Use as an int to list the effect type “Ambiance”, “Plate Reverb”, etc. at the right of the effect name on the X32/M32 screen. 38 Note: int values do not match with FX enums!
def get_effect_preset_flags(mixer, preset_number):
    control_path = f"/‐libs/fx/{preset_number:03d}/flags"
    print(mixer.query(control_path))

# /‐libs/fx/[001‐100]/hasdata int {0, 1} depending on the validity of the effect preset.
def check_effect_preset_data(mixer, preset_number):
    control_path = f"/‐libs/fx/{preset_number:03d}/hasdata"
    print(mixer.query(control_path))


# /‐libs/r/[001‐100]/pos int The position of the routing preset number [001‐100]
def get_routing_preset_position(mixer, preset_number):
    control_path = f"/‐libs/r/{preset_number:03d}/pos"
    print(mixer.query(control_path))

# /‐libs/r/[001‐100]/name string Name of the routing preset
def get_routing_preset_name(mixer, preset_number):
    control_path = f"/‐libs/r/{preset_number:03d}/name"
    print(mixer.query(control_path))

# /‐libs/r/[001‐100]/type int Type of the routing preset
def get_routing_preset_type(mixer, preset_number):
    control_path = f"/‐libs/r/{preset_number:03d}/type"
    print(mixer.query(control_path))

# /‐libs/r/[001‐100]/flags %int Unused (all 0).
def get_routing_preset_flags(mixer, preset_number):
    control_path = f"/‐libs/r/{preset_number:03d}/flags"
    print(mixer.query(control_path))

# /‐libs/r/[001‐100]/hasdata int {0, 1} depending on the validity of the routing preset.
def check_routing_preset_data(mixer, preset_number):
    control_path = f"/‐libs/r/{preset_number:03d}/hasdata"
    print(mixer.query(control_path))

# /‐libs/mon/[001‐100]/pos int The position of the AES/DP48 preset number [001‐100]
def get_monitor_preset_position(mixer, preset_number):
    control_path = f"/‐libs/mon/{preset_number:03d}/pos"
    print(mixer.query(control_path))


# /‐libs/mon/[001‐100]/name string Name of the AES/DP48 preset
def get_aes_dp48_preset_name(mixer, preset_number):
    control_path = f"/‐libs/mon/{preset_number:03d}/name"
    print(mixer.query(control_path))

# /‐libs/mon/[001‐100]/type int Type of the AES/DP48 preset
def get_aes_dp48_preset_type(mixer, preset_number):
    control_path = f"/‐libs/mon/{preset_number:03d}/type"
    print(mixer.query(control_path))

# /‐libs/mon/[001‐100]/flags %int Unused (all 0).
def get_aes_dp48_preset_flags(mixer, preset_number):
    control_path = f"/‐libs/mon/{preset_number:03d}/flags"
    print(mixer.query(control_path))

# /‐libs/mon/[001‐100]/hasdata int {0, 1} depending on the validity of the AES/DP48 preset.
def check_aes_dp48_preset_data(mixer, preset_number):
    control_path = f"/‐libs/mon/{preset_number:03d}/hasdata"
    print(mixer.query(control_path))

# /copy string, int, int Copies an X32/M32 internal set to another.
def copy_internal_set(mixer, set_type, source_index, destination_index):
    command = f"/copy,{set_type},{source_index},{destination_index}"
    print(mixer.execute(command))


# /add string, int, string Adds a cue element to the current show in the X32/M32 internal memory.
def add_cue(mixer, cue_name, cue_index, cue_description):
    command = f"/add,{cue_name},{cue_index},{cue_description}"
    print(mixer.execute(command))

# /save string, int, [int | string, …] Saves or updates in the X32/M32 internal memory a scene, snippet, or preset.
def save_internal_object(mixer, object_type, *params):
    command = f"/save,{object_type}"
    for param in params:
        command += f",{param}"
    print(mixer.execute(command))


# /load string, int [,int[, %int]] Loads from the X32/M32 internal memory a scene, snippet, or a preset.
def load_internal_object(mixer, object_type, index, *params):
    command = f"/load,{object_type},{index}"
    
    if object_type == 'libchan':
        channel_index, scope = params
        command += f",{channel_index},{scope}"
    elif object_type == 'libfx':
        effect_index = params[0]
        command += f",{effect_index}"
    
    print(mixer.execute(command))


# /rename string, int, string Renames in the X32/M32 internal memory a scene, snippet, or a preset listed at a given index.
def rename_internal_object(mixer, object_type, index, new_name):
    command = f"/rename,{object_type},{index},{new_name}"
    print(mixer.execute(command))


# /delete string, int Deletes from the X32/M32 internal memory an element at the given index.
def delete_internal_object(mixer, object_type, index):
    command = f"/delete,{object_type},{index}"
    print(mixer.execute(command))


# Get preferences data
def get_preferences(mixer):
    preferences = {}
    preferences["style"] = mixer.execute("/-prefs/style").strip()
    preferences["bright"] = mixer.execute("/-prefs/bright").strip()
    preferences["lcdcont"] = mixer.execute("/-prefs/lcdcont").strip()
    preferences["ledbright"] = mixer.execute("/-prefs/ledbright").strip()
    preferences["lamp"] = mixer.execute("/-prefs/lamp").strip()
    preferences["lampon"] = mixer.execute("/-prefs/lampon").strip()
    preferences["clockrate"] = mixer.execute("/-prefs/clockrate").strip()
    preferences["clocksource"] = mixer.execute("/-prefs/clocksource").strip()
    return preferences

# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None):
    if style:
        mixer.execute(f"/-prefs/style {style}")
    if bright:
        mixer.execute(f"/-prefs/bright {bright}")
    if lcdcont:
        mixer.execute(f"/-prefs/lcdcont {lcdcont}")
    if ledbright:
        mixer.execute(f"/-prefs/ledbright {ledbright}")
    if lamp:
        mixer.execute(f"/-prefs/lamp {lamp}")
    if lampon is not None:
        mixer.execute(f"/-prefs/lampon {int(lampon)}")
    if clockrate is not None:
        mixer.execute(f"/-prefs/clockrate {clockrate}")
    if clocksource is not None:
        mixer.execute(f"/-prefs/clocksource {clocksource}")

# Getting preferences data
preferences_data = get_preferences(mixer)
print(preferences_data)

# Setting preferences data
set_preferences(mixer, bright=50, lampon=True, clockrate=0)


# Get preferences data
def get_preferences(mixer):
    preferences = {}
    preferences["style"] = mixer.execute("/-prefs/style").strip()
    preferences["bright"] = mixer.execute("/-prefs/bright").strip()
    preferences["lcdcont"] = mixer.execute("/-prefs/lcdcont").strip()
    preferences["ledbright"] = mixer.execute("/-prefs/ledbright").strip()
    preferences["lamp"] = mixer.execute("/-prefs/lamp").strip()
    preferences["lampon"] = mixer.execute("/-prefs/lampon").strip()
    preferences["clockrate"] = mixer.execute("/-prefs/clockrate").strip()
    preferences["clocksource"] = mixer.execute("/-prefs/clocksource").strip()
    preferences["confirm_general"] = mixer.execute("/-prefs/confirm_general").strip()
    preferences["confirm_overwrite"] = mixer.execute("/-prefs/confirm_overwrite").strip()
    preferences["confirm_sceneload"] = mixer.execute("/-prefs/confirm_sceneload").strip()
    preferences["viewrtn"] = mixer.execute("/-prefs/viewrtn").strip()
    preferences["selfollowsbank"] = mixer.execute("/-prefs/selfollowsbank").strip()
    preferences["scene_advance"] = mixer.execute("/-prefs/scene_advance").strip()
    preferences["safe_masterlevels"] = mixer.execute("/-prefs/safe_masterlevels").strip()
    preferences["haflags"] = mixer.execute("/-prefs/haflags").strip()
    preferences["autosel"] = mixer.execute("/-prefs/autosel").strip()
    return preferences

# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None):
    if style:
        mixer.execute(f"/-prefs/style {style}")
    if bright:
        mixer.execute(f"/-prefs/bright {bright}")
    if lcdcont:
        mixer.execute(f"/-prefs/lcdcont {lcdcont}")
    if ledbright:
        mixer.execute(f"/-prefs/ledbright {ledbright}")
    if lamp:
        mixer.execute(f"/-prefs/lamp {lamp}")
    if lampon is not None:
        mixer.execute(f"/-prefs/lampon {int(lampon)}")
    if clockrate is not None:
        mixer.execute(f"/-prefs/clockrate {clockrate}")
    if clocksource is not None:
        mixer.execute(f"/-prefs/clocksource {clocksource}")
    if confirm_general is not None:
        mixer.execute(f"/-prefs/confirm_general {confirm_general}")
    if confirm_overwrite is not None:
        mixer.execute(f"/-prefs/confirm_overwrite {confirm_overwrite}")
    if confirm_sceneload is not None:
        mixer.execute(f"/-prefs/confirm_sceneload {confirm_sceneload}")
    if viewrtn is not None:
        mixer.execute(f"/-prefs/viewrtn {viewrtn}")
    if selfollowsbank is not None:
        mixer.execute(f"/-prefs/selfollowsbank {selfollowsbank}")
    if scene_advance is not None:
        mixer.execute(f"/-prefs/scene_advance {scene_advance}")
    if safe_masterlevels is not None:
        mixer.execute(f"/-prefs/safe_masterlevels {safe_masterlevels}")
    if haflags is not None:
        mixer.execute(f"/-prefs/haflags {haflags}")
    if autosel is not None:
        mixer.execute(f"/-prefs/autosel {autosel}")


# Getting preferences data
preferences_data = get_preferences(mixer)
print(preferences_data)

# Setting preferences data
set_preferences(mixer, confirm_general="ON", viewrtn="ON", haflags=5)


# Get preferences data
def get_preferences(mixer):
    preferences = {}
    preferences["style"] = mixer.execute("/-prefs/style").strip()
    preferences["bright"] = mixer.execute("/-prefs/bright").strip()
    preferences["lcdcont"] = mixer.execute("/-prefs/lcdcont").strip()
    preferences["ledbright"] = mixer.execute("/-prefs/ledbright").strip()
    preferences["lamp"] = mixer.execute("/-prefs/lamp").strip()
    preferences["lampon"] = mixer.execute("/-prefs/lampon").strip()
    preferences["clockrate"] = mixer.execute("/-prefs/clockrate").strip()
    preferences["clocksource"] = mixer.execute("/-prefs/clocksource").strip()
    preferences["confirm_general"] = mixer.execute("/-prefs/confirm_general").strip()
    preferences["confirm_overwrite"] = mixer.execute("/-prefs/confirm_overwrite").strip()
    preferences["confirm_sceneload"] = mixer.execute("/-prefs/confirm_sceneload").strip()
    preferences["viewrtn"] = mixer.execute("/-prefs/viewrtn").strip()
    preferences["selfollowsbank"] = mixer.execute("/-prefs/selfollowsbank").strip()
    preferences["scene_advance"] = mixer.execute("/-prefs/scene_advance").strip()
    preferences["safe_masterlevels"] = mixer.execute("/-prefs/safe_masterlevels").strip()
    preferences["haflags"] = mixer.execute("/-prefs/haflags").strip()
    preferences["autosel"] = mixer.execute("/-prefs/autosel").strip()
    preferences["show_control"] = mixer.execute("/-prefs/show_control").strip()
    preferences["clockmode"] = mixer.execute("/-prefs/clockmode").strip()
    preferences["hardmute"] = mixer.execute("/-prefs/hardmute").strip()
    preferences["dcamute"] = mixer.execute("/-prefs/dcamute").strip()
    preferences["invertmutes"] = mixer.execute("/-prefs/invertmutes").strip()
    preferences["name"] = mixer.execute("/-prefs/name").strip()
    preferences["rec_control"] = mixer.execute("/-prefs/rec_control").strip()
    preferences["fastFaders"] = mixer.execute("/-prefs/fastFaders").strip()
    return preferences

# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None):
    if style:
        mixer.execute(f"/-prefs/style {style}")
    if bright:
        mixer.execute(f"/-prefs/bright {bright}")
    if lcdcont:
        mixer.execute(f"/-prefs/lcdcont {lcdcont}")
    if ledbright:
        mixer.execute(f"/-prefs/ledbright {ledbright}")
    if lamp:
        mixer.execute(f"/-prefs/lamp {lamp}")
    if lampon is not None:
        mixer.execute(f"/-prefs/lampon {int(lampon)}")
    if clockrate is not None:
        mixer.execute(f"/-prefs/clockrate {clockrate}")
    if clocksource is not None:
        mixer.execute(f"/-prefs/clocksource {clocksource}")
    if confirm_general is not None:
        mixer.execute(f"/-prefs/confirm_general {confirm_general}")
    if confirm_overwrite is not None:
        mixer.execute(f"/-prefs/confirm_overwrite {confirm_overwrite}")
    if confirm_sceneload is not None:
        mixer.execute(f"/-prefs/confirm_sceneload {confirm_sceneload}")
    if viewrtn is not None:
        mixer.execute(f"/-prefs/viewrtn {viewrtn}")
    if selfollowsbank is not None:
        mixer.execute(f"/-prefs/selfollowsbank {selfollowsbank}")
    if scene_advance is not None:
        mixer.execute(f"/-prefs/scene_advance {scene_advance}")
    if safe_masterlevels is not None:
        mixer.execute(f"/-prefs/safe_masterlevels {safe_masterlevels}")
    if haflags is not None:
        mixer.execute(f"/-prefs/haflags {haflags}")
    if autosel is not None:
        mixer.execute(f"/-prefs/autosel {autosel}")
    if show_control is not None:
        mixer.execute(f"/-prefs/show_control {show_control}")
    if clockmode is not None:
        mixer.execute(f"/-prefs/clockmode {clockmode}")
    if hardmute is not None:
        mixer.execute(f"/-prefs/hardmute {hardmute}")
    if dcamute is not None:
        mixer.execute(f"/-prefs/dcamute {dcamute}")
    if invertmutes is not None:
        mixer.execute(f"/-prefs/invertmutes {invertmutes}")
    if name:
        mixer.execute(f"/-prefs/name {name}")
    if rec_control is not None:
        mixer.execute(f"/-prefs/rec_control {rec_control}")
    if fastFaders is not None:
        mixer.execute(f"/-prefs/fastFaders {fastFaders}")

# Getting preferences data
preferences_data = get_preferences(mixer)
print(preferences_data)

# Setting preferences data
set_preferences(mixer, show_control=1, clockmode="12h", rec_control=0)


# Get preferences data
def get_preferences(mixer):
    preferences = {}
    preferences["style"] = mixer.execute("/-prefs/style").strip()
    preferences["bright"] = mixer.execute("/-prefs/bright").strip()
    preferences["lcdcont"] = mixer.execute("/-prefs/lcdcont").strip()
    preferences["ledbright"] = mixer.execute("/-prefs/ledbright").strip()
    preferences["lamp"] = mixer.execute("/-prefs/lamp").strip()
    preferences["lampon"] = mixer.execute("/-prefs/lampon").strip()
    preferences["clockrate"] = mixer.execute("/-prefs/clockrate").strip()
    preferences["clocksource"] = mixer.execute("/-prefs/clocksource").strip()
    preferences["confirm_general"] = mixer.execute("/-prefs/confirm_general").strip()
    preferences["confirm_overwrite"] = mixer.execute("/-prefs/confirm_overwrite").strip()
    preferences["confirm_sceneload"] = mixer.execute("/-prefs/confirm_sceneload").strip()
    preferences["viewrtn"] = mixer.execute("/-prefs/viewrtn").strip()
    preferences["selfollowsbank"] = mixer.execute("/-prefs/selfollowsbank").strip()
    preferences["scene_advance"] = mixer.execute("/-prefs/scene_advance").strip()
    preferences["safe_masterlevels"] = mixer.execute("/-prefs/safe_masterlevels").strip()
    preferences["haflags"] = mixer.execute("/-prefs/haflags").strip()
    preferences["autosel"] = mixer.execute("/-prefs/autosel").strip()
    preferences["show_control"] = mixer.execute("/-prefs/show_control").strip()
    preferences["clockmode"] = mixer.execute("/-prefs/clockmode").strip()
    preferences["hardmute"] = mixer.execute("/-prefs/hardmute").strip()
    preferences["dcamute"] = mixer.execute("/-prefs/dcamute").strip()
    preferences["invertmutes"] = mixer.execute("/-prefs/invertmutes").strip()
    preferences["name"] = mixer.execute("/-prefs/name").strip()
    preferences["rec_control"] = mixer.execute("/-prefs/rec_control").strip()
    preferences["fastFaders"] = mixer.execute("/-prefs/fastFaders").strip()
    preferences["ip/dhcp"] = mixer.execute("/-prefs/ip/dhcp").strip()
    preferences["ip/addr/0"] = mixer.execute("/-prefs/ip/addr/0").strip()
    preferences["ip/addr/1"] = mixer.execute("/-prefs/ip/addr/1").strip()
    preferences["ip/addr/2"] = mixer.execute("/-prefs/ip/addr/2").strip()
    preferences["ip/addr/3"] = mixer.execute("/-prefs/ip/addr/3").strip()
    preferences["ip/mask/0"] = mixer.execute("/-prefs/ip/mask/0").strip()
    preferences["ip/mask/1"] = mixer.execute("/-prefs/ip/mask/1").strip()
    preferences["ip/mask/2"] = mixer.execute("/-prefs/ip/mask/2").strip()
    preferences["ip/mask/3"] = mixer.execute("/-prefs/ip/mask/3").strip()
    preferences["ip/gateway/0"] = mixer.execute("/-prefs/ip/gateway/0").strip()
    preferences["ip/gateway/1"] = mixer.execute("/-prefs/ip/gateway/1").strip()
    preferences["ip/gateway/2"] = mixer.execute("/-prefs/ip/gateway/2").strip()
    preferences["ip/gateway/3"] = mixer.execute("/-prefs/ip/gateway/3").strip()
    preferences["remote/enable"] = mixer.execute("/-prefs/remote/enable").strip()
    preferences["remote/protocol"] = mixer.execute("/-prefs/remote/protocol").strip()
    preferences["remote/port"] = mixer.execute("/-prefs/remote/port").strip()
    preferences["remote/ioenable"] = mixer.execute("/-prefs/remote/ioenable").strip()
    return preferences

# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None):
    if style:
        mixer.execute(f"/-prefs/style {style}")
    if bright:
        mixer.execute(f"/-prefs/bright {bright}")
    if lcdcont:
        mixer.execute(f"/-prefs/lcdcont {lcdcont}")
    if ledbright:
        mixer.execute(f"/-prefs/ledbright {ledbright}")
    if lamp:
        mixer.execute(f"/-prefs/lamp {lamp}")
    if lampon is not None:
        mixer.execute(f"/-prefs/lampon {lampon}")
    if clockrate is not None:
        mixer.execute(f"/-prefs/clockrate {clockrate}")
    if clocksource is not None:
        mixer.execute(f"/-prefs/clocksource {clocksource}")
    if confirm_general is not None:
        mixer.execute(f"/-prefs/confirm_general {confirm_general}")
    if confirm_overwrite is not None:
        mixer.execute(f"/-prefs/confirm_overwrite {confirm_overwrite}")
    if confirm_sceneload is not None:
        mixer.execute(f"/-prefs/confirm_sceneload {confirm_sceneload}")
    if viewrtn is not None:
        mixer.execute(f"/-prefs/viewrtn {viewrtn}")
    if selfollowsbank is not None:
        mixer.execute(f"/-prefs/selfollowsbank {selfollowsbank}")
    if scene_advance is not None:
        mixer.execute(f"/-prefs/scene_advance {scene_advance}")
    if safe_masterlevels is not None:
        mixer.execute(f"/-prefs/safe_masterlevels {safe_masterlevels}")
    if haflags is not None:
        mixer.execute(f"/-prefs/haflags {haflags}")
    if autosel is not None:
        mixer.execute(f"/-prefs/autosel {autosel}")
    if show_control is not None:
        mixer.execute(f"/-prefs/show_control {show_control}")
    if clockmode is not None:
        mixer.execute(f"/-prefs/clockmode {clockmode}")
    if hardmute is not None:
        mixer.execute(f"/-prefs/hardmute {hardmute}")
    if dcamute is not None:
        mixer.execute(f"/-prefs/dcamute {dcamute}")
    if invertmutes is not None:
        mixer.execute(f"/-prefs/invertmutes {invertmutes}")
    if name:
        mixer.execute(f"/-prefs/name {name}")
    if rec_control is not None:
        mixer.execute(f"/-prefs/rec_control {rec_control}")
    if fastFaders is not None:
        mixer.execute(f"/-prefs/fastFaders {fastFaders}")
    if ip_dhcp is not None:
        mixer.execute(f"/-prefs/ip/dhcp {ip_dhcp}")
    if ip_addr:
        for i, value in enumerate(ip_addr):
            mixer.execute(f"/-prefs/ip/addr/{i} {value}")
    if ip_mask:
        for i, value in enumerate(ip_mask):
            mixer.execute(f"/-prefs/ip/mask/{i} {value}")
    if ip_gateway:
        for i, value in enumerate(ip_gateway):
            mixer.execute(f"/-prefs/ip/gateway/{i} {value}")
    if remote_enable is not None:
        mixer.execute(f"/-prefs/remote/enable {remote_enable}")
    if remote_protocol is not None:
        mixer.execute(f"/-prefs/remote/protocol {remote_protocol}")
    if remote_port is not None:
        mixer.execute(f"/-prefs/remote/port {remote_port}")
    if remote_ioenable is not None:
        mixer.execute(f"/-prefs/remote/ioenable {remote_ioenable}")


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    return preferences


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None,
                    card_ADATsync=None, card_MADImode=None, card_MADIin=None, card_MADIout=None, card_MADIsrc=None,
                    card_URECsdsel=None, card_URECtracks=None, card_URECplayb=None, card_URECrout=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    # Additional card preferences
    if card_ADATsync is not None:
        mixer.execute(f"/-prefs/card/ADATsync {card_ADATsync}")
    if card_MADImode is not None:
        mixer.execute(f"/-prefs/card/MADImode {card_MADImode}")
    if card_MADIin is not None:
        mixer.execute(f"/-prefs/card/MADIin {card_MADIin}")
    if card_MADIout is not None:
        mixer.execute(f"/-prefs/card/MADIout {card_MADIout}")
    if card_MADIsrc is not None:
        mixer.execute(f"/-prefs/card/MADIsrc {card_MADIsrc}")
    if card_URECsdsel is not None:
        mixer.execute(f"/-prefs/card/URECsdsel {card_URECsdsel}")
    if card_URECtracks is not None:
        mixer.execute(f"/-prefs/card/URECtracks {card_URECtracks}")
    if card_URECplayb is not None:
        mixer.execute(f"/-prefs/card/URECplayb {card_URECplayb}")
    if card_URECrout is not None:
        mixer.execute(f"/-prefs/card/URECrout {card_URECrout}")

    return preferences


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None,
                    card_ADATsync=None, card_MADImode=None, card_MADIin=None, card_MADIout=None, card_MADIsrc=None,
                    card_URECsdsel=None, card_URECtracks=None, card_URECplayb=None, card_URECrout=None,
                    rta_visibility=None, rta_gain=None, rta_autogain=None, rta_source=None, rta_pos=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    # Additional card preferences
    if card_ADATsync is not None:
        mixer.execute(f"/-prefs/card/ADATsync {card_ADATsync}")
    if card_MADImode is not None:
        mixer.execute(f"/-prefs/card/MADImode {card_MADImode}")
    if card_MADIin is not None:
        mixer.execute(f"/-prefs/card/MADIin {card_MADIin}")
    if card_MADIout is not None:
        mixer.execute(f"/-prefs/card/MADIout {card_MADIout}")
    if card_MADIsrc is not None:
        mixer.execute(f"/-prefs/card/MADIsrc {card_MADIsrc}")
    if card_URECsdsel is not None:
        mixer.execute(f"/-prefs/card/URECsdsel {card_URECsdsel}")
    if card_URECtracks is not None:
        mixer.execute(f"/-prefs/card/URECtracks {card_URECtracks}")
    if card_URECplayb is not None:
        mixer.execute(f"/-prefs/card/URECplayb {card_URECplayb}")
    if card_URECrout is not None:
        mixer.execute(f"/-prefs/card/URECrout {card_URECrout}")

    # RTA preferences
    if rta_visibility is not None:
        mixer.execute(f"/-prefs/rta/visibility {rta_visibility}")
    if rta_gain is not None:
        mixer.execute(f"/-prefs/rta/gain {rta_gain[0]} {rta_gain[1]} {rta_gain[2]}")
    if rta_autogain is not None:
        mixer.execute(f"/-prefs/rta/autogain {rta_autogain}")
    if rta_source is not None:
        mixer.execute(f"/-prefs/rta/source {rta_source}")
    if rta_pos is not None:
        mixer.execute(f"/-prefs/rta/pos {rta_pos}")

    return preferences


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None,
                    card_ADATsync=None, card_MADImode=None, card_MADIin=None, card_MADIout=None, card_MADIsrc=None,
                    card_URECsdsel=None, card_URECtracks=None, card_URECplayb=None, card_URECrout=None,
                    rta_visibility=None, rta_gain=None, rta_autogain=None, rta_source=None, rta_pos=None, rta_mode=None,
                    rta_options=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    # Additional card preferences
    if card_ADATsync is not None:
        mixer.execute(f"/-prefs/card/ADATsync {card_ADATsync}")
    if card_MADImode is not None:
        mixer.execute(f"/-prefs/card/MADImode {card_MADImode}")
    if card_MADIin is not None:
        mixer.execute(f"/-prefs/card/MADIin {card_MADIin}")
    if card_MADIout is not None:
        mixer.execute(f"/-prefs/card/MADIout {card_MADIout}")
    if card_MADIsrc is not None:
        mixer.execute(f"/-prefs/card/MADIsrc {card_MADIsrc}")
    if card_URECsdsel is not None:
        mixer.execute(f"/-prefs/card/URECsdsel {card_URECsdsel}")
    if card_URECtracks is not None:
        mixer.execute(f"/-prefs/card/URECtracks {card_URECtracks}")
    if card_URECplayb is not None:
        mixer.execute(f"/-prefs/card/URECplayb {card_URECplayb}")
    if card_URECrout is not None:
        mixer.execute(f"/-prefs/card/URECrout {card_URECrout}")

    # RTA preferences
    if rta_visibility is not None:
        mixer.execute(f"/-prefs/rta/visibility {rta_visibility}")
    if rta_gain is not None:
        mixer.execute(f"/-prefs/rta/gain {rta_gain[0]} {rta_gain[1]} {rta_gain[2]}")
    if rta_autogain is not None:
        mixer.execute(f"/-prefs/rta/autogain {rta_autogain}")
    if rta_source is not None:
        mixer.execute(f"/-prefs/rta/source {rta_source}")
    if rta_pos is not None:
        mixer.execute(f"/-prefs/rta/pos {rta_pos}")
    if rta_mode is not None:
        mixer.execute(f"/-prefs/rta/mode {rta_mode}")
    if rta_options is not None:
        mixer.execute(f"/-prefs/rta/options {rta_options}")

    return preferences


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None,
                    card_ADATsync=None, card_MADImode=None, card_MADIin=None, card_MADIout=None, card_MADIsrc=None,
                    card_URECsdsel=None, card_URECtracks=None, card_URECplayb=None, card_URECrout=None,
                    rta_visibility=None, rta_gain=None, rta_autogain=None, rta_source=None, rta_pos=None, rta_mode=None,
                    rta_options=None, rta_det=None, rta_decay=None, rta_peakhold=None,
                    iQ_iQmodel=None, iQ_iQeqset=None, iQ_iQsound=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    # Additional card preferences
    if card_ADATsync is not None:
        mixer.execute(f"/-prefs/card/ADATsync {card_ADATsync}")
    if card_MADImode is not None:
        mixer.execute(f"/-prefs/card/MADImode {card_MADImode}")
    if card_MADIin is not None:
        mixer.execute(f"/-prefs/card/MADIin {card_MADIin}")
    if card_MADIout is not None:
        mixer.execute(f"/-prefs/card/MADIout {card_MADIout}")
    if card_MADIsrc is not None:
        mixer.execute(f"/-prefs/card/MADIsrc {card_MADIsrc}")
    if card_URECsdsel is not None:
        mixer.execute(f"/-prefs/card/URECsdsel {card_URECsdsel}")
    if card_URECtracks is not None:
        mixer.execute(f"/-prefs/card/URECtracks {card_URECtracks}")
    if card_URECplayb is not None:
        mixer.execute(f"/-prefs/card/URECplayb {card_URECplayb}")
    if card_URECrout is not None:
        mixer.execute(f"/-prefs/card/URECrout {card_URECrout}")

    # RTA preferences
    if rta_visibility is not None:
        mixer.execute(f"/-prefs/rta/visibility {rta_visibility}")
    if rta_gain is not None:
        mixer.execute(f"/-prefs/rta/gain {rta_gain[0]} {rta_gain[1]} {rta_gain[2]}")
    if rta_autogain is not None:
        mixer.execute(f"/-prefs/rta/autogain {rta_autogain}")
    if rta_source is not None:
        mixer.execute(f"/-prefs/rta/source {rta_source}")
    if rta_pos is not None:
        mixer.execute(f"/-prefs/rta/pos {rta_pos}")
    if rta_mode is not None:
        mixer.execute(f"/-prefs/rta/mode {rta_mode}")
    if rta_options is not None:
        mixer.execute(f"/-prefs/rta/options {rta_options}")
    if rta_det is not None:
        mixer.execute(f"/-prefs/rta/det {rta_det}")
    if rta_decay is not None:
        mixer.execute(f"/-prefs/rta/decay {rta_decay[0]} {rta_decay[1]} {rta_decay[2]}")
    if rta_peakhold is not None:
        mixer.execute(f"/-prefs/rta/peakhold {rta_peakhold}")

    # Turbosound iQ speakers preferences
    for i in range(1, 17):
        if iQ_iQmodel is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQmodel {iQ_iQmodel[i-1]}")
        if iQ_iQeqset is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQeqset {iQ_iQeqset[i-1]}")
        if iQ_iQsound is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQsound {iQ_iQsound[i-1]}")

    return preferences


# Set preferences data
def set_preferences(mixer, style=None, bright=None, lcdcont=None, ledbright=None, lamp=None, lampon=None, clockrate=None, clocksource=None,
                    confirm_general=None, confirm_overwrite=None, confirm_sceneload=None, viewrtn=None, selfollowsbank=None,
                    scene_advance=None, safe_masterlevels=None, haflags=None, autosel=None, show_control=None,
                    clockmode=None, hardmute=None, dcamute=None, invertmutes=None, name=None, rec_control=None, fastFaders=None,
                    ip_dhcp=None, ip_addr=None, ip_mask=None, ip_gateway=None,
                    remote_enable=None, remote_protocol=None, remote_port=None, remote_ioenable=None,
                    card_UFifc=None, card_UFmode=None, card_USBmode=None, card_ADATwc=None,
                    card_ADATsync=None, card_MADImode=None, card_MADIin=None, card_MADIout=None, card_MADIsrc=None,
                    card_URECsdsel=None, card_URECtracks=None, card_URECplayb=None, card_URECrout=None,
                    rta_visibility=None, rta_gain=None, rta_autogain=None, rta_source=None, rta_pos=None, rta_mode=None,
                    rta_options=None, rta_det=None, rta_decay=None, rta_peakhold=None,
                    iQ_iQmodel=None, iQ_iQeqset=None, iQ_iQsound=None,
                    key_layout=None, key_history=None):
    preferences = {}

    if style is not None:
        mixer.execute(f"/-prefs/style {style}")
    if bright is not None:
        mixer.execute(f"/-prefs/bright {bright[0]} {bright[1]} {bright[2]}")
    # ... (set other preferences data)

    if card_UFifc is not None:
        mixer.execute(f"/-prefs/card/UFifc {card_UFifc}")
    if card_UFmode is not None:
        mixer.execute(f"/-prefs/card/UFmode {card_UFmode}")
    if card_USBmode is not None:
        mixer.execute(f"/-prefs/card/USBmode {card_USBmode}")
    if card_ADATwc is not None:
        mixer.execute(f"/-prefs/card/ADATwc {card_ADATwc}")

    # Additional card preferences
    if card_ADATsync is not None:
        mixer.execute(f"/-prefs/card/ADATsync {card_ADATsync}")
    if card_MADImode is not None:
        mixer.execute(f"/-prefs/card/MADImode {card_MADImode}")
    if card_MADIin is not None:
        mixer.execute(f"/-prefs/card/MADIin {card_MADIin}")
    if card_MADIout is not None:
        mixer.execute(f"/-prefs/card/MADIout {card_MADIout}")
    if card_MADIsrc is not None:
        mixer.execute(f"/-prefs/card/MADIsrc {card_MADIsrc}")
    if card_URECsdsel is not None:
        mixer.execute(f"/-prefs/card/URECsdsel {card_URECsdsel}")
    if card_URECtracks is not None:
        mixer.execute(f"/-prefs/card/URECtracks {card_URECtracks}")
    if card_URECplayb is not None:
        mixer.execute(f"/-prefs/card/URECplayb {card_URECplayb}")
    if card_URECrout is not None:
        mixer.execute(f"/-prefs/card/URECrout {card_URECrout}")

    # RTA preferences
    if rta_visibility is not None:
        mixer.execute(f"/-prefs/rta/visibility {rta_visibility}")
    if rta_gain is not None:
        mixer.execute(f"/-prefs/rta/gain {rta_gain[0]} {rta_gain[1]} {rta_gain[2]}")
    if rta_autogain is not None:
        mixer.execute(f"/-prefs/rta/autogain {rta_autogain}")
    if rta_source is not None:
        mixer.execute(f"/-prefs/rta/source {rta_source}")
    if rta_pos is not None:
        mixer.execute(f"/-prefs/rta/pos {rta_pos}")
    if rta_mode is not None:
        mixer.execute(f"/-prefs/rta/mode {rta_mode}")
    if rta_options is not None:
        mixer.execute(f"/-prefs/rta/options {rta_options}")
    if rta_det is not None:
        mixer.execute(f"/-prefs/rta/det {rta_det}")
    if rta_decay is not None:
        mixer.execute(f"/-prefs/rta/decay {rta_decay[0]} {rta_decay[1]} {rta_decay[2]}")
    if rta_peakhold is not None:
        mixer.execute(f"/-prefs/rta/peakhold {rta_peakhold}")

    # Turbosound iQ speakers preferences
    for i in range(1, 17):
        if iQ_iQmodel is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQmodel {iQ_iQmodel[i-1]}")
        if iQ_iQeqset is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQeqset {iQ_iQeqset[i-1]}")
        if iQ_iQsound is not None:
            mixer.execute(f"/-prefs/iQ/{i:02d}/iQsound {iQ_iQsound[i-1]}")

    # Keyboard preferences
    if key_layout is not None:
        mixer.execute(f"/-prefs/key/layout {key_layout}")
    if key_history is not None:
        for i, entry in enumerate(key_history):
            mixer.execute(f"/-prefs/key/{i:02d} {entry}")

    return preferences


# Get USB stick information
def get_usb_info(mixer, path=None, title=None, dirpos=None, maxpos=None):
    usb_info = {}

    if path is not None:
        response = mixer.query(f"/-usb/path {path}")
        usb_info['path'] = response.strip()
    if title is not None:
        response = mixer.query(f"/-usb/title {title}")
        usb_info['title'] = response.strip()
    if dirpos is not None:
        response = mixer.query(f"/-usb/dir/dirpos {dirpos}")
        usb_info['dirpos'] = int(response)
    if maxpos is not None:
        response = mixer.query(f"/-usb/dir/maxpos")
        usb_info['maxpos'] = int(response)

    # Get file names in the current directory
    for i in range(1, 1000):
        try:
            response_type = mixer.query(f"/-usb/dir/{i:03d}/type")
            response_name = mixer.query(f"/-usb/dir/{i:03d}/name")
            usb_info[f'{i:03d}'] = {
                'type': response_type.strip(),
                'name': response_name.strip()
            }
        except:
            break

    return usb_info


# Get status data
def get_status_data(mixer, selidx=None, chfaderbank=None, grpfaderbank=None, sendsonfader=None):
    status_data = {}

    if selidx is not None:
        response = mixer.query(f"/-stat/selidx {selidx}")
        status_data['selidx'] = response.strip()
    if chfaderbank is not None:
        response = mixer.query(f"/-stat/chfaderbank {chfaderbank}")
        status_data['chfaderbank'] = int(response)
    if grpfaderbank is not None:
        response = mixer.query(f"/-stat/grpfaderbank {grpfaderbank}")
        status_data['grpfaderbank'] = int(response)
    if sendsonfader is not None:
        response = mixer.query(f"/-stat/sendsonfader {sendsonfader}")
        status_data['sendsonfader'] = response.strip()

    return status_data


# Get additional status data
def get_additional_status_data(mixer, bussendbank=None, eqband=None, solo=None, keysolo=None, userbank=None):
    status_data = {}

    if bussendbank is not None:
        response = mixer.query(f"/-stat/bussendbank {bussendbank}")
        status_data['bussendbank'] = int(response)
    if eqband is not None:
        response = mixer.query(f"/-stat/eqband {eqband}")
        status_data['eqband'] = int(response)
    if solo is not None:
        response = mixer.query(f"/-stat/solo {solo}")
        status_data['solo'] = response.strip()
    if keysolo is not None:
        response = mixer.query(f"/-stat/keysolo {keysolo}")
        status_data['keysolo'] = response.strip()
    if userbank is not None:
        response = mixer.query(f"/-stat/userbank {userbank}")
        status_data['userbank'] = int(response)

    return status_data


# Get remaining status data
def get_remaining_status_data(mixer, autosave=None, lock=None, usbmounted=None, remote=None, rtamodeeq=None, rtamodegeq=None, rtaeqpre=None, rtageqpost=None):
    status_data = {}

    if autosave is not None:
        response = mixer.query(f"/-stat/autosave {autosave}")
        status_data['autosave'] = response.strip()
    if lock is not None:
        response = mixer.query(f"/-stat/lock {lock}")
        status_data['lock'] = int(response)
    if usbmounted is not None:
        response = mixer.query(f"/-stat/usbmounted {usbmounted}")
        status_data['usbmounted'] = response.strip()
    if remote is not None:
        response = mixer.query(f"/-stat/remote {remote}")
        status_data['remote'] = response.strip()
    if rtamodeeq is not None:
        response = mixer.query(f"/-stat/rtamodeeq {rtamodeeq}")
        status_data['rtamodeeq'] = response.strip()
    if rtamodegeq is not None:
        response = mixer.query(f"/-stat/rtamodegeq {rtamodegeq}")
        status_data['rtamodegeq'] = response.strip()
    if rtaeqpre is not None:
        response = mixer.query(f"/-stat/rtaeqpre {rtaeqpre}")
        status_data['rtaeqpre'] = response.strip()
    if rtageqpost is not None:
        response = mixer.query(f"/-stat/rtageqpost {rtageqpost}")
        status_data['rtageqpost'] = response.strip()

    return status_data


# Get RTA source data
def get_rta_source(mixer):
    response = mixer.query("/-stat/rtasource")
    rta_source_data = {}

    channels = [
        f"Channel {i+1:02}" for i in range(32)
    ]
    aux = [
        f"Aux {i+1:02}" for i in range(8)
    ]
    fxrtn = [
        f"Fxrtn {i+1}L" for i in range(4)
    ]
    buses = [
        f"Bus {i+1:02}" for i in range(16)
    ]
    matrix = [
        f"Matrix {i+1:02}" for i in range(6)
    ]
    others = [
        "L/R", "Mono", "Monitor"
    ]

    # Combine the lists to get the complete RTA source mapping
    rta_source_mapping = channels + aux + fxrtn + buses + matrix + others

    for index, source in enumerate(rta_source_mapping):
        rta_source_data[index] = source

    return rta_source_data


# Get status data
def get_status_data(mixer):
    response = mixer.query("/-stat/xcardtype")
    xcardtype = int(response)

    response = mixer.query("/-stat/xcardsync")
    xcardsync = int(response)

    response = mixer.query("/-stat/geqonfdr")
    geqonfdr = int(response)

    response = mixer.query("/-stat/geqpos")
    geqpos = int(response)

    response = mixer.query("/-stat/screen/screen")
    screen = int(response)

    response = mixer.query("/-stat/screen/mutegrp")
    mutegrp = int(response)

    response = mixer.query("/-stat/screen/utils")
    utils = int(response)

    response = mixer.query("/-stat/screen/CHAN/page")
    chan_page = int(response)

    status_data = {
        "xcardtype": xcardtype,
        "xcardsync": xcardsync,
        "geqonfdr": geqonfdr,
        "geqpos": geqpos,
        "screen": screen,
        "mutegrp": mutegrp,
        "utils": utils,
        "chan_page": chan_page
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/selidx")
    selected_index = int(response)

    response = mixer.query("/-stat/chfaderbank")
    channel_fader_bank = int(response)

    response = mixer.query("/-stat/grpfaderbank")
    group_fader_bank = int(response)

    response = mixer.query("/-stat/sendsonfader")
    sends_on_fader = int(response)

    response = mixer.query("/-stat/bussendbank")
    bus_sends_bank = int(response)

    response = mixer.query("/-stat/eqband")
    eq_band = int(response)

    response = mixer.query("/-stat/solo")
    solo_state = int(response)

    response = mixer.query("/-stat/keysolo")
    key_solo_state = int(response)

    response = mixer.query("/-stat/userbank")
    user_bank = int(response)

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/autosave")
    autosave_state = int(response)

    response = mixer.query("/-stat/lock48")
    lock_status = int(response)

    response = mixer.query("/-stat/usbmounted")
    usb_mount_status = int(response)

    response = mixer.query("/-stat/remote")
    remote_mode = int(response)

    # ... (Add other additional status data retrieval here)

    # Store all the status data in a dictionary
    status_data = {
        "selected_index": selected_index,
        "channel_fader_bank": channel_fader_bank,
        "group_fader_bank": group_fader_bank,
        "sends_on_fader": sends_on_fader,
        "bus_sends_bank": bus_sends_bank,
        "eq_band": eq_band,
        "solo_state": solo_state,
        "key_solo_state": key_solo_state,
        "user_bank": user_bank,
        "autosave_state": autosave_state,
        "lock_status": lock_status,
        "usb_mount_status": usb_mount_status,
        "remote_mode": remote_mode,
        # ... (Add other additional status data to the dictionary)
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/selidx")
    selected_index = int(response)

    response = mixer.query("/-stat/chfaderbank")
    channel_fader_bank = int(response)

    response = mixer.query("/-stat/grpfaderbank")
    group_fader_bank = int(response)

    response = mixer.query("/-stat/sendsonfader")
    sends_on_fader = int(response)

    response = mixer.query("/-stat/bussendbank")
    bus_sends_bank = int(response)

    response = mixer.query("/-stat/eqband")
    eq_band = int(response)

    response = mixer.query("/-stat/solo")
    solo_state = int(response)

    response = mixer.query("/-stat/keysolo")
    key_solo_state = int(response)

    response = mixer.query("/-stat/userbank")
    user_bank = int(response)

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/autosave")
    autosave_state = int(response)

    response = mixer.query("/-stat/lock48")
    lock_status = int(response)

    response = mixer.query("/-stat/usbmounted")
    usb_mount_status = int(response)

    response = mixer.query("/-stat/remote")
    remote_mode = int(response)

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/screen/ASSIGN/page")
    assign_screen_page = int(response)

    response = mixer.query("/-stat/aes50/state")
    aes50_state = int(response)

    response = mixer.query("/-stat/aes50/A")
    aes50_detected_A = response.strip()

    response = mixer.query("/-stat/aes50/B")
    aes50_detected_B = response.strip()

    # Store all the status data in a dictionary
    status_data = {
        "selected_index": selected_index,
        "channel_fader_bank": channel_fader_bank,
        "group_fader_bank": group_fader_bank,
        "sends_on_fader": sends_on_fader,
        "bus_sends_bank": bus_sends_bank,
        "eq_band": eq_band,
        "solo_state": solo_state,
        "key_solo_state": key_solo_state,
        "user_bank": user_bank,
        "autosave_state": autosave_state,
        "lock_status": lock_status,
        "usb_mount_status": usb_mount_status,
        "remote_mode": remote_mode,
        "assign_screen_page": assign_screen_page,
        "aes50_state": aes50_state,
        "aes50_detected_A": aes50_detected_A,
        "aes50_detected_B": aes50_detected_B,
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/selidx")
    selected_index = int(response)

    response = mixer.query("/-stat/chfaderbank")
    channel_fader_bank = int(response)

    response = mixer.query("/-stat/grpfaderbank")
    group_fader_bank = int(response)

    response = mixer.query("/-stat/sendsonfader")
    sends_on_fader = int(response)

    response = mixer.query("/-stat/bussendbank")
    bus_sends_bank = int(response)

    response = mixer.query("/-stat/eqband")
    eq_band = int(response)

    response = mixer.query("/-stat/solo")
    solo_state = int(response)

    response = mixer.query("/-stat/keysolo")
    key_solo_state = int(response)

    response = mixer.query("/-stat/userbank")
    user_bank = int(response)

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/autosave")
    autosave_state = int(response)

    response = mixer.query("/-stat/lock48")
    lock_status = int(response)

    response = mixer.query("/-stat/usbmounted")
    usb_mount_status = int(response)

    response = mixer.query("/-stat/remote")
    remote_mode = int(response)

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/screen/ASSIGN/page")
    assign_screen_page = int(response)

    response = mixer.query("/-stat/aes50/state")
    aes50_state = int(response)

    response = mixer.query("/-stat/aes50/A")
    aes50_detected_A = response.strip()

    response = mixer.query("/-stat/aes50/B")
    aes50_detected_B = response.strip()

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/solosw/01-32")
    solo_switches = [int(sw) for sw in response.strip().split(",")]

    response = mixer.query("/-stat/talk/A")
    talkback_A_state = int(response)

    response = mixer.query("/-stat/talk/B")
    talkback_B_state = int(response)

    response = mixer.query("/-stat/osc/on")
    oscillator_state = int(response)

    response = mixer.query("/-stat/tape/state")
    tape_state = int(response)

    # Store all the status data in a dictionary
    status_data = {
        "selected_index": selected_index,
        "channel_fader_bank": channel_fader_bank,
        "group_fader_bank": group_fader_bank,
        "sends_on_fader": sends_on_fader,
        "bus_sends_bank": bus_sends_bank,
        "eq_band": eq_band,
        "solo_state": solo_state,
        "key_solo_state": key_solo_state,
        "user_bank": user_bank,
        "autosave_state": autosave_state,
        "lock_status": lock_status,
        "usb_mount_status": usb_mount_status,
        "remote_mode": remote_mode,
        "assign_screen_page": assign_screen_page,
        "aes50_state": aes50_state,
        "aes50_detected_A": aes50_detected_A,
        "aes50_detected_B": aes50_detected_B,
        "solo_switches": solo_switches,
        "talkback_A_state": talkback_A_state,
        "talkback_B_state": talkback_B_state,
        "oscillator_state": oscillator_state,
        "tape_state": tape_state,
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/meter/02/mode")
    meter_mode = int(response)

    response = mixer.query("/-stat/meter/02/cnt")
    meter_count = int(response)

    response = mixer.query("/-stat/meter/02/0PPN")
    meter_ppn = int(response)

    response = mixer.query("/-stat/rtasource")
    rta_source = int(response)

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/rta/options")
    rta_options = int(response)

    response = mixer.query("/-stat/rta/det")
    rta_detector = int(response)

    response = mixer.query("/-stat/rta/decay")
    rta_decay = float(response)

    response = mixer.query("/-stat/rta/peakhold")
    rta_peak_hold = int(response)

    response = mixer.query("/-stat/xcardsync")
    xcard_sync = int(response)

    response = mixer.query("/-stat/geqonfdr")
    geq_on_fader = int(response)

    response = mixer.query("/-stat/geqpos")
    geq_position = int(response)

    response = mixer.query("/-stat/solo")
    solo_state = int(response)

    response = mixer.query("/-stat/keysolo")
    key_solo_state = int(response)

    response = mixer.query("/-stat/userbank")
    user_bank = int(response)

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/screen/ASSIGN/page")
    assign_screen_page = int(response)

    response = mixer.query("/-stat/aes50/state")
    aes50_state = int(response)

    response = mixer.query("/-stat/aes50/A")
    aes50_detected_A = response.strip()

    response = mixer.query("/-stat/aes50/B")
    aes50_detected_B = response.strip()

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/solosw/01-32")
    solo_switches = [int(sw) for sw in response.strip().split(",")]

    response = mixer.query("/-stat/talk/A")
    talkback_A_state = int(response)

    response = mixer.query("/-stat/talk/B")
    talkback_B_state = int(response)

    response = mixer.query("/-stat/osc/on")
    oscillator_state = int(response)

    response = mixer.query("/-stat/tape/state")
    tape_state = int(response)

    response = mixer.query("/-stat/tape/file")
    tape_file = response.strip()

    response = mixer.query("/-stat/tape/etime")
    elapsed_time = int(response)

    response = mixer.query("/-stat/tape/rtime")
    remaining_time = int(response)

    # User Parameters
    user_parameters = {}
    user_params = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
                   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                   14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    for param_id in user_params:
        response = mixer.query(f"/-stat/userpar/{param_id}/value")
        value = int(response)
        user_parameters[f"{param_id:02d}"] = value

    # Store all the status data in a dictionary
    status_data = {
        # Previous status data (unchanged)
        "meter_mode": meter_mode,
        "meter_count": meter_count,
        "meter_ppn": meter_ppn,
        "rta_source": rta_source,

        # Additional status data (from previous updates)
        "rta_options": rta_options,
        "rta_detector": rta_detector,
        "rta_decay": rta_decay,
        "rta_peak_hold": rta_peak_hold,
        "xcard_sync": xcard_sync,
        "geq_on_fader": geq_on_fader,
        "geq_position": geq_position,
        "solo_state": solo_state,
        "key_solo_state": key_solo_state,
        "user_bank": user_bank,

        # Additional status data (latest updates)
        "assign_screen_page": assign_screen_page,
        "aes50_state": aes50_state,
        "aes50_detected_A": aes50_detected_A,
        "aes50_detected_B": aes50_detected_B,
        "solo_switches": solo_switches,
        "talkback_A_state": talkback_A_state,
        "talkback_B_state": talkback_B_state,
        "oscillator_state": oscillator_state,
        "tape_state": tape_state,
        "tape_file": tape_file,
        "elapsed_time": elapsed_time,
        "remaining_time": remaining_time,
        "user_parameters": user_parameters,
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/selidx")
    selected_index = int(response)

    response = mixer.query("/-stat/chfader")
    channel_fader = float(response)

    response = mixer.query("/-stat/solosw/01")
    solo_channel_01 = bool(int(response))

    response = mixer.query("/-stat/solosw/02")
    solo_channel_02 = bool(int(response))

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/solosw/03")
    solo_channel_03 = bool(int(response))

    response = mixer.query("/-stat/solosw/04")
    solo_channel_04 = bool(int(response))

    response = mixer.query("/-stat/solosw/05")
    solo_channel_05 = bool(int(response))

    response = mixer.query("/-stat/solosw/06")
    solo_channel_06 = bool(int(response))

    response = mixer.query("/-stat/solosw/07")
    solo_channel_07 = bool(int(response))

    response = mixer.query("/-stat/solosw/08")
    solo_channel_08 = bool(int(response))

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/urec/state")
    xlive_state = int(response)

    # X-Live! extension card state
    xlive_states = {
        0: "STOP",
        1: "PPAUSE",
        2: "PLAY",
        3: "REC",
    }

    response = mixer.query("/-stat/urec/rtime")
    xlive_recording_time = int(response)

    response = mixer.query("/-stat/urec/etime")
    xlive_elapsed_time = int(response)

    response = mixer.query("/-stat/urec/state")
    xlive_state = xlive_states[int(response)]

    response = mixer.query("/-urec/sd1info")
    xlive_sd1_info = response.strip()

    response = mixer.query("/-urec/session/002/name")
    xlive_session_name = response.strip()

    response = mixer.query("/-urec/sessionmax")
    xlive_session_max = int(response)

    response = mixer.query("/-urec/sessionlen")
    xlive_session_length = int(response)

    response = mixer.query("/-urec/sessionpos")
    xlive_session_position = int(response)

    # Store all the status data in a dictionary
    status_data = {
        "selected_index": selected_index,
        "channel_fader": channel_fader,
        "solo_channel_01": solo_channel_01,
        "solo_channel_02": solo_channel_02,
        "solo_channel_03": solo_channel_03,
        "solo_channel_04": solo_channel_04,
        "solo_channel_05": solo_channel_05,
        "solo_channel_06": solo_channel_06,
        "solo_channel_07": solo_channel_07,
        "solo_channel_08": solo_channel_08,
        "xlive_state": xlive_state,
        "xlive_recording_time": xlive_recording_time,
        "xlive_elapsed_time": xlive_elapsed_time,
        "xlive_sd1_info": xlive_sd1_info,
        "xlive_session_name": xlive_session_name,
        "xlive_session_max": xlive_session_max,
        "xlive_session_length": xlive_session_length,
        "xlive_session_position": xlive_session_position,
    }

    return status_data


def get_status_data(mixer):
    # Previous status data retrieval code
    response = mixer.query("/-stat/selidx")
    selected_index = int(response)

    response = mixer.query("/-stat/chfader")
    channel_fader = float(response)

    response = mixer.query("/-stat/solosw/01")
    solo_channel_01 = bool(int(response))

    response = mixer.query("/-stat/solosw/02")
    solo_channel_02 = bool(int(response))

    # Additional status data retrieval (from previous updates)
    response = mixer.query("/-stat/solosw/03")
    solo_channel_03 = bool(int(response))

    response = mixer.query("/-stat/solosw/04")
    solo_channel_04 = bool(int(response))

    response = mixer.query("/-stat/solosw/05")
    solo_channel_05 = bool(int(response))

    response = mixer.query("/-stat/solosw/06")
    solo_channel_06 = bool(int(response))

    response = mixer.query("/-stat/solosw/07")
    solo_channel_07 = bool(int(response))

    response = mixer.query("/-stat/solosw/08")
    solo_channel_08 = bool(int(response))

    # Additional status data retrieval (latest updates)
    response = mixer.query("/-stat/urec/state")
    xlive_state = int(response)

    # X-Live! extension card state
    xlive_states = {
        0: "STOP",
        1: "PPAUSE",
        2: "PLAY",
        3: "REC",
    }

    response = mixer.query("/-stat/urec/rtime")
    xlive_recording_time = int(response)

    response = mixer.query("/-stat/urec/etime")
    xlive_elapsed_time = int(response)

    # Convert elapsed and remaining time from milliseconds to seconds
    xlive_elapsed_time_sec = xlive_elapsed_time // 1000
    xlive_recording_time_sec = xlive_recording_time // 1000

    response = mixer.query("/-stat/urec/state")
    xlive_state = xlive_states[int(response)]

    response = mixer.query("/-urec/sd1info")
    xlive_sd1_info = response.strip()

    response = mixer.query("/-urec/session/002/name")
    xlive_session_name = response.strip()

    response = mixer.query("/-urec/sessionmax")
    xlive_session_max = int(response)

    response = mixer.query("/-urec/sessionlen")
    xlive_session_length = int(response)

    response = mixer.query("/-urec/sessionpos")
    xlive_session_position = int(response)

    # Store all the status data in a dictionary
    status_data = {
        "selected_index": selected_index,
        "channel_fader": channel_fader,
        "solo_channel_01": solo_channel_01,
        "solo_channel_02": solo_channel_02,
        "solo_channel_03": solo_channel_03,
        "solo_channel_04": solo_channel_04,
        "solo_channel_05": solo_channel_05,
        "solo_channel_06": solo_channel_06,
        "solo_channel_07": solo_channel_07,
        "solo_channel_08": solo_channel_08,
        "xlive_state": xlive_state,
        "xlive_recording_time_sec": xlive_recording_time_sec,
        "xlive_elapsed_time_sec": xlive_elapsed_time_sec,
        "xlive_sd1_info": xlive_sd1_info,
        "xlive_session_name": xlive_session_name,
        "xlive_session_max": xlive_session_max,
        "xlive_session_length": xlive_session_length,
        "xlive_session_position": xlive_session_position,
    }

    return status_data


def send_action_command(mixer, command, value=None):
    if value is not None:
        response = mixer.send("/-action/" + command, value)
    else:
        response = mixer.send("/-action/" + command)
    return response

# Set clock value
#send_action_command(mixer, "setclock", "12:00:00")

# Initialize X32 Console
#send_action_command(mixer, "initall", 1)

# Initialize X32 Libraries
#send_action_command(mixer, "initlib", 1)

# Save X32/M32 state
#send_action_command(mixer, "savestate", 1)

# Create checkpoint for undo
#send_action_command(mixer, "undopt", 1)

# Perform an undo
#send_action_command(mixer, "doundo", 1)

# Play next track from USB recorder
#send_action_command(mixer, "playtrack", 1)

# Renew LCD screen display
#send_action_command(mixer, "newscreen", 1)

# Clear all solo buttons
#send_action_command(mixer, "clearsolo", 1)

# Set sampling rate to 48kHz
#send_action_command(mixer, "setsrate", 0)

# Select RTA source channel #1 (Ch 1)
#send_action_command(mixer, "setrtasrc", 0)


def send_action_command(mixer, command, value=None):
    if value is not None:
        response = mixer.send("/-action/" + command, value)
    else:
        response = mixer.send("/-action/" + command)
    return response

# Renew LCD screen display
#send_action_command(mixer, "newscreen", 1)

# Select and execute record #3 in the current directory
#send_action_command(mixer, "recselect", 3)

# Load saved cue #10
#send_action_command(mixer, "gocue", 10)

# Load saved scene #5
#send_action_command(mixer, "goscene", 5)

# Load saved snippet #2
#send_action_command(mixer, "gosnippet", 2)

# Select X-Live! sdcard record session index 6
#send_action_command(mixer, "selsession", 6)


def send_action_command(mixer, command, value=None):
    if value is not None:
        response = mixer.send("/-action/" + command, value)
    else:
        response = mixer.send("/-action/" + command)
    return response

# Delete X-Live! sdcard record session index 6
#send_action_command(mixer, "delsession", 6)

# Select X-Live! marker index 10
#send_action_command(mixer, "selmarker", 10)

# Delete X-Live! marker index 5
#send_action_command(mixer, "delmarker", 5)

# Save X-Live! sdcard position at marker index 3
#send_action_command(mixer, "savemarker", 3)

# Add X-Live! Marker
#send_action_command(mixer, "addmarker", 1)

# Set X-Live! sdcard position to 5000 milliseconds
#send_action_command(mixer, "setposition", 5000)

# Clear X-Live! alert status
#send_action_command(mixer, "clearalert", 1)


def send_action_command(mixer, command, value=None):
    if value is not None:
        response = mixer.send("/-action/" + command, value)
    else:
        response = mixer.send("/-action/" + command)
    return response

# Format active sdcard
#send_action_command(mixer, "formatcard", 0)


def get_xlive_data(mixer):
    xlive_data = {
        "sessionmax": mixer.query("/-urec/sessionmax"),
        "markermax": mixer.query("/-urec/markermax"),
        "sessionlen": mixer.query("/-urec/sessionlen"),
        "sessionpos": mixer.query("/-urec/sessionpos"),
        "markerpos": mixer.query("/-urec/markerpos"),
        "batterystate": mixer.query("/-urec/batterystate"),
        "srate": mixer.query("/-urec/srate"),
        "tracks": mixer.query("/-urec/tracks"),
        "sessionspan": mixer.query("/-urec/sessionspan"),
        "sessionoffs": mixer.query("/-urec/sessionoffs"),
        "sd1state": mixer.query("/-urec/sd1state"),
        "sd2state": mixer.query("/-urec/sd2state"),
        "sd1info": mixer.query("/-urec/sd1info")
    }
    return xlive_data
xlive_data = get_xlive_data(mixer)
print(xlive_data)


def get_xlive_session_names(mixer):
    session_names = {}
    for session_num in range(1, 101):
        param = f"/-urec/session/{session_num:03d}/name"
        session_name = mixer.query(param)
        if session_name:
            session_names[session_num] = session_name
    return session_names

def get_xlive_marker_times(mixer):
    marker_times = {}
    for marker_num in range(1, 101):
        param = f"/-urec/marker/{marker_num:03d}/time"
        marker_time = mixer.query(param)
        if marker_time is not None:
            marker_times[marker_num] = marker_time
    return marker_times


def get_additional_status_data_previous(mixer):
    response = mixer.query("/-stat/solosw/03")
    solo_channel_03 = bool(int(response))

    response = mixer.query("/-stat/solosw/04")
    solo_channel_04 = bool(int(response))

    response = mixer.query("/-stat/solosw/05")
    solo_channel_05 = bool(int(response))

    response = mixer.query("/-stat/solosw/06")
    solo_channel_06 = bool(int(response))

    response = mixer.query("/-stat/solosw/07")
    solo_channel_07 = bool(int(response))

    response = mixer.query("/-stat/solosw/08")
    solo_channel_08 = bool(int(response))

    # Store the status data in a dictionary
    additional_status_data_previous = {
        "solo_channel_03": solo_channel_03,
        "solo_channel_04": solo_channel_04,
        "solo_channel_05": solo_channel_05,
        "solo_channel_06": solo_channel_06,
        "solo_channel_07": solo_channel_07,
        "solo_channel_08": solo_channel_08,
    }

    return additional_status_data_previous


def get_additional_status_data_latest(mixer):
    response = mixer.query("/-stat/urec/state")
    xlive_state = int(response)

    # X-Live! extension card state
    xlive_states = {
        0: "STOP",
        1: "PPAUSE",
        2: "PLAY",
        3: "REC",
    }

    response = mixer.query("/-stat/urec/rtime")
    xlive_recording_time = int(response)

    response = mixer.query("/-stat/urec/etime")
    xlive_elapsed_time = int(response)

    # Convert elapsed and remaining time from milliseconds to seconds
    xlive_elapsed_time_sec = xlive_elapsed_time // 1000
    xlive_recording_time_sec = xlive_recording_time // 1000

    response = mixer.query("/-stat/urec/state")
    xlive_state = xlive_states[int(response)]

    response = mixer.query("/-urec/sd1info")
    xlive_sd1_info = response.strip()

    response = mixer.query("/-urec/session/002/name")
    xlive_session_name = response.strip()

    response = mixer.query("/-urec/sessionmax")
    xlive_session_max = int(response)

    response = mixer.query("/-urec/sessionlen")
    xlive_session_length = int(response)

    response = mixer.query("/-urec/sessionpos")
    xlive_session_position = int(response)

    # Store the status data in a dictionary
    additional_status_data_latest = {
        "xlive_state": xlive_state,
        "xlive_recording_time_sec": xlive_recording_time_sec,
        "xlive_elapsed_time_sec": xlive_elapsed_time_sec,
        "xlive_sd1_info": xlive_sd1_info,
        "xlive_session_name": xlive_session_name,
        "xlive_session_max": xlive_session_max,
        "xlive_session_length": xlive_session_length,
        "xlive_session_position": xlive_session_position,
    }

    return additional_status_data_latest


def get_latest_status_data(mixer):
    response = mixer.query("/-stat/screen/CHAN/page")
    screen_chan_page = int(response)

    # Store the status data in a dictionary
    latest_status_data = {
        "screen_chan_page": screen_chan_page,
    }

    return latest_status_data


def get_ch_mix_levels(mixer):
    ch_mix_levels = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/1/level")
        ch_mix_levels[f"ch{ch_num}_mix1_level"] = float(response)

        # Add more mix levels if needed (2 to n)

    return ch_mix_levels

def get_bus_mix_levels(mixer):
    bus_mix_levels = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/1/level")
        bus_mix_levels[f"bus{bus_num}_mix1_level"] = float(response)

        # Add more mix levels if needed (2 to n)

    return bus_mix_levels

def get_main_stereo_mix_levels(mixer):
    main_stereo_mix_levels = {}
    response = mixer.query("/main/st/mix/1/level")
    main_stereo_mix_levels["main_st_mix1_level"] = float(response)

    # Add more main stereo mix levels if needed (2 to n)

    return main_stereo_mix_levels

def get_main_mono_mix_levels(mixer):
    main_mono_mix_levels = {}
    response = mixer.query("/main/m/mix/1/level")
    main_mono_mix_levels["main_mono_mix1_level"] = float(response)

    # Add more main mono mix levels if needed (2 to n)

    return main_mono_mix_levels

def get_fx_return_mix_levels(mixer):
    fx_return_mix_levels = {}
    for fx_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fx_num:02d}/mix/1/level")
        fx_return_mix_levels[f"fx{fx_num}_mix1_level"] = float(response)

        # Add more fx return mix levels if needed (2 to n)

    return fx_return_mix_levels

def get_aux_in_mix_levels(mixer):
    aux_in_mix_levels = {}
    for aux_num in range(1, 7):
        response = mixer.query(f"/auxin/{aux_num:02d}/mix/1/level")
        aux_in_mix_levels[f"aux{aux_num}_mix1_level"] = float(response)

        # Add more aux in mix levels if needed (2 to n)

    return aux_in_mix_levels

def get_screen_channel_page(mixer):
    response = mixer.query("/-stat/screen/CHAN/page")
    screen_channel_page = int(response)
    return screen_channel_page

def get_bussendbank(mixer):
    response = mixer.query("/-stat/bussendbank")
    bussendbank = int(response)
    return bussendbank

def get_ch_mix_mlevel(mixer):
    ch_mix_mlevel = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/mlevel")
        ch_mix_mlevel[f"ch{ch_num}_mix_mlevel"] = float(response)

    return ch_mix_mlevel

def get_bus_mix_mlevel(mixer):
    bus_mix_mlevel = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/mlevel")
        bus_mix_mlevel[f"bus{bus_num}_mix_mlevel"] = float(response)

    return bus_mix_mlevel

def get_fx_return_mix_mlevel(mixer):
    fx_return_mix_mlevel = {}
    for fx_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fx_num:02d}/mix/mlevel")
        fx_return_mix_mlevel[f"fx{fx_num}_mix_mlevel"] = float(response)

    return fx_return_mix_mlevel

def get_aux_in_mix_mlevel(mixer):
    aux_in_mix_mlevel = {}
    for aux_num in range(1, 7):
        response = mixer.query(f"/auxin/{aux_num:02d}/mix/mlevel")
        aux_in_mix_mlevel[f"aux{aux_num}_mix_mlevel"] = float(response)

    return aux_in_mix_mlevel

def get_ch_mix_mono(mixer):
    ch_mix_mono = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/mono")
        ch_mix_mono[f"ch{ch_num}_mix_mono"] = int(response)

    return ch_mix_mono

def get_bus_mix_mono(mixer):
    bus_mix_mono = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/mono")
        bus_mix_mono[f"bus{bus_num}_mix_mono"] = int(response)

    return bus_mix_mono

def get_fx_return_mix_mono(mixer):
    fx_return_mix_mono = {}
    for fx_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fx_num:02d}/mix/mono")
        fx_return_mix_mono[f"fx{fx_num}_mix_mono"] = int(response)

    return fx_return_mix_mono

def get_aux_in_mix_mono(mixer):
    aux_in_mix_mono = {}
    for aux_num in range(1, 7):
        response = mixer.query(f"/auxin/{aux_num:02d}/mix/mono")
        aux_in_mix_mono[f"aux{aux_num}_mix_mono"] = int(response)

    return aux_in_mix_mono

def get_ch_mix_pan(mixer):
    ch_mix_pan = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/pan")
        ch_mix_pan[f"ch{ch_num}_mix_pan"] = float(response)

    return ch_mix_pan

def get_bus_mix_pan(mixer):
    bus_mix_pan = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/pan")
        bus_mix_pan[f"bus{bus_num}_mix_pan"] = float(response)

    return bus_mix_pan

def get_fx_return_mix_pan(mixer):
    fx_return_mix_pan = {}
    for fx_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fx_num:02d}/mix/pan")
        fx_return_mix_pan[f"fx{fx_num}_mix_pan"] = float(response)

    return fx_return_mix_pan

def get_aux_in_mix_pan(mixer):
    aux_in_mix_pan = {}
    for aux_num in range(1, 7):
        response = mixer.query(f"/auxin/{aux_num:02d}/mix/pan")
        aux_in_mix_pan[f"aux{aux_num}_mix_pan"] = float(response)

    return aux_in_mix_pan

def get_ch_mix_st(mixer):
    ch_mix_st = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/st")
        ch_mix_st[f"ch{ch_num}_mix_st"] = float(response)

    return ch_mix_st

def get_bus_mix_st(mixer):
    bus_mix_st = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/st")
        bus_mix_st[f"bus{bus_num}_mix_st"] = float(response)

    return bus_mix_st

def get_fx_return_mix_st(mixer):
    fx_return_mix_st = {}
    for fx_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fx_num:02d}/mix/st")
        fx_return_mix_st[f"fx{fx_num}_mix_st"] = float(response)

    return fx_return_mix_st

def get_aux_in_mix_st(mixer):
    aux_in_mix_st = {}
    for aux_num in range(1, 7):
        response = mixer.query(f"/auxin/{aux_num:02d}/mix/st")
        aux_in_mix_st[f"aux{aux_num}_mix_st"] = float(response)

    return aux_in_mix_st

def get_screen_usb_page(mixer):
    response = mixer.query("/-stat/screen/USB/page")
    screen_usb_page = int(response)
    return screen_usb_page


def get_config_solo_mono(mixer):
    response = mixer.query("/config/solo/mono")
    config_solo_mono = int(response)
    return config_solo_mono

def get_screen_channel_page(mixer):
    response = mixer.query("/-stat/screen/CHAN/page")
    screen_channel_page = int(response)
    return screen_channel_page

def get_stat_talk_A(mixer):
    response = mixer.query("/-stat/talk/A")
    stat_talk_A = int(response)
    return stat_talk_A

def get_config_solo_dim(mixer):
    response = mixer.query("/config/solo/dim")
    config_solo_dim = int(response)
    return config_solo_dim

def get_stat_talk_B(mixer):
    response = mixer.query("/-stat/talk/B")
    stat_talk_B = int(response)
    return stat_talk_B

def get_stat_undo_time(mixer):
    response = mixer.query("/-undo/time")
    stat_undo_time = int(response)
    return stat_undo_time

def get_stat_userbank(mixer):
    response = mixer.query("/-stat/userbank")
    stat_userbank = int(response)
    return stat_userbank

def get_stat_screen_screen_screen(mixer):
    response = mixer.query("/-stat/screen/screen/screen")
    stat_screen_screen_screen = int(response)
    return stat_screen_screen_screen

def get_config_mute_levels(mixer):
    config_mute_levels = {}
    for mute_num in range(1, 7):
        response = mixer.query(f"/config/mute/{mute_num}")
        config_mute_levels[f"mute{mute_num}"] = int(response)

    return config_mute_levels

# Get config solo mono
config_solo_mono = get_config_solo_mono(mixer)

# Get screen channel page
screen_channel_page = get_screen_channel_page(mixer)

# Get stat talk A
stat_talk_A = get_stat_talk_A(mixer)

# Get config solo dim
config_solo_dim = get_config_solo_dim(mixer)

# Get stat talk B
stat_talk_B = get_stat_talk_B(mixer)

# Get stat undo time
stat_undo_time = get_stat_undo_time(mixer)

# Get stat user bank
stat_userbank = get_stat_userbank(mixer)

# Get stat screen screen screen
stat_screen_screen_screen = get_stat_screen_screen_screen(mixer)

# Get config mute levels
config_mute_levels = get_config_mute_levels(mixer)


def get_stat_selidx(mixer):
    response = mixer.query("/-stat/selidx")
    stat_selidx = response.strip()
    return stat_selidx

def get_stat_sendsonfader(mixer):
    response = mixer.query("/-stat/sendsonfader")
    stat_sendsonfader = int(response)
    return stat_sendsonfader

def get_stat_solosw(mixer):
    stat_solosw = {}
    for solosw_num in range(1, 71):
        response = mixer.query(f"/-stat/solosw/{solosw_num:02d}")
        stat_solosw[f"solosw{solosw_num:02d}"] = int(response)

    return stat_solosw

def get_ch_mix_on(mixer):
    ch_mix_on = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/on")
        ch_mix_on[f"ch{ch_num:02d}"] = int(response)

    return ch_mix_on

def get_bus_mix_on(mixer):
    bus_mix_on = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/on")
        bus_mix_on[f"bus{bus_num:02d}"] = int(response)

    return bus_mix_on

def get_auxin_mix_on(mixer):
    auxin_mix_on = {}
    for auxin_num in range(1, 9):
        response = mixer.query(f"/auxin/{auxin_num:02d}/mix/on")
        auxin_mix_on[f"auxin{auxin_num:02d}"] = int(response)

    return auxin_mix_on

def get_fxrtn_mix_on(mixer):
    fxrtn_mix_on = {}
    for fxrtn_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fxrtn_num:02d}/mix/on")
        fxrtn_mix_on[f"fxrtn{fxrtn_num:02d}"] = int(response)

    return fxrtn_mix_on

def get_dca_mix_on(mixer):
    dca_mix_on = {}
    for dca_num in range(1, 9):
        response = mixer.query(f"/dca/{dca_num}/mix/on")
        dca_mix_on[f"dca{dca_num}"] = int(response)

    return dca_mix_on

def get_main_m_mix_on(mixer):
    response = mixer.query("/main/m/mix/on")
    main_m_mix_on = int(response)
    return main_m_mix_on

def get_mtx_mix_on(mixer):
    mtx_mix_on = {}
    for mtx_num in range(1, 7):
        response = mixer.query(f"/mtx/{mtx_num:02d}/mix/on")
        mtx_mix_on[f"mtx{mtx_num:02d}"] = int(response)

    return mtx_mix_on

def get_stat_solo(mixer):
    response = mixer.query("/-stat/solo")
    stat_solo = int(response)
    return stat_solo

def get_ch_mix_fader(mixer):
    ch_mix_fader = {}
    for ch_num in range(1, 33):
        response = mixer.query(f"/ch/{ch_num:02d}/mix/fader")
        ch_mix_fader[f"ch{ch_num:02d}"] = float(response)

    return ch_mix_fader

def get_bus_mix_fader(mixer):
    bus_mix_fader = {}
    for bus_num in range(1, 17):
        response = mixer.query(f"/bus/{bus_num:02d}/mix/fader")
        bus_mix_fader[f"bus{bus_num:02d}"] = float(response)

    return bus_mix_fader

def get_auxin_mix_fader(mixer):
    auxin_mix_fader = {}
    for auxin_num in range(1, 9):
        response = mixer.query(f"/auxin/{auxin_num:02d}/mix/fader")
        auxin_mix_fader[f"auxin{auxin_num:02d}"] = float(response)

    return auxin_mix_fader

def get_fxrtn_mix_fader(mixer):
    fxrtn_mix_fader = {}
    for fxrtn_num in range(1, 9):
        response = mixer.query(f"/fxrtn/{fxrtn_num:02d}/mix/fader")
        fxrtn_mix_fader[f"fxrtn{fxrtn_num:02d}"] = float(response)

    return fxrtn_mix_fader

def get_dca_mix_fader(mixer):
    dca_mix_fader = {}
    for dca_num in range(1, 9):
        response = mixer.query(f"/dca/{dca_num}/mix/fader")
        dca_mix_fader[f"dca{dca_num}"] = float(response)

    return dca_mix_fader

def get_main_m_mix_fader(mixer):
    response = mixer.query("/main/m/mix/fader")
    main_m_mix_fader = float(response)
    return main_m_mix_fader

def get_mtx_mix_fader(mixer):
    mtx_mix_fader = {}
    for mtx_num in range(1, 7):
        response = mixer.query(f"/mtx/{mtx_num:02d}/mix/fader")
        mtx_mix_fader[f"mtx{mtx_num:02d}"] = float(response)

    return mtx_mix_fader

def get_main_st_mix_fader(mixer):
    response = mixer.query("/main/st/mix/fader")
    main_st_mix_fader = float(response)
    return main_st_mix_fader

def get_main_st_mix_on(mixer):
    response = mixer.query("/main/st/mix/on")
    main_st_mix_on = int(response)
    return main_st_mix_on

def get_stat_chfaderbank(mixer):
    response = mixer.query("/-stat/chfaderbank")
    stat_chfaderbank = int(response)
    return stat_chfaderbank

def get_stat_grpfaderbank(mixer):
    response = mixer.query("/-stat/grpfaderbank")
    stat_grpfaderbank = int(response)
    return stat_grpfaderbank

# Get stat selidx
stat_selidx = get_stat_selidx(mixer)

# Get stat sendsonfader
stat_sendsonfader = get_stat_sendsonfader(mixer)

# Get stat solosw
stat_solosw = get_stat_solosw(mixer)

# Get ch mix on
ch_mix_on = get_ch_mix_on(mixer)

# Get bus mix on
bus_mix_on = get_bus_mix_on(mixer)

# Get auxin mix on
auxin_mix_on = get_auxin_mix_on(mixer)

# Get fxrtn mix on
fxrtn_mix_on = get_fxrtn_mix_on(mixer)

# Get dca mix on
dca_mix_on = get_dca_mix_on(mixer)

# Get main m mix on
main_m_mix_on = get_main_m_mix_on(mixer)

# Get mtx mix on
mtx_mix_on = get_mtx_mix_on(mixer)

# Get stat solo
stat_solo = get_stat_solo(mixer)

# Get ch mix fader
ch_mix_fader = get_ch_mix_fader(mixer)

# Get bus mix fader
bus_mix_fader = get_bus_mix_fader(mixer)

# Get auxin mix fader
auxin_mix_fader = get_auxin_mix_fader(mixer)

# Get fxrtn mix fader
fxrtn_mix_fader = get_fxrtn_mix_fader(mixer)

# Get dca mix fader
dca_mix_fader = get_dca_mix_fader(mixer)

# Get main m mix fader
main_m_mix_fader = get_main_m_mix_fader(mixer)

# Get mtx mix fader
mtx_mix_fader = get_mtx_mix_fader(mixer)

# Get main st mix fader
main_st_mix_fader = get_main_st_mix_fader(mixer)

# Get main st mix on
main_st_mix_on = get_main_st_mix_on(mixer)

# Get stat chfaderbank
stat_chfaderbank = get_stat_chfaderbank(mixer)

# Get stat grpfaderbank
stat_grpfaderbank = get_stat_grpfaderbank(mixer)
