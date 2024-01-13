import json
from struct import unpack

state_dictionary = {
    0: "power off",
    1: "power on",
    2: "discharge",
    3: "charge",
    4: "charge complete",
    5: "host mode",
    6: "shutdown",
    7: "error",
    8: "undefined"
}

# event_data = {
#     'device': 'example_device',
#     'payload': '9164293726C85400'
# }

def payload(hex_value):
    
    pckt = bytearray.fromhex(hex_value)
    bit_shift = unpack('<Q',pckt)[0] >> 4

    stdout = {}

    stdout['time'] = bit_shift & 0xFFFFFFFF
    stdout['state'] = state_dictionary[unpack('<B',pckt[4:5])[0] >> 4]
    stdout['state-of_charge'] = unpack('<B', pckt[5:6])[0] / 2
    stdout['temperature'] = unpack('<B', pckt[6:7])[0] / 2 - 20
    
    print(json.dumps(stdout))

log_event = lambda event: payload(event['payload'])

log_event()

