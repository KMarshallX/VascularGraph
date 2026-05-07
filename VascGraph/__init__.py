#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Top-level package exports for VascGraph.
"""

import importlib


__all__ = ['Skeletonize', 'GraphIO', 'GeomGraph', 'GraphValidation', 'Tools', 'GraphLab']


def __getattr__(name):

    if name in __all__:
        module = importlib.import_module('VascGraph.' + name)
        globals()[name] = module
        return module

    raise AttributeError(name)
