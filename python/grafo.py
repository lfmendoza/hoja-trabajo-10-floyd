import os
import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.ciudades = {}

    def agregar_ciudad(self, ciudad):
        if ciudad not in self.ciudades:
            self.ciudades[ciudad] = len(self.ciudades)
            self.grafo.add_node(ciudad)

    def agregar_arco(self, ciudad1, ciudad2, distancia):
        self.grafo.add_edge(ciudad1, ciudad2, weight=distancia)

    def eliminar_arco(self, ciudad1, ciudad2):
        if self.grafo.has_edge(ciudad1, ciudad2):
            self.grafo.remove_edge(ciudad1, ciudad2)

    def get_matriz_adyacencia(self):
        return nx.adjacency_matrix(self.grafo, weight='weight').todense()

    def get_ciudad(self, indice):
        for ciudad, idx in self.ciudades.items():
            if idx == indice:
                return ciudad
        return None

    def get_indice(self, ciudad):
        return self.ciudades.get(ciudad, -1)

    def get_num_vertices(self):
        return len(self.ciudades)

    def get_ciudades(self):
        return list(self.ciudades.keys())

    @staticmethod
    def leer_grafo_desde_archivo():
        grafo = Grafo()
        path = os.path.join(os.path.dirname(__file__), 'resources', 'guategrafo.txt')
        with open(path, 'r') as file:
            for linea in file:
                ciudad1, ciudad2, km = linea.strip().split()
                km = int(km)
                grafo.agregar_ciudad(ciudad1)
                grafo.agregar_ciudad(ciudad2)
                grafo.agregar_arco(ciudad1, ciudad2, km)
        return grafo
