import networkx as nx

def floyd_warshall(grafo):
    distancias, paths = nx.floyd_warshall_predecessor_and_distance(grafo, weight='weight')
    return distancias, paths

def obtener_ruta(distancias, paths, origen, destino):
    if origen not in distancias or destino not in distancias[origen]:
        return "No hay camino"
    camino = []
    actual = destino
    while actual != origen:
        camino.insert(0, actual)
        actual = paths[origen][actual]
        if actual is None:
            return "No hay camino"
    camino.insert(0, origen)
    distancia = distancias[origen][destino]
    return f"Ruta: {' -> '.join(camino)}, Peso: {distancia:.2f} KM"

def centro_grafo(distancias):
    max_distancia_por_nodo = {nodo: max(distancias[nodo].values()) for nodo in distancias}
    centro = min(max_distancia_por_nodo, key=max_distancia_por_nodo.get)
    return centro
