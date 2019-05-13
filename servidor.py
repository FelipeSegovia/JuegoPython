from xmlrpc.server import SimpleXMLRPCServer

def mostrar_mapa():
    a = []
    archivo = open('mapa.txt','r')
    for linea in archivo:
        a.append(linea.strip("\r\n"))
    archivo.close
    return a

server = SimpleXMLRPCServer(("192.168.0.16", 8000))
print("Listening on port 8000...")
server.register_function(mostrar_mapa, "mostrar_mapa")
server.serve_forever()