import unittest
from grafo import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = Grafo.leer_grafo_desde_archivo()

    def test_leer_grafo_desde_archivo(self):
        self.assertIsNotNone(self.grafo)
        self.assertGreater(len(self.grafo.grafo.nodes), 0)

    def test_agregar_nodo(self):
        self.grafo.agregar_ciudad("NuevaCiudad")
        self.assertIn("NuevaCiudad", self.grafo.grafo.nodes)

    def test_agregar_arco(self):
        self.grafo.agregar_arco("Guatemala", "Antigua", 42)
        self.assertIn("Antigua", self.grafo.grafo["Guatemala"])

    def test_eliminar_arco(self):
        self.grafo.agregar_arco("Guatemala", "Antigua", 42)
        self.grafo.eliminar_arco("Guatemala", "Antigua")
        self.assertNotIn("Antigua", self.grafo.grafo["Guatemala"])

if __name__ == "__main__":
    unittest.main()
