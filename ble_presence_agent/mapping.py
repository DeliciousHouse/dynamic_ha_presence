def map_device_to_room(scan_results):
    mapping = {}
    for device, value in scan_results.items():
        if value < 5.0:
            mapping[device] = "occupant_nearby"
        else:
            mapping[device] = "occupant_away"
    return mapping
