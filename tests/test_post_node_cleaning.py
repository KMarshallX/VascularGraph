#!/usr/bin/env python

"""Tests for CalcTools.post_node_cleaning."""

import unittest

import numpy as np

from VascGraph.GeomGraph import Graph
from VascGraph.Tools.CalcTools import post_node_cleaning


def make_graph(edges, n_nodes=None):
    if n_nodes is None:
        n_nodes=max(max(i) for i in edges)+1
    pos=[np.array([float(i), 0.0, 0.0]) for i in range(n_nodes)]
    return Graph(NodesPos=pos, Edges=edges)


def edge_set(graph):
    return set(tuple(sorted(i)) for i in graph.GetEdges())


class TestPostNodeCleaning(unittest.TestCase):

    def test_simple_path_keeps_only_endpoints(self):
        graph=make_graph([(0, 1), (1, 2), (2, 3)])

        cleaned=post_node_cleaning(graph)

        self.assertEqual(cleaned.number_of_nodes(), 2)
        self.assertEqual(cleaned.number_of_edges(), 1)
        self.assertEqual(sorted(len(cleaned.GetNeighbors(i)) for i in cleaned.GetNodes()),
                         [1, 1])

    def test_branch_graph_keeps_endpoints_and_branch_nodes(self):
        graph=make_graph([(0, 1), (1, 2), (2, 3), (2, 4), (4, 5)])

        cleaned=post_node_cleaning(graph)
        degrees=sorted(len(cleaned.GetNeighbors(i)) for i in cleaned.GetNodes())

        self.assertEqual(degrees, [1, 1, 1, 3])
        self.assertEqual(cleaned.number_of_nodes(), 4)

    def test_graph_without_degree_two_nodes_is_topologically_unchanged(self):
        graph=make_graph([(0, 1), (0, 2), (0, 3)])

        cleaned=post_node_cleaning(graph)

        self.assertEqual(cleaned.number_of_nodes(), graph.number_of_nodes())
        self.assertEqual(edge_set(cleaned), edge_set(graph))

    def test_input_graph_is_not_modified(self):
        graph=make_graph([(0, 1), (1, 2), (2, 3)])
        nodes_before=set(graph.GetNodes())
        edges_before=edge_set(graph)

        post_node_cleaning(graph)

        self.assertEqual(set(graph.GetNodes()), nodes_before)
        self.assertEqual(edge_set(graph), edges_before)

    def test_cleaned_graph_has_no_degree_two_nodes_for_branch_chains(self):
        graph=make_graph([(0, 1), (1, 2), (2, 3), (2, 4), (4, 5), (5, 6)])

        cleaned=post_node_cleaning(graph)

        self.assertNotIn(2, [len(cleaned.GetNeighbors(i)) for i in cleaned.GetNodes()])


if __name__ == '__main__':
    unittest.main()
