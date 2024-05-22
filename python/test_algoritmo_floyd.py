import unittest
import networkx as nx
from algoritmo_floyd import floyd_warshall, obtener_ruta, centro_del_grafo

class TestAlgoritmoFloyd(unittest.TestCase):

    def setUp(self):
        self.grafo = nx.DiGraph()
        self.grafo.add_edge("A", "B", weight=3)
        self.grafo.add_edge("B", "A", weight=2)
        self.grafo.add_edge("B", "C", weight=7)

    def test_floyd_warshall(self):
        distancias = floyd_warshall(self.grafo)
        self.assertEqual(distancias["A"]["B"], 3)
        self.assertEqual(distancias["B"]["A"], 2)
        self.assertEqual(distancias["B"]["C"], 7)

    def test_obtener_ruta(self):
        distancias = floyd_warshall(self.grafo)
        ruta = obtener_ruta(distancias, "A", "B")
        self.assertEqual(ruta, ["A", "B"])

    def test_centro_del_grafo(self):
        distancias = floyd_warshall(self.grafo)
        centro = centro_del_grafo(self.grafo, distancias)
        self.assertEqual(centro, "A")  # Ajusta según tu implementación específica

if __name__ == "__main__":
    unittest.main()
