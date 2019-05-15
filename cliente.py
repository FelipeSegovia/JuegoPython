import socket
import os
import subprocess
import time

def Main():
    host = "10.3.132.58"
    puerto = 8000

    socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_cliente.connect((host,puerto))

    alias = input("Ingrese su nombre: ")

    mensaje = input(alias+" ->")

    while mensaje != "q":
        socket_cliente.sendto("{}->{}".format(alias,mensaje).encode("utf-8"),(host,puerto))
        mensaje = socket_cliente.recv(1024)
        print(mensaje.decode('ascii')) 


if __name__ == "__main__":
    Main()