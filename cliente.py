import xmlrpc.client

while True:
    with xmlrpc.client.ServerProxy("http://192.168.0.2:8000/") as proxy:
        print("Bienvenido al pilla pilla")
        print("0 para salir")
        print("1 para mostrar mapa")
        print("2 para jugar")
        op = input("Ingrese opcion:")
        
        if (op=="1"):
            matriz = (proxy.mostrar_mapa())
            for i in range(len(matriz)):             
                print(matriz[i])
        elif (op=="2"):
            id = input("Ingrese la inicial de su nombre:")
            matriz = (proxy.colocar_jugador(id))
        elif (op=="0"):
            break
        
        
        