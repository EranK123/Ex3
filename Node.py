class Location:

    def __init__(self,x,y,z):
        # self.x = x
        # self.y = y
        # self.z = z
        self.location = (x,y,z)




    # def __str__(self):
    #     dict = {"pos": self.location.x + "," + self.location.y + "," + self.location.z,}
    #     return dict


class Node:

    def __init__(self, id: int,location):
        self.id = id
        self.weight = 0
        self.tag = 0
        self.location = location
        self.in_edges = {}  # {node's id : weight}
        self.out_edges = {}  # {node's id : weight}

    def setWeight(self, weight):
        self.weight = weight

    def setTag(self, tag):
        self.tag = tag

    def set_location(self,x,y,z):
        self.location = (x,y,z)

    # def get_location(self):
    #     if self.location is None:
    #         self.location = (random(0,100), random(0,100), random(0,100))
    #     # self.location = (x,y,z)