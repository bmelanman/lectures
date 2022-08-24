import dictionary as dct


class WeightedGraph:
    """ A collection of vertices and weighted edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0


def add_vertex(graph, vertex):
    # Insert the vertex into the matrix, mapped to a new, empty dictionary.
    pass


def add_edge(graph, vertex_u, vertex_v, weight):
    # Get vertex_u's dictionary from the matrix.
    # Insert vertex_v into vertex_u's dictionary, mapped to weight.
    # Get vertex_v's dictionary from the matrix.
    # Insert vertex_u into vertex_v's dictionary, mapped to weight.
    # Increment the size.
    pass


def path(graph, vertex_u, vertex_v):
    # Create an empty priority queue of jobs.
    # Enqueue (0, vertex_u) to the priority queue of jobs.
    # Create an empty dictionary of predecessors.
    # Insert (vertex_u, vertex_u) into the dictionary of predecessors.
    # Create an empty dictionary of distances.
    # Insert (vertex_u, 0) into the dictionary of distances.
    # While the priority queue of jobs is non-empty, do:
    #     Dequeue a (priority, vertex) from the priority queue of jobs.
    #     Set a temporary variable to -1 * priority.
    #     If temp > the distance to the vertex, then:
    #         (there is already a better path; continue and ignore this one)
    #     Else if the current vertex is vertex_v, then:
    #         (the path to vertex_v is in the dictionary; return it)
    #     Get the current vertex's dictionary from the matrix.
    #     For each key (a neighbor) in the current vertex's dictionary, do:
    #         If the neighbor has no predecessor or if has a distance such that
    #          distance > temp + weight, then:
    #             Enqueue (-1 * (temp + weight), neighbor).
    #             Insert (neighbor, current) into the predecessors dict.
    #             Insert (neighbor, temp + weight) into the distances dict.
    # (there is no path to vertex_v)
    pass
