from unittest import TestCase
from DiGraph import DiGraph
from Node import Node


class TestDiGraph(TestCase):
    def test_v_size(self):
        graph = DiGraph()
        graph.add_node(0, (1, 2, 3))
        graph.add_node(1, (1, 2, 3))
        graph.add_node(2, (1, 2, 3))
        self.assertEqual(graph.nodes_size, 3)

    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(0, (1, 2, 3))
        graph.add_node(1, (1, 2, 3))
        graph.add_node(2, (1, 2, 3))
        graph.add_edge(1, 2, 3)
        graph.add_edge(0, 1, 4)
        self.assertEqual(graph.edges_size, 2)

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(0, (1, 2, 3))
        graph.add_node(1, (1, 2, 3))
        graph.add_node(2, (1, 2, 3))
        nodes = {0: Node(0, (1, 2, 3)), 1: Node(1, (1, 2, 3)), 2: Node(2, (1, 2, 3))}
        self.assertEqual(nodes.get(0).location, graph.get_all_v().get(0).location)

    def test_all_in_edges_of_node(self):
        self.fail()

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(0, (1, 2, 3))
        graph.add_node(1, (1, 2, 3))
        graph.add_node(2, (1, 2, 3))
        graph.add_edge(1, 2, 3)
        graph.add_edge(0, 1, 4)
        graph.add_edge(1, 0, 4)
        self.assertEqual(True, graph.remove_node(1))
        self.assertEqual(False, graph.remove_node(3))
        self.assertEqual(0, graph.e_size())

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(0, (1, 2, 3))
        graph.add_node(1, (1, 2, 3))
        graph.add_node(2, (1, 2, 3))
        graph.add_edge(1, 2, 3)
        graph.add_edge(1, 0, 3)
        graph.add_edge(0, 1, 4)
        self.assertEqual(True, graph.remove_edge(1, 2))
