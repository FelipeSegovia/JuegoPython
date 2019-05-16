import socket 
  
def Main(): 
    host = '192.168.0.2'
    port = 8000
  
    un_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    un_socket.connect((host,port)) 
    message = "hola servidor culiao"
    while True: 
        un_socket.send(message.encode())
        dato = un_socket.recv(1024).decode() 
        print('Mensaje recibido del server :',dato)   
        opcion = input('\nQuieres continuar(s/n) :') 
        if opcion == 's': 
            continue
        elif opcion == 'n': 
            break 
    un_socket.close() 
  
if __name__ == '__main__': 
    Main() 