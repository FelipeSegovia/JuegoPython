import socket
import sys
import threading
from time import gmtime, strftime
import time
from queue import Queue

NUMERO_DE_HILOS = 2
NUMERO_JOBS = [1, 2]
cola = Queue()

conexiones = []
direcciones = []

host = "192.168.1.20"
puerto = 8000
socket_servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_servidor.bind((host,puerto))
socket_servidor.listen(5)
def iniciar():
    for c in conexiones:
        c.close()

    #Vacio las conexiones y direcciones
    del conexiones[:]
    del direcciones[:]
    
    while True:
        try:
            con,dir = socket_servidor.accept()
            socket_servidor.setblocking(1) #prevengo el timeout

            conexiones.append(con)
            direcciones.append(dir)

            print("({})Conexion desde {} a sido establecida!".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),dir[0]))
            #Envio datos del servidor al cliente
            con.send(bytes("Bienvenido al servidor!","utf-8"))

            #Recibo datos desde el cliente al servidor
            dato = con.recv(1024)
            print(dir[0])
            print('Recibi: {!r}'.format(dato))
            for direccion in direcciones:
                if direccion != dir:
                    con.sendall(dato)
            
            
        except:
            print("Error en la conexion")
    

def Main():

    for _ in range(NUMERO_DE_HILOS):
        hilo = threading.Thread(target=iniciar)
        hilo.daemon = True
        hilo.start()
    
    for x in NUMERO_JOBS:
        cola.put(x)
    cola.join()

if __name__ == "__main__":
    Main()