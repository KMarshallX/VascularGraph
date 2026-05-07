#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lazy geometric graph exports.
"""

import importlib


_EXPORTS = {
    'Graph': ('VascGraph.GeomGraph.Graph', 'Graph'),
    'GraphObject': ('VascGraph.GeomGraph.GraphObject', 'GraphObject'),
    'DiGraph': ('VascGraph.GeomGraph.DiGraph', 'DiGraph'),
    'GenerateDiGraph': ('VascGraph.GeomGraph.GenerateDiGraph', 'GenerateDiGraph'),
    'AnnotateDiGraph': ('VascGraph.GeomGraph.AnnotateDiGraph', 'AnnotateDiGraph'),
}

__all__ = list(_EXPORTS.keys())


def __getattr__(name):

    if name in _EXPORTS:
        module_name, attr_name = _EXPORTS[name]
        attr = getattr(importlib.import_module(module_name), attr_name)
        globals()[name] = attr
        return attr

    raise AttributeError(name)
