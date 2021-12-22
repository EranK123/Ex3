import heapq
import json
import sys
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from queue import PriorityQueue
from dataclasses import dataclass, field


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name) as f:
            data = json.load(f)

        for node in data['Nodes']:
            self.graph.add_node(node['id'], node['pos'])
        for edge in data['Edges']:
            self.graph.add_edge(edge['src'], edge['dest'], edge['w'])
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as file:
                g = self.dict_graph()
                json.dump(g, file, indent=4)
        except IOError as e:
            return False
        return True

    def dict_of_node(self):

        Nodes = []
        for k, v in self.graph.get_all_v().items():
            print(v.location)
            node = {}
            temp_location = str((v.location))[1:-1]
            node["pos"] = str((temp_location).replace(' ', ''))
            node["id"] = k
            Nodes.append(node)
        return Nodes

    def dict_of_edge(self):
        Edges = []
        for k1 in self.graph.nodes.keys():
            for k2, v in self.graph.all_out_edges_of_node(k1).items():
                edges = {}
                edges["src"] = k1
                edges["weight"] = v
                edges["dest"] = k2
                Edges.append(edges)
        return Edges

    def dict_graph(self):
        my_dict = {}
        my_dict["Edges"] = self.dict_of_edge()
        my_dict["Nodes"] = self.dict_of_node()
        return my_dict

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path_list = self.path(id1, id2)
        dist = self.graph.nodes[id2].weight
        return dist, path_list

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        current_path = []
        cities_list = []
        min_list = sys.maxsize
        cities_temp_list = []
        min_temp = 0
        for i in range(len(node_lst)):
            first_time = False
            cities_temp_list.clear()
            cities_temp = node_lst.copy()
            min_temp = 0
            curr_node_index = i
            location = i
            while len(cities_temp) > 1:
                key = cities_temp[location]
                cities_temp.remove(key)
                self.dikjstra(self.graph.nodes[key])
                min_value = sys.maxsize
                for j in range(len(cities_temp)):
                    if min_value > self.graph.nodes[cities_temp[j]].weight:
                        min_value = self.graph.nodes[cities_temp[j]].weight
                        curr_node_index = cities_temp[j]
                        location = j
                if min_value == sys.maxsize:
                    break
                min_temp += min_value
                current_path = self.shortest_path_tsp(key, curr_node_index)
                if first_time:
                    current_path.pop(0)
                first_time = True
                cities_temp_list.extend(current_path)
            if min_list > min_temp:
                cities_list.clear()
                cities_list = cities_temp_list.copy()
                min_list = min_temp
        return cities_list, min_list

    def shortest_path_tsp(self, src, dest):
        path_list = []
        parent = dest
        while parent is not src:
            path_list.append(self.graph.nodes[parent].id)
            parent = self.graph.nodes[dest].tag
            dest = self.graph.nodes[parent].id

        path_list.append(self.graph.nodes[src].id)
        path_list.reverse()
        return path_list

    def centerPoint(self) -> (int, float):
        max_value = sys.maxsize
        key = -1
        for i in self.graph.nodes:
            node = self.graph.nodes[i]
            self.dikjstra(node)
            temp = self.get_max()
            if temp < max_value:
                max_value = temp
                key = node.id

        return key, max_value

    def get_max(self):
        max_value = -sys.maxsize - 1
        for i in self.graph.nodes:
            node_w = self.graph.nodes[i].weight
            if node_w > max_value:
                max_value = node_w
        return max_value

    def plot_graph(self) -> None:
        return

    def dikjstra(self, src: Node):
        self.set_tag()
        self.set_weight()
        visited = []
        pq = PriorityQueue()
        # pq = []
        self.graph.nodes[src.id].setWeight(0)
        pq.put(PrioritizedItem(src.weight, src))
        # heapq.heappush(pq, (src.weight, src))
        while len(visited) is not self.graph.nodes_size and pq.qsize() > 0:
            t = pq.get()
            r = t.get_id()
            # t = heapq.heappop(pq)
            # r = t[1]
            curr_node = self.graph.nodes[r]
            # curr_node = self.graph.nodes[r.id]
            if curr_node not in visited:
                visited.append(curr_node)
                self.adj(curr_node, pq, visited)

    def adj(self, node, pq, visited):
        current_dis = -1
        new_dis = -1
        e = self.graph.nodes[node.id].out_edges
        for nd in e:
            node_dest = self.graph.nodes[nd]

            if node_dest not in visited:
                current_dis = self.graph.nodes[node.id].out_edges[nd]
                new_dis = current_dis + node.weight

                if new_dis < node_dest.weight:
                    node_dest.setWeight(new_dis)
                    node_dest.setTag(node.id)

                pq.put(PrioritizedItem(node_dest.weight, node_dest))
                # if node_dest in pq:
                #  pq.remove(node_dest)
                #   heapq.heappush(pq, (node_dest.weight, node_dest))
                # else:
                #    heapq.heappush(pq, (node_dest.weight, node_dest))

    def path(self, src: int, dest: int):
        path_list = []
        self.shortest_path_dist(src, dest)
        parent = dest
        while parent is not src:
            path_list.append(self.graph.nodes[parent].id)
            parent = self.graph.nodes[dest].tag
            dest = self.graph.nodes[parent].id

        path_list.append(self.graph.nodes[src].id)
        path_list.reverse()
        return path_list

    def shortest_path_dist(self, src: int, dest: int):
        self.set_tag()
        self.dikjstra(self.graph.nodes[src])
        return self.graph.nodes[dest].weight

    def set_tag(self):
        for i in range(self.graph.nodes_size):
            self.graph.nodes[i].setTag(-1)

    def set_weight(self):
        for i in range(self.graph.nodes_size):
            self.graph.nodes[i].setWeight(sys.maxsize)


class PrioritizedItem:
    # priority: int
    # item: object = field()
    def __init__(self, weight, node):
        self.weight = weight
        self.node = node

    def __lt__(self, other):
        return self.weight < other.weight

    def get_id(self):
        return self.node.id




