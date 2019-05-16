import socket 
from _thread import *
import threading 
  
#Para realizar bloqueo del hilo
print_lock = threading.Lock() 
  
#funcion threaded
def threaded(socket_del_cliente): 
    while True: 
        # datos recibidos del cliente 
        dato = socket_del_cliente.recv(1024).decode() 
        # si no recibe nada suelta el hilo
        if not dato: 
            print('El cliente termino su conexion, desbloqueando el hilo...')
            #desbloqueando el hilo
            print_lock.release() 
            break
        # le respondo al cliente
        mensaje_del_servidor=" soy el servidor"
        socket_del_cliente.send(mensaje_del_servidor.encode()) 
    socket_del_cliente.close() 
  
  
def Main(): 
    host = "" 
    port = 8000
    un_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    un_socket.bind((host, port)) 
    print("socket enlazado al puerto: ", port) 
    un_socket.listen(5)
    print("socket a la espera de 5 clientes") 
  
    while True:
        #Aqui se detiene a esperar una conexion obtieniendo un socket y el (ip mas puerto)
        socket_del_cliente, direccion = un_socket.accept()
        #Bloqueando
        print_lock.acquire()
        #direccion 0 es la ip y direccion 1 es el puerto
        print('conectado a :', direccion[0], ':', direccion[1]) 
        # Comienza un nuevo hilo 
        start_new_thread(threaded, (socket_del_cliente,)) 
    un_socket.close() 
  
if __name__ == '__main__': 
    Main() 