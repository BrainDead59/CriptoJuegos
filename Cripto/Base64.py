#!/usr/bin/env python3
import base64

ords = bytes.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf') #Hexadecimal to Bytes
ords = base64.b64encode(ords) #Bytes to Base64
print("Here is your flag:")
print(ords.decode())

#with base64 module, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.