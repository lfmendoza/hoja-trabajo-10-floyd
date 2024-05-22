package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.io.IOException;
public class GrafoTest {

    @Test
    public void testAgregarCiudad() {
        Grafo grafo = new Grafo(3);
        grafo.agregarCiudad("Mixco");
        grafo.agregarCiudad("Antigua");
        assertEquals(0, grafo.getIndice("Mixco"));
        assertEquals(1, grafo.getIndice("Antigua"));
    }

    @Test
    public void testAgregarArco() {
        Grafo grafo = new Grafo(3);
        grafo.agregarCiudad("Mixco");
        grafo.agregarCiudad("Antigua");
        grafo.agregarArco("Mixco", "Antigua", 30);
        assertEquals(30, grafo.getMatrizAdyacencia()[grafo.getIndice("Mixco")][grafo.getIndice("Antigua")]);
    }

    @Test
    public void testEliminarArco() {
        Grafo grafo = new Grafo(3);
        grafo.agregarCiudad("Mixco");
        grafo.agregarCiudad("Antigua");
        grafo.agregarArco("Mixco", "Antigua", 30);
        grafo.eliminarArco("Mixco", "Antigua");
        assertEquals(Integer.MAX_VALUE, grafo.getMatrizAdyacencia()[grafo.getIndice("Mixco")][grafo.getIndice("Antigua")]);
    }

    @Test
    public void testLeerGrafoDesdeArchivo() throws IOException {
        Grafo grafo = Grafo.leerGrafoDesdeArchivo();
        assertNotNull(grafo);
        assertTrue(grafo.getNumVertices() > 0);
    }
}