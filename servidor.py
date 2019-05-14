from xmlrpc.server import SimpleXMLRPCServer
server = SimpleXMLRPCServer(("192.168.0.2", 8000))

matriz = []
archivo = open('mapa.txt','r') # este es el mapa inicial
for linea in archivo:
    matriz.append(linea.strip("\r\n"))
archivo.close()

def resetear_mapa():
    archivo = open ('mapa_m.txt','a') # reseteo el mapa cuando todos los jugadores salen de la partida o esta termina
    #for i in range(len(matriz)):
    #    archivo.write(matriz[i])
    #archivo.close()
    #return 1;
    
def mostrar_mapa():
    matriz_m = []
    archivo = open('mapa_m.txt','r') # este es el mapa que se va a ir modificando
    for linea in archivo:
        matriz_m.append(linea.strip("\r\n"))
    archivo.close()
    return (matriz_m)


def colocar_jugador(id):
    return 1


print("Esperando al cliente.. puerto 8000")
server.register_function(resetear_mapa, "resetear_mapa")
server.register_function(mostrar_mapa, "mostrar_mapa")
server.register_function(colocar_jugador,"colocar_jugador")
server.serve_forever()