
from collections import defaultdict, deque

"""
Undirected graph implemented using a dictonary.
"""


class Graph:
    def __init__(self, inital_adjacencies=None):
        self.graph = defaultdict()
        if inital_adjacencies is not None:
            self.initalaize_graph(inital_adjacencies)

    def initalaize_graph(self, adjacencies):
        # for the given adjacency list, adds all edges to graph
        for x, y in adjacencies:
            self.add_edge(x, y)

    def add_edge(self, vertex_one, vertex_two):
        # adds an edge to the graph, either by initalizing a new dict
        # entry or adding to an existing one for both vertexs
        if vertex_one in self.graph.keys():
            self.graph[vertex_one].add(vertex_two)
        else:
            self.graph[vertex_one] = {vertex_two}

        if vertex_two in self.graph.keys():
            self.graph[vertex_two].add(vertex_one)
        else:
            self.graph[vertex_two] = {vertex_one}

    def get_neighbors(self, vertex):
        # returns a set of all neighbors of a vertex, basically every vertex
        # that shares an edge with the given vertex
        return self.graph[vertex]

    def add_vertex(self, vertex):
        # adds a vertex that does not have any connections yet
        if vertex not in self.graph.keys():
            self.graph[vertex] = set()

    def are_adjecent(self, vertex_one, vertex_two):
        # checks if two vertexs are adjecent by seeing if they are conatined
        # in each other's neighbors lists
        if vertex_two in self.get_neighbors(vertex_one):
            if vertex_one in self.get_neighbors(vertex_two):
                return True
        return False

    def bfs_search(self, vertex):
        # does bfs search staring at the given vertex and then
        # returns list of states and predecesors
        state = defaultdict()
        pred = defaultdict()
        for v in self.graph.keys():
            state[v] = "undiscovered"
            pred[v] = None
        state[vertex] = "discovered"

        queue = deque()
        queue.append(vertex)
        while len(queue) > 0:
            top = queue.popleft()
            for n in self.get_neighbors(top):
                if state[n] == "undiscovered":
                    state[n] = "discovered"
                    pred[n] = top
                    queue.append(n)
            state[top] = "processed"
        return state, pred

    def reconstruct_bfs_path(self, pred, goal_node):
        # returns the path as a list that the bfs took given the end node and
        # the list of predecesors
        current_node = goal_node
        path = []
        while current_node is not None:
            path.insert(0, current_node)
            current_node = pred[current_node]
        return path

    def __str__(self):
        return str(dict(self.graph))
