import networkx as nx

def main():
    G = leer_grafo_desde_archivo("guategrafo.txt")
    distancias = floyd_warshall(G)
    
    while True:
        print("Opciones del programa:")
        print("1. Ruta más corta entre dos ciudades")
        print("2. Ciudad centro del grafo")
        print("3. Modificar grafo")
        print("4. Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            origen = input("Ciudad origen: ")
            destino = input("Ciudad destino: ")
            ruta = obtener_ruta(distancias, origen, destino)
            print(f"Ruta más corta de {origen} a {destino}: {' -> '.join(ruta)}")
        elif opcion == 2:
            centro = centro_del_grafo(G, distancias)
            print(f"Ciudad centro del grafo: {centro}")
        elif opcion == 3:
            print("Opciones de modificación:")
            print("a) Interrupción de tráfico entre dos ciudades")
            print("b) Establecer conexión entre dos ciudades")
            opcion_mod = input("Ingrese su opción (a/b): ")

            if opcion_mod == 'a':
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                if G.has_edge(ciudad1, ciudad2):
                    G.remove_edge(ciudad1, ciudad2)
            elif opcion_mod == 'b':
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                km = int(input("Distancia en KM: "))
                G.add_edge(ciudad1, ciudad2, weight=km)

            distancias = floyd_warshall(G)
        elif opcion == 4:
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    