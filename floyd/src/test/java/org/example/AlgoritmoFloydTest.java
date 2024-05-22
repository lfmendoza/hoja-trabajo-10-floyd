package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class AlgoritmoFloydTest {

    @Test
    public void testFloydWarshall() {
        int[][] grafo = {
                {0, 3, Integer.MAX_VALUE},
                {2, 0, Integer.MAX_VALUE},
                {Integer.MAX_VALUE, 7, 0}
        };
        int[][] distancias = AlgoritmoFloyd.floydWarshall(grafo);
        assertEquals(3, distancias[0][1]);
        assertEquals(2, distancias[1][0]);
        assertEquals(7, distancias[2][1]);
    }

    @Test
    public void testObtenerRuta() {
        int[][] grafo = {
                {0, 3, Integer.MAX_VALUE},
                {2, 0, Integer.MAX_VALUE},
                {Integer.MAX_VALUE, 7, 0}
        };
        int[][] distancias = AlgoritmoFloyd.floydWarshall(grafo);
        int[][] next = {
                {0, 1, -1},
                {0, 1, -1},
                {1, 1, 2}
        };
        Grafo g = new Grafo(3);
        g.agregarCiudad("A");
        g.agregarCiudad("B");
        g.agregarCiudad("C");
        String ruta = AlgoritmoFloyd.obtenerRuta(distancias, next, 0, 1, g);
        assertEquals("Ruta: A -> B, Peso: 3 KM", ruta);
    }

    @Test
    public void testCentroGrafo() {
        int[][] grafo = {
                {0, 3, Integer.MAX_VALUE},
                {2, 0, Integer.MAX_VALUE},
                {Integer.MAX_VALUE, 7, 0}
        };
        int[][] distancias = AlgoritmoFloyd.floydWarshall(grafo);
        Grafo g = new Grafo(3);
        g.agregarCiudad("A");
        g.agregarCiudad("B");
        g.agregarCiudad("C");
        String centro = AlgoritmoFloyd.centroGrafo(distancias, g);
        assertEquals("A", centro);  // Ajusta según tu implementación específica
    }
}