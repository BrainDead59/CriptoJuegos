#!/usr/bin/env python3
from pwn import xor

cadena = "label"
numero = 13

string = ""
for i in range(0,len(cadena)):
    resultado = ord(cadena[i])
    resultado = numero ^ resultado
    string+= chr(resultado)

print(string)

print(xor(numero,cadena).decode())

#ord convierte char a ascii
#chr convierte el ascii a char
#pwntools library has a convenient xor() function that can XOR together data of different types and lengths
#binarioNumero = int(format(numero,'b'))
#print(binarioNumero)