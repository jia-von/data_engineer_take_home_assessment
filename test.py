import binascii
from pprint import pprint
from struct import unpack, pack
from struct import calcsize

# Given input hexadecimal data:
# F1E6E63676C75000

# output:

# {
# "time": 1668181615,
# "state": "error",
# "state_of_charge": 99.5,
# "temperature": 20.0
# }

# Read from right to left
# 8th byte: 00

# 7th byte: 50 -- temperature
# battery temperature represents the temperature of the battery. Values can vary between -20 and 100. The precision is 0.5. To store it as an integer we added 20 and multiplied it by 2

# 6th byte: C7 -- state_of_charge
# state of charge represents the charge of the battery. It is a float with values between 0 and 100 and a 0.5 precision. To store it as an integer it was multiplied by 2.

# 5th byte: 76 -- contains 4 bits of state and 4 bits of time
# 4th byte: 36 -- time
# 3th byte: E6 -- time
# 2nd bute: E6 -- time
# 1st byte: F1 --contains 4 bits of time and 4 bits of type


# decoded = bytes.fromhex('F1E6E63676C75000').decode('utf-32')
# print(decoded)

# hex_array = ['F1','E6','E6','36','76','C7','50','00']
hex_value = 'F1E6E63676C75000'
hex_value2 = '9164293726C85400'
hex_value3 = '6188293726C75C00'

# pckt = binascii.unhexlify('17640e100ed7021d004700550100')
# data = {}

# data["version"] = unpack(">B", pckt[0:1])[0]
# data["batt_lvl"] = unpack(">B", pckt[1:2])[0]
# data["interval"] = unpack(">H", pckt[2:4])[0]
# data["log_count"] = unpack(">H", pckt[4:6])[0]
# data["humidity"] = unpack(">h", pckt[6:8])[0] / 10
# data["dew_point"] = unpack(">h", pckt[8:10])[0] / 10
# data["temperature"] = unpack(">h", pckt[10:12])[0] / 10
# pprint(data)


# create dictionary for state

state_dict = {
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


pckt = bytearray.fromhex(hex_value)
bit_shift = unpack('<Q',pckt)[0] >> 4

data = {}

data['time'] = bit_shift & 0xFFFFFFFF
data["state"] = unpack('<B',pckt[4:5])[0] >> 4
data["state-of_charge"] = unpack('<B', pckt[5:6])[0] / 2
data["temperature"] = unpack('<B', pckt[6:7])[0] / 2 - 20

pprint(data)

# https://stackoverflow.com/questions/67559430/any-idea-how-to-decode-these-little-endian-bytes-in-python
# https://realpython.com/python-bitwise-operators/
# https://docs.python.org/3/library/struct.html#struct-alignment

