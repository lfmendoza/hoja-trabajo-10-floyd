package org.example;

import java.io.IOException;
import java.util.Scanner;

/**
 * Algoritmo de Floyd
 *
 */
public class App 
{
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        Grafo grafo = Grafo.leerGrafoDesdeArchivo();
        int[][] distancias = AlgoritmoFloyd.floydWarshall(grafo.getMatrizAdyacencia());
        int[][] next = AlgoritmoFloyd.floydWarshall(grafo.getMatrizAdyacencia());

        while (true) {
            System.out.println("Opciones del programa:");
            System.out.println("1. Ruta más corta entre dos ciudades");
            System.out.println("2. Ciudad centro del grafo");
            System.out.println("3. Modificar grafo");
            System.out.println("4. Salir");

            int opcion = scanner.nextInt();
            scanner.nextLine();  // Limpiar buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ciudad origen: ");
                    String origen = scanner.nextLine();
                    System.out.print("Ciudad destino: ");
                    String destino = scanner.nextLine();
                    int indiceOrigen = grafo.getIndice(origen);
                    int indiceDestino = grafo.getIndice(destino);

                    if (indiceOrigen >= 0 && indiceOrigen < grafo.getNumVertices() && indiceDestino >= 0 && indiceDestino < grafo.getNumVertices()) {
                        String ruta = AlgoritmoFloyd.obtenerRuta(distancias, next, indiceOrigen, indiceDestino, grafo);
                        System.out.println("Ruta más corta: " + ruta);
                    } else {
                        System.out.println("Índices fuera de los límites del grafo.");
                    }
                    break;

                case 2:
                    System.out.println("Ciudad centro del grafo: " + AlgoritmoFloyd.centroGrafo(distancias, grafo));
                    break;

                case 3:
                    System.out.println("Opciones de modificación:");
                    System.out.println("a) Interrupción de tráfico entre dos ciudades");
                    System.out.println("b) Establecer conexión entre dos ciudades");

                    char opcionMod = scanner.nextLine().charAt(0);
                    if (opcionMod == 'a') {
                        System.out.print("Ciudad 1: ");
                        String ciudad1 = scanner.nextLine();
                        System.out.print("Ciudad 2: ");
                        String ciudad2 = scanner.nextLine();
                        grafo.eliminarArco(ciudad1, ciudad2);
                    } else if (opcionMod == 'b') {
                        System.out.print("Ciudad 1: ");
                        String ciudad1 = scanner.nextLine();
                        System.out.print("Ciudad 2: ");
                        String ciudad2 = scanner.nextLine();
                        System.out.print("Distancia en KM: ");
                        int distancia = scanner.nextInt();
                        scanner.nextLine();  // Limpiar buffer
                        grafo.agregarArco(ciudad1, ciudad2, distancia);
                    }
                    distancias = AlgoritmoFloyd.floydWarshall(grafo.getMatrizAdyacencia());
                    next = AlgoritmoFloyd.floydWarshall(grafo.getMatrizAdyacencia());
                    break;

                case 4:
                    System.out.println("Programa terminado.");
                    return;

                default:
                    System.out.println("Opción no válida.");
                    break;
            }
        }
    }
}
