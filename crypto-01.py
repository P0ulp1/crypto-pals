#!/usr/bin/python3

from base64 import b64encode

#Declaring input variable
input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(input)

#Converting str to bytearray
inputRaw = bytearray.fromhex(input)

#Encoding all bytes to b64
output = b64encode(inputRaw)

print(output)

