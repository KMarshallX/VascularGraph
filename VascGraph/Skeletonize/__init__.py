#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Lazy skeletonization exports.
"""

import importlib


_EXPORTS = {
    'BaseGraph': ('VascGraph.Skeletonize.BaseGraph', 'BaseGraph'),
    'GenerateGraph': ('VascGraph.Skeletonize.GenerateGraph', 'GenerateGraph'),
    'ContractGraph': ('VascGraph.Skeletonize.ContractGraph', 'ContractGraph'),
    'RefineGraph': ('VascGraph.Skeletonize.RefineGraph', 'RefineGraph'),
    'RefineGraphRadius': ('VascGraph.Skeletonize.RefineGraphRadius', 'RefineGraphRadius'),
    'Skel3D': ('VascGraph.Skeletonize.sknw', 'Skel3D'),
    'Skeleton': ('VascGraph.Skeletonize.Skeleton', 'Skeleton'),
}

__all__ = list(_EXPORTS.keys())


def __getattr__(name):

    if name in _EXPORTS:
        module_name, attr_name = _EXPORTS[name]
        attr = getattr(importlib.import_module(module_name), attr_name)
        globals()[name] = attr
        return attr

    if name == 'BinaryModels':
        module = importlib.import_module('VascGraph.Skeletonize.BinaryModels')
        globals()[name] = module
        return module

    raise AttributeError(name)
