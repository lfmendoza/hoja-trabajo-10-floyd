package org.example;

import java.util.*;
import java.io.*;


public class Grafo {
    private int numVertices;
    private int[][] matrizAdyacencia;
    private Map<String, Integer> ciudadIndice;
    private List<String> indiceCiudad;

    public Grafo(int numVertices) {
        this.numVertices = numVertices;
        matrizAdyacencia = new int[numVertices][numVertices];
        for (int[] fila : matrizAdyacencia) {
            Arrays.fill(fila, Integer.MAX_VALUE);
        }
        ciudadIndice = new HashMap<>();
        indiceCiudad = new ArrayList<>(Collections.nCopies(numVertices, ""));
    }

    public void agregarCiudad(String ciudad) {
        if (!ciudadIndice.containsKey(ciudad)) {
            int indice = ciudadIndice.size();
            ciudadIndice.put(ciudad, indice);
            indiceCiudad.set(indice, ciudad);
        }
    }

    public void agregarArco(String ciudad1, String ciudad2, int distancia) {
        int indice1 = ciudadIndice.get(ciudad1);
        int indice2 = ciudadIndice.get(ciudad2);
        matrizAdyacencia[indice1][indice2] = distancia;
    }

    public void eliminarArco(String ciudad1, String ciudad2) {
        int indice1 = ciudadIndice.get(ciudad1);
        int indice2 = ciudadIndice.get(ciudad2);
        matrizAdyacencia[indice1][indice2] = Integer.MAX_VALUE;
    }

    public int[][] getMatrizAdyacencia() {
        return matrizAdyacencia;
    }

    public String getCiudad(int indice) {
        return indiceCiudad.get(indice);
    }

    public int getIndice(String ciudad) {
        return ciudadIndice.get(ciudad);
    }

    public int getNumVertices() {
        return numVertices;
    }

    public List<String> getCiudades() {
        return new ArrayList<>(ciudadIndice.keySet());
    }

    public static Grafo leerGrafoDesdeArchivo() throws IOException {
        InputStream inputStream = Grafo.class.getClassLoader().getResourceAsStream("guategrafo.txt");
        if (inputStream == null) {
            throw new FileNotFoundException("El archivo guategrafo.txt no se encuentra en src/main/resources");
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(inputStream));
        String linea;
        Set<String> ciudades = new HashSet<>();
        List<String[]> arcos = new ArrayList<>();

        while ((linea = br.readLine()) != null) {
            String[] partes = linea.split(" ");
            String ciudad1 = partes[0];
            String ciudad2 = partes[1];
            int distancia = Integer.parseInt(partes[2]);

            ciudades.add(ciudad1);
            ciudades.add(ciudad2);
            arcos.add(new String[]{ciudad1, ciudad2, String.valueOf(distancia)});
        }

        Grafo grafo = new Grafo(ciudades.size());
        for (String ciudad : ciudades) {
            grafo.agregarCiudad(ciudad);
        }
        for (String[] arco : arcos) {
            grafo.agregarArco(arco[0], arco[1], Integer.parseInt(arco[2]));
        }

        return grafo;
    }
}