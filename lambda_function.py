# Name: Jia Von Then
# Date: 13 January 2024

import json
from struct import unpack

# state is a string, with the following corresponding values are used to create a python dictionary
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

def payload(value):
    
    #  Decode hexadecimal to bytes
    pckt = bytes.fromhex(value["payload"])

    # Due to space optimization, the information is not byte aligned. A field can start in the middle of a byte. We therfore need bit operations to decode the payload
    # Therefore I shift the 4 bits to the right
    bit_shift = unpack('<Q',pckt)[0] >> 4

    # Dictionary to store the key-value pairs
    stdout = {}

    stdout['device'] = value["device"]

    # A 32-bitmask was used to read only the appropriate bit range 
    stdout['time'] = bit_shift & 0xFFFFFFFF

    # 4 bit shift to the right was conducted on the 4th byte to obtain the state integer
    # the integer was used to find the key-value pair in state_dictionary defined previously
    stdout['state'] = state_dictionary[unpack('<B',pckt[4:5])[0] >> 4]

    # state of charge represents the charge of the battery. It is a float with values between 0 and 100 and a 0.5 precision. To store it as an integer it was multiplied by 2
    stdout['state-of_charge'] = unpack('<B', pckt[5:6])[0] / 2

    # battery temperature represents the temperature of the battery. Values can vary between -20 and 100. The precision is 0.5. To store it as an integer we added 20 and multiplied it by 2
    stdout['temperature'] = unpack('<B', pckt[6:7])[0] / 2 - 20
    
    # and logs the data to stdout in the following format:
    return json.dumps(stdout)

# Write a Python lambda function that takes as input an event:
# Python lambda function is defined as 'lambda arguments : expression'
# References: https://www.w3schools.com/python/python_lambda.asp
lambda event: payload(json.loads(event))
