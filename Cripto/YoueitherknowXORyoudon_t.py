#!/usr/bin/env python3
from pwn import xor
from Crypto.Util.number import *
import itertools

# flag  xor (secret xor "crypto{") = 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
# secret = 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 xor "crypto{" 
# 14 xor 99 = 109 and go on
# as it is an operation of one xor one, we need to complement the secret

test = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104") #genera la conversion a bytes, se guarda como una cadena de bytes
resul = xor(test[:7], "crypto{".encode())

cadena = ""
for val in resul:
    cadena += chr(val)
cadena += 'y'

cadena = cadena * (len(test)//len(cadena))
flag = xor(cadena,test)
print(flag.decode())


