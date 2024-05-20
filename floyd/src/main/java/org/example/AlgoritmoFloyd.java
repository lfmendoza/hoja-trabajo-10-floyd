package org.example;

public class AlgoritmoFloyd {
    public static int[][] floydWarshall(int[][] grafo) {
        int V = grafo.length;
        int[][] dist = new int[V][V];
        int[][] next = new int[V][V];

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (i != j && grafo[i][j] == Integer.MAX_VALUE) {
                    next[i][j] = -1;
                } else {
                    next[i][j] = j;
                }
                dist[i][j] = grafo[i][j];
            }
        }

        for (int k = 0; k < V; k++) {
            for (int i = 0; i < V; i++) {
                for (int j = 0; j < V; j++) {
                    if (dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE && dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                        next[i][j] = next[i][k];
                    }
                }
            }
        }

        return dist;
    }

    public static String obtenerRuta(int[][] next, int i, int j) {
        if (next[i][j] == -1) return "No hay camino";
        StringBuilder path = new StringBuilder();
        while (i != j) {
            path.append(i).append(" -> ");
            i = next[i][j];
        }
        path.append(j);
        return path.toString();
    }

    public static String centroGrafo(int[][] dist, Grafo grafo) {
        int V = dist.length;
        int[] maxDist = new int[V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][j] != Integer.MAX_VALUE) {
                    maxDist[i] = Math.max(maxDist[i], dist[i][j]);
                }
            }
        }
        int minMaxDist = Integer.MAX_VALUE;
        int centro = -1;
        for (int i = 0; i < V; i++) {
            if (maxDist[i] < minMaxDist) {
                minMaxDist = maxDist[i];
                centro = i;
            }
        }
        return grafo.getCiudad(centro);
    }
}

