import networkx as nx

def leer_grafo_desde_archivo(nombre_archivo):
    G = nx.DiGraph()
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            ciudad1, ciudad2, km = linea.strip().split()
            G.add_edge(ciudad1, ciudad2, weight=int(km))
    return G
