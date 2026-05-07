#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
GraphML writer for VascGraph geometric graphs.
"""

import json

import networkx as nx
import numpy as np


class WriteGraphml:

    def __init__(self, path='', name='output.graphml', graph=None):

        self.path = path
        self.name = name
        self.graph = graph

        if self.graph is None:
            print('Cannot write empty graph!')
            return

        graph_to_write = self.__graphml_graph(self.graph)
        nx.write_graphml(graph_to_write, self.__output_path())

    def __output_path(self):

        if self.name.split('.')[-1] != 'graphml':
            self.name = self.name + '.graphml'
        return self.path + self.name

    def __as_scalar(self, value):

        if isinstance(value, np.generic):
            return value.item()

        if isinstance(value, (str, int, float, bool)):
            return value

        return None

    def __jsonable(self, value):

        if isinstance(value, np.generic):
            return value.item()

        if isinstance(value, np.ndarray):
            return self.__jsonable(value.tolist())

        if isinstance(value, (list, tuple)):
            return [self.__jsonable(i) for i in value]

        if isinstance(value, set):
            return [self.__jsonable(i) for i in sorted(value)]

        if isinstance(value, dict):
            return dict((str(k), self.__jsonable(v)) for k, v in value.items())

        return value

    def __as_graphml_value(self, value):

        scalar = self.__as_scalar(value)
        if scalar is not None:
            return scalar

        if value is None:
            return None

        try:
            if isinstance(value, np.ndarray):
                return json.dumps(self.__jsonable(value), separators=(',', ':'))
        except:
            pass

        try:
            if isinstance(value, (list, tuple, set, dict)):
                return json.dumps(self.__jsonable(value), separators=(',', ':'))
        except:
            return str(value)

        return str(value)

    def __node_attrs(self, attrs):

        out = {}
        pos = attrs.get('pos', None)
        if pos is None:
            raise ValueError("Graph node is missing required 'pos' attribute.")

        try:
            out['X'] = float(pos[0])
            out['Y'] = float(pos[1])
            out['Z'] = float(pos[2])
        except:
            raise ValueError("Graph node 'pos' attribute must contain 3 coordinates.")

        for key, value in attrs.items():
            if key in ['X', 'Y', 'Z']:
                continue
            graphml_value = self.__as_graphml_value(value)
            if graphml_value is not None:
                out[key] = graphml_value

        return out

    def __edge_attrs(self, attrs):

        out = {}
        for key, value in attrs.items():
            graphml_value = self.__as_graphml_value(value)
            if graphml_value is not None:
                out[key] = graphml_value
        return out

    def __graphml_graph(self, graph):

        if nx.is_directed(graph):
            out = nx.DiGraph()
        else:
            out = nx.Graph()

        try:
            nodes = graph.GetNodes()
        except:
            nodes = list(graph.nodes())

        for node in nodes:
            try:
                attrs = dict(graph.node[node])
            except:
                attrs = dict(graph.nodes[node])
            node_attrs = self.__node_attrs(attrs)
            node_attrs['name'] = str(node)
            out.add_node(node, **node_attrs)

        try:
            edges = graph.GetEdges()
        except:
            edges = list(graph.edges())

        for edge in edges:
            u, v = edge[0], edge[1]
            try:
                attrs = dict(graph[u][v])
            except:
                attrs = {}
            out.add_edge(u, v, **self.__edge_attrs(attrs))

        return out

    def Update(self):

        pass
