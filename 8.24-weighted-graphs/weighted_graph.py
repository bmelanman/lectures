import dictionary as dct


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    # Insert the vertex into the matrix, mapped to a new, empty dictionary.
    pass


def add_edge(graph, vertex_u, vertex_v):
    # Get vertex_u's dictionary from the matrix.
    # Insert vertex_v into vertex_u's dictionary, mapped to 1.
    # Get vertex_v's dictionary from the matrix.
    # Insert vertex_u into vertex_v's dictionary, mapped to 1.
    # Increment the size.
    pass


def path(graph, vertex_u, vertex_v):
    # Create an empty queue of jobs.
    # Enqueue vertex_u to the queue of jobs.
    # Create an empty dictionary of predecessors.
    # Insert (vertex_u, vertex_u) into the dictionary of predecessors.
    # While the queue of jobs is non-empty, do:
    #     Dequeue a current vertex from the queue of jobs.
    #     If the current vertex is vertex_v, then:
    #         (the path to vertex_v is in the dictionary; return it)
    #     Get the current vertex's dictionary from the matrix.
    #     For each key (a neighbor) in the current vertex's dictionary, do:
    #         If the neighbor is not in the dictionary of predecessors, then:
    #             Enqueue the neighbor to the queue of jobs.
    #             Insert (neighbor, current) into the dictionary.
    # (there is no path to vertex_v)
    pass
