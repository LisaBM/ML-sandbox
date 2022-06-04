from typing import List, Mapping, Tuple

from scipy import sparse


class Graph:

    def __init__(self, nodes: List, edges: Mapping[Tuple, float]):
        if not set(nodes) >= set(n for e in edges for n in e):
            raise RuntimeError("Unexpected node detected.")
        self._nodes = nodes
        self._edges = edges

    @property
    def nodes(self) -> List:
        return self._nodes

    @property
    def edges(self) -> Mapping[Tuple, float]:
        return self._edges

    @property
    def n_nodes(self) -> int:
        return len(self.nodes)


class AdjacencyMatrix:

    def __init__(self, graph: Graph):
        self._graph = graph
        self._node_mapping = {
            node: i for i, node in enumerate(self._graph.nodes)
        }
        self._values = self._matrix_from_graph()

    @property
    def graph(self):
        return self._graph

    @property
    def values(self):
        return self._values

    def _matrix_from_graph(self) -> sparse._csr.csr_matrix:
        values = []
        start_points = []
        end_points = []
        for (start_point, end_point), value in self._graph.edges.items():
            values.append(value)
            start_points.append(self._node_mapping[start_point])
            end_points.append(self._node_mapping[end_point])

        matrix = sparse.coo_matrix(
            (values, (start_points, end_points)),
            shape=(self.graph.n_nodes, self.graph.n_nodes))
        return matrix + matrix.transpose()
