import networkx as nx
import os

def leer_grafo_desde_archivo():
    path = os.path.join(os.path.dirname(__file__), 'resources', 'guategrafo.txt')
    G = nx.DiGraph()
    with open(path, 'r') as file:
        for linea in file:
            ciudad1, ciudad2, km = linea.strip().split()
            G.add_edge(ciudad1, ciudad2, weight=int(km))
    return G
