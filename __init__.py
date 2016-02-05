import __future__

def create_instance(c_instance):

    return GenericScript(c_instance, device_map_mode, volume_map_mode, tuple(device_controls), transport_controls, tuple(volume_controls), tuple(trackarm_controls), bank_controls, controller_descriptions, mixer_options)