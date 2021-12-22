from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from Node import Node


class TestGraphAlgo(TestCase):

    def test_init(self):
        self.fail()

    def test_get_graph(self):
        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        graph = DiGraph()
        graphAlgo = GraphAlgo(graph)
        graphAlgo.graph.add_node(0, (1, 2, 3))
        graphAlgo.graph.add_node(1, (1, 2, 3))
        graphAlgo.graph.add_node(2, (1, 2, 3))
        graphAlgo.graph.add_node(3, (1, 2, 3))
        graphAlgo.graph.add_node(4, (1, 2, 3))
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(3, 0, 3)
        graphAlgo.graph.add_edge(0, 2, 2)
        graphAlgo.graph.add_edge(1, 3, 4)
        graphAlgo.get_graph().add_edge(2, 3, 5)
        graphAlgo.graph.add_edge(4, 1, 3)
        graphAlgo.graph.add_edge(3, 4, 2)
        self.assertEqual((5, [0, 1, 3]), graphAlgo.shortest_path(0, 3))
        self.assertEqual((7, [0, 1, 3, 4]), graphAlgo.shortest_path(0, 4))
        self.assertEqual((4, [3, 0, 1]), graphAlgo.shortest_path(3, 1))

    def test_tsp(self):
        graph = DiGraph()
        graphAlgo = GraphAlgo(graph)
        graphAlgo.graph.add_node(0, (1, 2, 3))
        graphAlgo.graph.add_node(1, (1, 2, 3))
        graphAlgo.graph.add_node(2, (1, 2, 3))
        graphAlgo.graph.add_node(3, (1, 2, 3))
        graphAlgo.graph.add_node(4, (1, 2, 3))
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(3, 0, 3)
        graphAlgo.graph.add_edge(0, 2, 2)
        graphAlgo.graph.add_edge(1, 3, 4)
        graphAlgo.get_graph().add_edge(2, 3, 5)
        graphAlgo.graph.add_edge(4, 1, 3)
        graphAlgo.graph.add_edge(3, 4, 2)
        list1 = [0, 2, 4]
        list2 = [0, 4]
        self.assertEqual(graphAlgo.TSP(list1), ([0, 2, 3, 4], 9))
        self.assertEqual(graphAlgo.TSP(list2), ([0, 1, 3, 4], 7))

    def test_center_point(self):
        graph = DiGraph()
        graphAlgo = GraphAlgo(graph)
        graphAlgo.graph.add_node(0, (1, 2, 3))
        graphAlgo.graph.add_node(1, (1, 2, 3))
        graphAlgo.graph.add_node(2, (1, 2, 3))
        graphAlgo.graph.add_node(3, (1, 2, 3))
        graphAlgo.graph.add_node(4, (1, 2, 3))
        graphAlgo.graph.add_edge(0, 1, 1)
        graphAlgo.graph.add_edge(3, 0, 3)
        graphAlgo.graph.add_edge(0, 2, 2)
        graphAlgo.graph.add_edge(1, 3, 4)
        graphAlgo.graph.add_edge(4, 1, 3)
        graphAlgo.graph.add_edge(3, 4, 2)
        graphAlgo.graph.add_edge(2, 3, 3)
        self.assertEqual(graphAlgo.centerPoint(), (3, 5))

    def test_plot_graph(self):
        self.fail()
