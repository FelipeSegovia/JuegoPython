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

def crear_socket():
    try:
        global host
        global puerto
        global socket_servidor

        host  = "10.3.132.58"
        puerto = 8000
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Error al crear socket: "+ str(msg))

def conectar_socket():
    try:
        global host
        global puerto
        global socket_servidor
        print("Socket conectado: "+ str(puerto))

        socket_servidor.bind((host,puerto))
        socket_servidor.listen(5) #acepta 5 conexiones 
    except socket.error as msg:
        print("Error al conectar el socket: "+ str(msg)+"\nReinentando...")
        conectar_socket()

def aceptar_conexiones():
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

            print("({})Conexion desde {} a sido establecida!".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()),dir[0]))
            con.send(bytes("Bienvenido al servidor!","utf-8"))
            
        except:
            print("Error en la conexion")

def crear_hilos():
    for _ in range(NUMERO_DE_HILOS):
        hilo = threading.Thread(target=iniciar)
        hilo.daemon = True
        hilo.start()

def iniciar():
    while True:
        x = cola.get()
        if x == 1:
            crear_socket()
            conectar_socket()
            aceptar_conexiones()
        
        cola.task_done()

def crear_trabajos():
    for x in NUMERO_JOBS:
        cola.put(x)
    cola.join()

def Main():

    print("Hola desde el servidor")
    crear_hilos()
    crear_trabajos()

        
    
        


if __name__ == "__main__":
    Main()