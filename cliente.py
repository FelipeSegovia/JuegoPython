import xmlrpc.client

with xmlrpc.client.ServerProxy("http://192.168.0.16:8000/") as proxy:
    lista = proxy.mostrar_mapa()
    for i in range(len(lista)):
        print(lista[i])