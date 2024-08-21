#!/usr/bin/env python3
from pwn import xor
from Crypto.Util.number import *
import itertools

# flag xor byte = 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d //hexadecimal

test = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d") #genera la conversion a bytes, se guarda como una cadena de bytes

# print(test) # se muestra la cadena de bytes, al ser cadena se muestra el char que representa cada byte
# print(test.decode())
# for val in test: #cuando se acceden los valores se obtiene la representación en int es decir el ascii de cada char
#     print(val)

for order in range(256):
    resul = xor(order,test) # xor de la cadena de bytes con el valor int, genera una cadena de bytes
    cadena = ""
    for val in resul: # para poder generar la cadena normal es necesario el iterar sobre la cadena
        cadena += chr(val)
    if(cadena.startswith("crypto")):
        print(cadena)
        print(order)

