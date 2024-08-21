#!/usr/bin/env python3

ords = bytes.fromhex('63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d')

print("Here is your flag:")
print(ords.decode())

#decode tranforma a cadena normal de forma inmediata
#encode transforma a cadena de bytes con default de utf-8
#the bytes.fromhex() function can be used to convert hex to bytes. The .hex() instance method can be called on byte strings to get the hex representation.