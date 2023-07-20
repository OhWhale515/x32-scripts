import xair_api
import time
import math

def get_all_status_data(mixer):
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

    # Print all the status data
    print("Stat selidx:", stat_selidx)
    print("Stat sendsonfader:", stat_sendsonfader)
    print("Stat solosw:", stat_solosw)
    print("Ch mix on:", ch_mix_on)
    print("Bus mix on:", bus_mix_on)
    print("Auxin mix on:", auxin_mix_on)
    print("Fxrtn mix on:", fxrtn_mix_on)
    print("DCA mix on:", dca_mix_on)
    print("Main M mix on:", main_m_mix_on)
    print("Mtx mix on:", mtx_mix_on)
    print("Stat solo:", stat_solo)
    print("Ch mix fader:", ch_mix_fader)
    print("Bus mix fader:", bus_mix_fader)
    print("Auxin mix fader:", auxin_mix_fader)
    print("Fxrtn mix fader:", fxrtn_mix_fader)
    print("DCA mix fader:", dca_mix_fader)
    print("Main M mix fader:", main_m_mix_fader)
    print("Mtx mix fader:", mtx_mix_fader)
    print("Main ST mix fader:", main_st_mix_fader)
    print("Main ST mix on:", main_st_mix_on)
    print("Stat chfaderbank:", stat_chfaderbank)
    print("Stat grpfaderbank:", stat_grpfaderbank)

def main():
    kind_id = "X32"
    ip = "192.168.1.247"

    with xair_api.connect(kind_id, ip=ip) as mixer:
        # Wait for the mixer to initialize
        time.sleep(2)

        # Get all the status data
        get_all_status_data(mixer)

if __name__ == "__main__":
    main()
