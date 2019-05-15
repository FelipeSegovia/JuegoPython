import socket
import os
import subprocess
import time

def Main():
    host = "192.168.0.16"
    puerto = 8000

    socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_cliente.connect((host,puerto))

    alias = input("Ingrese su nombre: ")

    mensaje = input(alias+" ->")

    while mensaje != "q":
        socket_cliente.sendto("{}->{}".format(alias,mensaje).encode("utf-8"),(host,puerto))
        #msg = socket_cliente.recvfrom(1024)
        #print(msg.decode("utf-8"))
        #nuevo_socket.sendto("{}-> {}".format(alias,mensaje).encode("utf-8"), servidor)  


if __name__ == "__main__":
    Main()