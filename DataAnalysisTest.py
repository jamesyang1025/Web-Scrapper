import unittest
from Graph import Graph
import Main


class TestGraph(unittest.TestCase):

    def test_find_hub_actors(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        self.assertEqual("Bruce Willis", graph.find_hub_actors())

    def test_find_most_grossing_age_group(self):
        graph = Graph()

        Main.load_data_to_graph(graph)

        self.assertEqual("81-85", graph.find_most_grossing_age_group())


if __name__ == '__main__':
    unittest.main()
