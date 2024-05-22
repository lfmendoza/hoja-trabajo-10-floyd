import unittest
from grafo import leer_grafo_desde_archivo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = leer_grafo_desde_archivo()

    def test_leer_grafo_desde_archivo(self):
        self.assertIsNotNone(self.grafo)
        self.assertGreater(len(self.grafo.nodes), 0)

    def test_agregar_nodo(self):
        self.grafo.add_node("NuevaCiudad")
        self.assertIn("NuevaCiudad", self.grafo.nodes)

    def test_agregar_arco(self):
        self.grafo.add_edge("Guatemala", "Antigua", weight=42)
        self.assertIn("Antigua", self.grafo["Guatemala"])

    def test_eliminar_arco(self):
        self.grafo.add_edge("Guatemala", "Antigua", weight=42)
        self.grafo.remove_edge("Guatemala", "Antigua")
        self.assertNotIn("Antigua", self.grafo["Guatemala"])

if __name__ == "__main__":
    unittest.main()
