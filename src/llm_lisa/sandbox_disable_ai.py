"""
Basic OO representation of graphs
"""

from rich import print

# from dataclasses import dataclass
# from typing import Any

# @dataclass(frozen=True, slots=True)
# class Node_v2:
#     id: int
#     attrs: dict[str, Any] = {}


class Node:
    def __init__(self, id: int, **kwargs):
        self.id = id
        for k, v in kwargs.items():
            setattr(self, k, v)


node_store = [Node(id=id, some_field="PLACEHOLDER") for id in range(100)]


class Graph:
    """
    G=(V, E)
    G=(nodes, edges) - a graph is composed of a set of nodes and adjacency lists

    interface
    ==============

    >>> node_store = [Node(id=id, some_field="PLACEHOLDER") for id in range(100)]
    >>> g = Graph(nodes=node_store)
    >>> g.add_bi_edge(1, 2)
    >>> g.add_bi_edge(1, 3)
    >>> g.add_bi_edge(1, 4)
    >>> g.add_bi_edge(1, 5)
    # >>> g.bfs()
    # >>> g.dfc()
    # >>> g.kruskal()
    # >>> g.dystra()
    # >>> g.ph()
    """

    def __init__(self, nodes: list[Node]):
        self.edges = {node.id: [] for node in nodes}

    def add_bi_edge(self, id1: int, id2: int):
        # update adj
        self.edges[id1].append(id2)
        self.edges[id2].append(id1)


# interface example
graph = Graph(nodes=node_store)
graph.add_bi_edge(1, 2)
graph.add_bi_edge(1, 3)
graph.add_bi_edge(1, 4)

print(graph.edges)
if __name__ == "__main__":
    import doctest

    doctest.testmod()
