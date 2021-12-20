class Location:

    def __init__(self, x, y, z):
        self.location = (x, y, z)


class Node:

    def __init__(self, id: int, location):
        self.id = id
        self.weight = 0
        self.tag = 0
        self.location = location
        self.in_edges = {}
        self.out_edges = {}

    def setWeight(self, weight):
        self.weight = weight

    def setTag(self, tag):
        self.tag = tag


