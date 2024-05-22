import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def floyd_warshall(grafo):
    nodes = list(grafo.nodes)
    num_nodes = len(nodes)
    dist = np.full((num_nodes, num_nodes), np.inf)
    next_node = np.zeros((num_nodes, num_nodes), dtype=int)

    for i in range(num_nodes):
        dist[i, i] = 0

    for u, v, data in grafo.edges(data=True):
        i, j = nodes.index(u), nodes.index(v)
        dist[i, j] = data['weight']
        next_node[i, j] = j

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    next_node[i, j] = next_node[i, k]

    return dist, next_node

def obtener_ruta(next_node, nodes, origen, destino):
    i, j = nodes.index(origen), nodes.index(destino)
    if np.isinf(next_node[i, j]):
        return "No hay camino"
    camino = [origen]
    while i != j:
        i = next_node[i, j]
        camino.append(nodes[i])
    distancia = next_node[nodes.index(origen), nodes.index(destino)]
    return f"Ruta: {' -> '.join(camino)}, Peso: {distancia:.2f} KM"

def centro_grafo(dist, nodes):
    max_distancia_por_nodo = {nodes[i]: max(dist[i]) for i in range(len(nodes))}
    centro = min(max_distancia_por_nodo, key=max_distancia_por_nodo.get)
    return centro

def mostrar_grafo(grafo):
    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold", arrowsize=20)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()
