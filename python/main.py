from grafo import Grafo
from algoritmo_floyd import floyd_warshall, obtener_ruta, centro_grafo

def main():
    grafo = Grafo.leer_grafo_desde_archivo()
    distancias, paths = floyd_warshall(grafo.grafo)

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
            if origen in grafo.ciudades and destino in grafo.ciudades:
                ruta = obtener_ruta(distancias, paths, origen, destino)
                print(f"Ruta más corta: {ruta}")
            else:
                print("Una o ambas ciudades no existen en el grafo.")
        elif opcion == 2:
            centro = centro_grafo(distancias)
            print(f"Ciudad centro del grafo: {centro}")
        elif opcion == 3:
            print("Opciones de modificación:")
            print("a) Interrupción de tráfico entre dos ciudades")
            print("b) Establecer conexión entre dos ciudades")
            opcion_mod = input("Ingrese su opción (a/b): ")

            if opcion_mod == 'a':
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                grafo.eliminar_arco(ciudad1, ciudad2)
            elif opcion_mod == 'b':
                ciudad1 = input("Ciudad 1: ")
                ciudad2 = input("Ciudad 2: ")
                km = int(input("Distancia en KM: "))
                grafo.agregar_arco(ciudad1, ciudad2, km)

            distancias, paths = floyd_warshall(grafo.grafo)
        elif opcion == 4:
            print("Programa terminado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
