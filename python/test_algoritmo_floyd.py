import unittest
import networkx as nx
from algoritmo_floyd import floyd_warshall, obtener_ruta, centro_grafo

class TestAlgoritmoFloyd(unittest.TestCase):

    def setUp(self):
        self.grafo = nx.DiGraph()
        self.grafo.add_edge("A", "B", weight=3)
        self.grafo.add_edge("B", "A", weight=2)
        self.grafo.add_edge("B", "C", weight=7)
        self.distancias, self.next_node = floyd_warshall(self.grafo)
        self.nodes = list(self.grafo.nodes)

    def test_floyd_warshall(self):
        self.assertEqual(self.distancias[self.nodes.index("A")][self.nodes.index("B")], 3)
        self.assertEqual(self.distancias[self.nodes.index("B")][self.nodes.index("A")], 2)
        self.assertEqual(self.distancias[self.nodes.index("B")][self.nodes.index("C")], 7)

    def test_obtener_ruta(self):
        ruta = obtener_ruta(self.next_node, self.nodes, "A", "B")
        self.assertEqual(ruta, "Ruta: A -> B, Peso: 1.00 KM")

    def test_centro_grafo(self):
        centro = centro_grafo(self.distancias, self.nodes)
        self.assertEqual(centro, "B")

if __name__ == "__main__":
    unittest.main()
