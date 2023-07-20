import xair_api
import time

def use_case_test():
    kind_id = "X32"
    ip = "192.168.1.247"

    mixer = xair_api.connect(kind_id, ip=ip)
    with mixer:
        setup_mixer(mixer)
        perform_operations(mixer)
        check_results(mixer)

def setup_mixer(mixer):
    # Set up the mixer for the test scenario
    mixer.set_channel_volume(1, -10)
    mixer.set_channel_volume(2, -5)
    mixer.set_channel_pan(1, 20)
    mixer.set_channel_mute(1, True)

def perform_operations(mixer):
    # Perform various mixer operations during the use case test
    mixer.set_channel_volume(3, -8)
    mixer.set_channel_mute(3, False)
    mixer.set_aux_send_level(1, 3, -12)
    mixer.set_channel_eq_band(2, 'Low', 3)

def check_results(mixer):
    # Check the results after the operations are performed
    channel_volume = mixer.get_channel_volume(3)
    assert channel_volume == -8, "Volume level not set correctly"
    
    channel_mute = mixer.get_channel_mute(3)
    assert not channel_mute, "Mute status not set correctly"
    
    aux_send_level = mixer.get_aux_send_level(1, 3)
    assert aux_send_level == -12, "Aux send level not set correctly"
    
    eq_band_gain = mixer.get_channel_eq_band(2, 'Low')
    assert eq_band_gain == 3, "EQ band gain not set correctly"

if __name__ == "__main__":
    use_case_test()
