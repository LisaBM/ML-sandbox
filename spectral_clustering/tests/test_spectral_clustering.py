import spectral_clustering as sc


class TestGraph:

    @pytest.mark.parametrize("nodes,edges", [([1, 2], {(2, 1): 0.5})])
    def test_graph(self, nodes, edges):
        g = sc.Graph(nodes, edges)
        assert set(nodes) == set(g.nodes)
        assert set(edges.keys()) == set(g.edges.keys())
        for edge, weight in edges.items():
            assert g.edges[edge] == weight

    def test_graph_assert(self):
        with pytest.raises(RuntimeError):
            g = sc.Graph([1, 2], {(2, 3): 0.5})


class TestAdjacencyMatrix:

    @pytest.mark.parametrize("nodes,edges,expected", [([1, 2], {
        (2, 1): 0.5
    }, [[0, 0.5], [0.5, 0]])])
    def test_matrix_from_graph(self, nodes, edges, expected):
        graph = sc.Graph(nodes, edges)
        adjacency_matrix = sc.AdjacencyMatrix(graph)
        assert (adjacency_matrix.values.toarray() == expected).all()
