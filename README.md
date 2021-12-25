# Ex3 212727283 - 315907113
In this assignment we are implementing a Directed Weighted Graph. The implementation of the graph relies on three classes: Node - a class we made to represent a node in the graph, DiGraph - a class which implements GraphInteface and GraphAlgo - a class which implements GraphAlgoInterface. It allows the user to run algorithms on the graph.

**Node** - This class, as said before, represents a node in the graph. The node consists of the fields id and location. The id field is the number of the node .Location is a class that defines the location of a certain node in space. It is defined by a tuple of x,y and z coordinates.
In addition, each node has weight and a tag. These are helpful fields which will help us find the shortest path and the actual path between two nodes. Will be explained later. Moreover, every node has a dictionary intialized to it. One representing edges going out of the node, one for edges going in the node. The dictionary will consist of key and value. The key will be the node’s destination id. The value will be the weight of the edges. For example if we have an edge from node 1 to node 2 with the weight 3, the out_edges dictionary will refer to the node whose id is 1. and the dictionary will look like this: {2,3}. In this way we have easy access to each edge if the node’s id is given.

**DiGraph** - This class represents a directed weighted graph. The initialization of the graph consists of nodes dictionary, edge size, node size and mc. The nodes dictionary will have a key which will be the node’s id and the value will be the actual node. mc will represent the number of manipulation we have done on the graph.
This class  allows the user to manipulate the graph using the methods:

*add_edge* - adds an edge to the graph. Given a node’s source id and a node’s destination id and weight, we access the out_edges dictionary in the destination 
position and add the weight. Same with in_edges dictionary just the opposite ids.

*add_node* - adds a new node to the graph. Given a location and the id, we access the graph nodes dictionary and add a new node.

*remove_node* - removes a node from the graph and all of its edges. Given a node’s id we access the node’s out_edges and in_edges and remove all the edges. Finally we remove the node from the graph nodes dictionary.

*remove_edge* - removes an edge from the graph. Given node’s source id and node’s destination id, we access the out_edges dict of the node’s and delete the edge and we access the in_edges dict of the destination node and delete the edge.

**GraphAlgo** - This class will run certain algorithms on the graph. The initialization of the graph consists of DiGraph. The class has couple of functions:

*get_graph* - returns the DiGraph initialized to GraphAlgo graph.

*load_from_json* - Given a json file name, the function will load the json file to a graph.

*save_to_json* - Given a file name, this function will save the graph to a the file.

*shortest_path* - This function will calculate the shortest path from a given node’s source id to a given destination node’s id. It will return the weight of the path and the actual path. The function uses the dikjstra algorithm. This algorithm finds the shortest path between node a and node b. It picks the source node, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited when done with all the neighbors. This algorithm will help us calculate the weight. To find the path we will use a help function called path. The function returns a list of Nodes representing the path. The list is ordered. This method uses the shortestPathDist function. In short, we save the parent of each node from the dikjstra algorithm in a tag variable which is defined in the Node class.
Specially for this algorithm we have created a help class which will determine how a Priority Queue will work. We need this because in dikjstra we extract the lowest cost route each iteration. This class is called PrioritizedItem and it has two parameters: a Node object and a node's weight. Using the __it__ function we can determing the priority of the objects in the priority queue which is their weights.

*TSP* - given a list of node’s ids called node_lst, a sub list of nodes in the graph, the method computes a list of consecutive nodes which go over all the nodes in cities. The sum of the weights of all the consecutive (pairs) of nodes is the "cost" of the solution.
The algorithm checks if the node_lst list is contained in the graph. It calculates the path using dijkstra from nodes in the list to another one. After it finds  the shortest path’s weight it  removes it from the list and calculates again from the end of the path and adds the new path(weight) to the list. It saves the weight. doing this for all the nodes in the cities list if found a better path(lower weight) it changes the list.

*centerPoint* - Returns the Node center of the graph. The center of a graph is the set of all vertices of minimum eccentricity, that is, the set of all vertices u where the greatest distance (weight) d(u,v) to other vertices v is minimal. Thus vertices in the center minimize the maximal distance from other points in the graph. We will use the dijkstra method of each node to compute the distances to all nodes in the graph.

*plot_graph* - this function plots the graph, i.e, it will draw the graph in a 2d space. It should show the desired graph the user wishes to draw. The graph will consists of all the nodes and the location of each node, the edges between them and the direction of each edge. It uses the matplotlib library.

**Tests** - we also included tests to the main classes, DiGraph and GraphAlgo. In the tests, using unittest, we have tested each function in each class to check if our implementation is correct or not. After finishing each method we checked it using unittest to find out if the method has flaws or not. This tool was extremely helpful in programming.

**Running the program** - 



**Some drawing examples using the matplotlib library:**

The check0 graph:


<img width="589" alt="Screen Shot 2021-12-25 at 10 50 22" src="https://user-images.githubusercontent.com/93202645/147381395-1c61feac-2b2a-4fe2-9ebc-e0a082560cf2.png">



The A5 graph:


<img width="611" alt="Screen Shot 2021-12-25 at 10 50 43" src="https://user-images.githubusercontent.com/93202645/147381400-a53670ab-1956-44dc-8eee-d82b964d1c1e.png">

A UML class diagram:

![GraphPythonUml](https://user-images.githubusercontent.com/93202645/147381341-4241f84c-e7b3-42c1-a452-8c41f5d8b4ea.png)





