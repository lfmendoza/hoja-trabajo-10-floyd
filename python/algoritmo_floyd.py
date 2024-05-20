def floyd_warshall(G):
    return dict(nx.floyd_warshall(G))

def obtener_ruta(matriz_caminos, origen, destino):
    return nx.reconstruct_path(origen, destino, matriz_caminos)

def centro_del_grafo(G, distancias):
    exc = {n: max(dists.values()) for n, dists in distancias.items()}
    centro = min(exc, key=exc.get)
    return centro
