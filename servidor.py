#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:

        client, client_address = SERVER.accept()
        print("%s:%s ha sido conectado." % client_address)
        client.send(bytes("Escribe!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
        """Handles a single client connection."""

        name = client.recv(BUFSIZ).decode("utf8")
        welcome = 'bienvenido %s! si quieres salir escribe {quit}.' % name
        client.send(bytes(welcome, "utf8"))
        msg = "%s ha entrado al chat!" % name
        broadcast(bytes(msg, "utf8"))
        clients[client] = name

        print("Tam: "+str(len(clients)))
        if str(len(clients)) < "3":
                while True:
                        msg = client.recv(BUFSIZ)
                        if msg != bytes("{quit}", "utf8"):
                                broadcast(msg, name+": ")
                        else:
                                client.send(bytes("{quit}", "utf8"))
                                client.close()
                                del clients[client]
                                broadcast(bytes("%s ha salido del chat." % name, "utf8"))
                                break
        else:
                print("Cliente invalido intenta escribir")


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = '10.3.132.21'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(2)
    #SERVER.setblocking(False)
    print("Esperando conexion...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()