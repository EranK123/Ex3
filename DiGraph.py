from src.GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self, **kwargs):
        self.nodes = {}
        self.nodes_size = 0
        self.edges_size = 0
        self.mc = 0

    def v_size(self) -> int:
        if self.nodes_size < 0:
            raise NotImplementedError
        return self.nodes_size

    def e_size(self) -> int:
        if self.edges_size < 0:
            raise NotImplementedError
        return self.edges_size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes[id1].out_edges

    def get_mc(self) -> int:
        # if self.mc < 0:
        #  raise NotImplementedError
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        # if id1 not in self.nodes.keys() or id2 not in self.nodes.keys():
        if self.nodes.get(id1) is None or self.nodes.get(id2) is None:
            return False
        if id1 == id2:
            return False

        self.nodes.get(id1).out_edges[id2] = weight
        self.nodes.get(id2).in_edges[id1] = weight
        self.mc += 1
        self.edges_size += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        n = Node(node_id, pos)
        self.nodes[node_id] = n
        self.mc += 1
        self.nodes_size += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False

        n = self.nodes[node_id]
        list_for_remove_out = []
        list_for_remove_in = []
        for i in n.out_edges:
            list_for_remove_out.append(i)

        for j in list_for_remove_out:
            self.remove_edge(node_id, j)
        for i in n.in_edges:
            list_for_remove_in.append(i)

        for j in list_for_remove_in:
            self.remove_edge(j, node_id)
        del self.nodes[node_id]
        self.nodes_size -= 1
        self.mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False

        if self.nodes.get(node_id1).out_edges[node_id2] is None or self.nodes.get(node_id2).in_edges[node_id1] is None:
            return False

        del self.nodes.get(node_id1).out_edges[node_id2]
        del self.nodes.get(node_id2).in_edges[node_id1]
        self.mc += 1
        self.edges_size -= 1
        return True
